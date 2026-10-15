import javax.swing.*;
import java.awt.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.UUID;

/**
 * LAB Work 1: Attendance Tracker
 * Java Swingを使用した出席追跡アプリケーション。
 */
public class AttendanceTrackerprot extends JFrame {

    private JTextField nameField;
    private JTextField courseField;
    private JTextField timeInField;
    private JTextField eSignatureField;

    public AttendanceTrackerprot() {
        setTitle("Attendance Tracker");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel panel = new JPanel(new GridBagLayout());
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        add(panel);

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10);
        gbc.anchor = GridBagConstraints.WEST;

        // Attendance Name
        gbc.gridx = 0; gbc.gridy = 0;
        panel.add(new JLabel("Attendance Name:"), gbc);
        gbc.gridx = 1;
        nameField = new JTextField(20);
        panel.add(nameField, gbc);

        // Course/Year
        gbc.gridx = 0; gbc.gridy = 1;
        panel.add(new JLabel("Course/Year:"), gbc);
        gbc.gridx = 1;
        courseField = new JTextField(20);
        panel.add(courseField, gbc);

        // Time In
        gbc.gridx = 0; gbc.gridy = 2;
        panel.add(new JLabel("Time In:"), gbc);
        gbc.gridx = 1;
        timeInField = new JTextField(20);
        timeInField.setEditable(false);
        panel.add(timeInField, gbc);

        // E-Signature
        gbc.gridx = 0; gbc.gridy = 3;
        panel.add(new JLabel("E-Signature:"), gbc);
        gbc.gridx = 1;
        eSignatureField = new JTextField(20);
        eSignatureField.setEditable(false);
        panel.add(eSignatureField, gbc);

        // Refreshボタン
        gbc.gridx = 0; gbc.gridy = 4; gbc.gridwidth = 2;
        gbc.anchor = GridBagConstraints.CENTER;
        JButton refreshButton = new JButton("Refresh Time & Signature");
        refreshButton.addActionListener(e -> refreshTimeAndSignature());
        panel.add(refreshButton, gbc);

        // ★最終強化：レイアウト確定後に生成（これで絶対反映される！）
        pack();  // 追加：コンポーネントサイズを確定
        refreshTimeAndSignature();  // 自動生成
    }

    private void refreshTimeAndSignature() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        timeInField.setText(LocalDateTime.now().format(formatter));

        String uuid = UUID.randomUUID().toString().replaceAll("-", "");
        String shortSignature = uuid.substring(0, 8).toUpperCase();
        eSignatureField.setText(shortSignature);

        // 追加：強制再描画（これで確実に表示更新）
        timeInField.repaint();
        eSignatureField.repaint();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            AttendanceTrackerfirst tracker = new AttendanceTrackerfirst();
            tracker.setVisible(true);
        });
    }
}