import java.io.*;
import java.util.*;

public class MP19 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter dataset file path: ");
        String path = input.nextLine();

        File file = new File(path);
        if (!file.exists() || !file.isFile()) {
            System.out.println("Invalid file path.");
            return;
        }

        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String header = br.readLine(); // ヘッダー行
            String line;
            int total = 0;
            int passCount = 0, failCount = 0;
            int sumScore = 0;
            int maxScore = Integer.MIN_VALUE;
            int minScore = Integer.MAX_VALUE;

            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                if (values.length < 8) continue; // 不完全行はスキップ

                int score = Integer.parseInt(values[6]);
                String result = values[7];

                sumScore += score;
                maxScore = Math.max(maxScore, score);
                minScore = Math.min(minScore, score);
                total++;

                if (result.equals("PASS")) passCount++;
                else if (result.equals("FAIL")) failCount++;
            }

            System.out.println("=== Dataset Summary Report ===");
            System.out.println("Total records: " + total);
            System.out.println("Average score: " + (sumScore / (double) total));
            System.out.println("Highest score: " + maxScore);
            System.out.println("Lowest score: " + minScore);
            System.out.println("Pass count: " + passCount);
            System.out.println("Fail count: " + failCount);

        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }
}
