import java.io.*;
import java.util.*;

public class DataAudit {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        File file;

        // ファイルパス入力 & 検証ループ
        while (true) {
            System.out.print("Enter dataset file path: ");
            String path = input.nextLine();
            file = new File(path);

            if (!file.exists() || !file.isFile()) {
                System.out.println("Invalid file path. Please try again.");
                continue;
            }
            if (!path.endsWith(".csv")) {
                System.out.println("Error: File is not in CSV format.");
                continue;
            }
            break; // valid file
        }

        // CSV 読み込み & データ品質チェック
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            List<DataRecord> records = new ArrayList<>();

            br.readLine(); // ヘッダー行を読み飛ばす（変数に入れない）

            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                records.add(new DataRecord(values));
            }

            Validator validator = new Validator(records);
            validator.runChecks();

        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        } finally {
            input.close(); // Scanner を閉じる
        }
    }
}

// CSVの1行を表すクラス
class DataRecord {
    String title;
    String console;
    double sales;
    String publisher;
    String developer;
    String date;

    public DataRecord(String[] values) {
        this.title = values.length > 0 ? values[0] : null;
        this.console = values.length > 1 ? values[1] : null;
        this.sales = values.length > 2 && !values[2].isEmpty() ? Double.parseDouble(values[2]) : 0;
        this.publisher = values.length > 3 ? values[3] : null;
        this.developer = values.length > 4 ? values[4] : null;
        this.date = values.length > 5 ? values[5] : null;
    }
}

// データ品質チェックを行うクラス
class Validator {
    List<DataRecord> records;

    public Validator(List<DataRecord> records) {
        this.records = records;
    }

    public void runChecks() {
        System.out.println("=== Data Quality Report ===");
        checkMissing();
        checkNegativeSales();
        checkInvalidDates();
        checkDuplicates();
    }

    private void checkMissing() {
        long missingPublisher = records.stream().filter(r -> r.publisher == null || r.publisher.isEmpty()).count();
        long missingDeveloper = records.stream().filter(r -> r.developer == null || r.developer.isEmpty()).count();
        System.out.println("Missing Publisher: " + missingPublisher);
        System.out.println("Missing Developer: " + missingDeveloper);
    }

    private void checkNegativeSales() {
        long negativeSales = records.stream().filter(r -> r.sales < 0).count();
        System.out.println("Negative Sales: " + negativeSales);
    }

    private void checkInvalidDates() {
        long invalidDates = records.stream().filter(r -> r.date != null && !isValidDate(r.date)).count();
        System.out.println("Invalid Dates: " + invalidDates);
    }

    private boolean isValidDate(String date) {
        return date.matches("\\d{4}-\\d{2}-\\d{2}");
    }

    private void checkDuplicates() {
        Set<String> seen = new HashSet<>();
        long duplicates = records.stream()
            .filter(r -> !seen.add(r.title + r.console))
            .count();
        System.out.println("Duplicate Records: " + duplicates);
    }
}
