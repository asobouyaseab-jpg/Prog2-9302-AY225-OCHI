import javax.swing.*;
import java.awt.*;
import java.time.LocalDateTime;
import java.util.UUID;

/**
 * LAB Work 1: Attendance Tracker
 * Java Swingを使用した出席追跡アプリケーション。
 * JFrameにラベル付きフィールドを表示し、システム日時とE-Signatureを自動生成。
 * @author Your Name
 */
public class AttendanceTrackerfirst extends JFrame {

    public AttendanceTrackerfirst() {
        // ウィンドウの基本設定
        setTitle("Attendance Tracker");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null); // 画面中央に表示

        // メインコンテナをGridBagLayoutで設定（柔軟な配置用）
        setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 5, 10); // コンポーネント間の余白
        gbc.anchor = GridBagConstraints.WEST;

        // JPanelを作成してフィールドをグループ化（読みやすさ向上）
        JPanel panel = new JPanel(new GridBagLayout());
        panel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
        add(panel, gbc);

        // 1. Attendance Name フィールド
        gbc.gridx = 0; gbc.gridy = 0;
        panel.add(new JLabel("Attendance Name:"), gbc);
        gbc.gridx = 1;
        JTextField nameField = new JTextField(20);
        panel.add(nameField, gbc);

        // 2. Course/Year フィールド
        gbc.gridx = 0; gbc.gridy = 1;
        panel.add(new JLabel("Course/Year:"), gbc);
        gbc.gridx = 1;
        JTextField courseField = new JTextField(20);
        panel.add(courseField, gbc);

        // 3. Time In フィールド（システム日時自動取得）
        gbc.gridx = 0; gbc.gridy = 2;
        panel.add(new JLabel("Time In:"), gbc);
        gbc.gridx = 1;
        JTextField timeInField = new JTextField(20);
        // 現在の日時を取得して設定（フォーマット調整）
        String timeIn = LocalDateTime.now().format(java.time.format.DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        timeInField.setText(timeIn);
        timeInField.setEditable(false); // 編集不可
        panel.add(timeInField, gbc);

        // 4. E-Signature フィールド（UUIDでユニーク生成）
        gbc.gridx = 0; gbc.gridy = 3;
        panel.add(new JLabel("E-Signature:"), gbc);
        gbc.gridx = 1;
        JTextField eSignatureField = new JTextField(20);
        // ユニークなE-Signatureを生成
        String eSignature = UUID.randomUUID().toString().substring(0, 8).toUpperCase(); // 短くフォーマット
        eSignatureField.setText(eSignature);
        eSignatureField.setEditable(false); // 編集不可
        panel.add(eSignatureField, gbc);

        // ボタンでリフレッシュ（オプション：再生成）
        gbc.gridx = 0; gbc.gridy = 4; gbc.gridwidth = 2;
        gbc.anchor = GridBagConstraints.CENTER;
        JButton refreshButton = new JButton("Refresh Time & Signature");
        refreshButton.addActionListener(e -> {
            timeInField.setText(LocalDateTime.now().format(java.time.format.DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")));
            eSignatureField.setText(UUID.randomUUID().toString().substring(0, 8).toUpperCase());
        });
        panel.add(refreshButton, gbc);
    }

    // メイン関数：プログラム実行
    public static void main(String[] args) {
        // SwingはEvent Dispatch Threadで実行
        SwingUtilities.invokeLater(() -> {
            new AttendanceTracker1().setVisible(true);
        });
    }
}