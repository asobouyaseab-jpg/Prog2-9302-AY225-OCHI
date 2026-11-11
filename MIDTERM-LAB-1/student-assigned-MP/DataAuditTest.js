const fs = require('fs');
const readline = require('readline');
const path = require('path');

function validateFilePath(filePath) {
    if (!fs.existsSync(filePath)) {
        console.log("Error: File does not exist.");
        return false;
    }
    try {
        fs.accessSync(filePath, fs.constants.R_OK);
    } catch (err) {
        console.log("Error: File is not readable.");
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

function runChecks(records) {
    // 欠損値チェック Missing values
    const missingCounts = {};
    records.forEach(record => {
        for (let key in record) {
            if (!record[key] || record[key] === '') {
                missingCounts[key] = (missingCounts[key] || 0) + 1;
            }
        }
    });

    // 負の売上チェック  Negative sales
    const negativeSales = records.filter(r => parseFloat(r.total_sales) < 0);

    // 不正日付チェック（例: YYYY-MM-DD） Invalid dates
    const invalidDates = records.filter(r => r.date && !/^\d{4}-\d{2}-\d{2}$/.test(r.date));

    // 重複チェック（title + console） Duplicate records
    const seen = new Set();
    const duplicates = records.filter(r => {
        const key = r.title + r.console;
        if (seen.has(key)) return true;
        seen.add(key);
        return false;
    });

    console.log("=== Data Quality Report ===");
    console.log("Missing Values:", missingCounts);
    console.log("Negative Sales:", negativeSales.length);
    console.log("Invalid Dates:", invalidDates.length);
    console.log("Duplicate Records:", duplicates.length);
}

async function main() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    let filePath;
    while (true) {
        filePath = await new Promise(resolve => rl.question("Enter dataset file path: ", resolve));
        if (validateFilePath(filePath)) break;
    }

    try {
        const records = parseCSV(filePath);
        runChecks(records);
    } catch (err) {
        console.log("Error processing file:", err.message);
    } finally {
        rl.close();
    }
}

main();
