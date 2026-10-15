import javax.swing.*;
import java.awt.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.UUID;

/**
 * LAB Work 1: Attendance Tracker
 * Java Swingを使用した出席追跡アプリケーション。
 */
public class AttendanceTracker1 extends JFrame {

    // 修正したところ1: ここにインスタンス変数として宣言（超重要！）
    private JTextField nameField;
    private JTextField courseField;
    private JTextField timeInField;
    private JTextField eSignatureField;

    public AttendanceTracker1() {
        // ウィンドウの基本設定
        setTitle("Attendance Tracker");
        setSize(600, 400);  // 少し大きくして見やすく
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // JPanelを作成
        JPanel panel = new JPanel(new GridBagLayout());
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        add(panel);

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10);
        gbc.anchor = GridBagConstraints.WEST;

        // 1. Attendance Name
        gbc.gridx = 0; gbc.gridy = 0;
        panel.add(new JLabel("Attendance Name:"), gbc);
        gbc.gridx = 1;
        nameField = new JTextField(20);
        panel.add(nameField, gbc);

        // 2. Course/Year
        gbc.gridx = 0; gbc.gridy = 1;
        panel.add(new JLabel("Course/Year:"), gbc);
        gbc.gridx = 1;
        courseField = new JTextField(20);
        panel.add(courseField, gbc);

        // 3. Time In
        gbc.gridx = 0; gbc.gridy = 2;
        panel.add(new JLabel("Time In:"), gbc);
        gbc.gridx = 1;
        timeInField = new JTextField(20);
        timeInField.setEditable(false);
        panel.add(timeInField, gbc);

        // 4. E-Signature
        gbc.gridx = 0; gbc.gridy = 3;
        panel.add(new JLabel("E-Signature:"), gbc);
        gbc.gridx = 1;
        eSignatureField = new JTextField(20);
        eSignatureField.setEditable(false);
        panel.add(eSignatureField, gbc);

        // 修正したところ2: ここで自動生成を呼び出す
        refreshTimeAndSignature();

        // Refreshボタン
        gbc.gridx = 0; gbc.gridy = 4; gbc.gridwidth = 2;
        gbc.anchor = GridBagConstraints.CENTER;
        JButton refreshButton = new JButton("Refresh Time & Signature");
        refreshButton.addActionListener(e -> refreshTimeAndSignature());
        panel.add(refreshButton, gbc);
    }

    // 修正したところ3: 自動生成用のメソッドを作成（ボタンからも呼び出せる）^
    private void refreshTimeAndSignature() {
        // 現在時刻を設定
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        timeInField.setText(LocalDateTime.now().format(formatter));

        // E-Signature生成（8文字大文字）
        String uuid = UUID.randomUUID().toString().replaceAll("-", "");
        String shortSignature = uuid.substring(0, 8).toUpperCase();
        eSignatureField.setText(shortSignature);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new AttendanceTrackerfirst().setVisible(true);
        });
    }
}