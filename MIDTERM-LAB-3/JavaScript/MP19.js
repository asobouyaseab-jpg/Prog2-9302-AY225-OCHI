const fs = require('fs');
const readline = require('readline');
const path = require('path');

function validateFilePath(filePath) {
    if (!fs.existsSync(filePath)) {
        console.log("Error: File does not exist.");
        return false;
    }
    if (path.extname(filePath) !== '.csv') {
        console.log("Error: File is not in CSV format.");
        return false;
    }
    return true;
}

function parseCSV(filePath) {
    const data = fs.readFileSync(filePath, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');
    const headers = lines[0].split(',');
    const records = lines.slice(1).map(line => {
        const values = line.split(',');
        return Object.fromEntries(headers.map((h, i) => [h.trim(), values[i] ? values[i].trim() : null]));
    });
    return records;
}

function generateSummary(records) {
    let total = records.length;
    let sumScore = 0, passCount = 0, failCount = 0;
    let maxScore = -Infinity, minScore = Infinity;

    records.forEach(r => {
        const score = parseInt(r.Score);
        const result = r.Result;
        if (!isNaN(score)) {
            sumScore += score;
            maxScore = Math.max(maxScore, score);
            minScore = Math.min(minScore, score);
        }
        if (result === "PASS") passCount++;
        else if (result === "FAIL") failCount++;
    });

    console.log("=== Dataset Summary Report ===");
    console.log("Total records:", total);
    console.log("Average score:", (sumScore / total).toFixed(2));
    console.log("Highest score:", maxScore);
    console.log("Lowest score:", minScore);
    console.log("Pass count:", passCount);
    console.log("Fail count:", failCount);
}

async function main() {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    let filePath;
    while (true) {
        filePath = await new Promise(resolve => rl.question("Enter dataset file path: ", resolve));
        if (validateFilePath(filePath)) break;
    }
    const records = parseCSV(filePath);
    generateSummary(records);
    rl.close();
}

main();
