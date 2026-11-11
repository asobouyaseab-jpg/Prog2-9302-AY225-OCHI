import java.io.*;
import java.util.*;

public class MP20 {
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
            String[] keys = header.split(",");
            String line;
            List<Map<String, String>> jsonList = new ArrayList<>();

            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                Map<String, String> obj = new LinkedHashMap<>();
                for (int i = 0; i < keys.length && i < values.length; i++) {
                    obj.put(keys[i], values[i]);
                }
                jsonList.add(obj);
            }

            // JSON風に出力
            System.out.println("=== CSV to JSON ===");
            System.out.println(jsonList);

        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }
}
