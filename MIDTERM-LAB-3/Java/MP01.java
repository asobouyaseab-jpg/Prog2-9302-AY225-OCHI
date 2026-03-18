import java.io.*;
import java.util.*;

public class MP01 {
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
            String header = br.readLine(); // ヘッダー行を読み飛ばす
            int total = 0;
            while (br.readLine() != null) {
                total++;
            }
            System.out.println("=== Record Count ===");
            System.out.println("Total records: " + total);
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        } finally {
            input.close();
        }
    }
}
