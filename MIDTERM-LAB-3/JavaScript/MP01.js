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
    return lines;
}

async function main() {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    let filePath;
    while (true) {
        filePath = await new Promise(resolve => rl.question("Enter dataset file path: ", resolve));
        if (validateFilePath(filePath)) break;
    }

    try {
        const lines = parseCSV(filePath);
        const totalRecords = lines.length - 1; // ヘッダーを除外
        console.log("=== Record Count ===");
        console.log("Total records:", totalRecords);
    } catch (err) {
        console.log("Error processing file:", err.message);
    } finally {
        rl.close();
    }
}

main();
