import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.UUID;

public class AttendanceTracker extends JFrame {

    private JTextField nameField;
    private JTextField courseField;
    private JTextField timeField;
    private JTextField signatureField;

    public AttendanceTracker() {
        // ウィンドウ設定
        setTitle("Attendance Tracker");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(520, 320);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));

        // フォームパネル
        JPanel formPanel = new JPanel(new GridLayout(5, 2, 10, 12));
        formPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        // フィールド作成
        nameField = new JTextField(20);
        courseField = new JTextField(20);

        timeField = new JTextField(20);
        timeField.setEditable(false);
        timeField.setBackground(new Color(240, 240, 240));

        signatureField = new JTextField(30);
        signatureField.setEditable(false);
        signatureField.setBackground(new Color(245, 245, 220));

        // ラベルとフィールド追加
        formPanel.add(new JLabel("Name:"));
        formPanel.add(nameField);
        formPanel.add(new JLabel("Course/Year:"));
        formPanel.add(courseField);
        formPanel.add(new JLabel("Time In:"));
        formPanel.add(timeField);
        formPanel.add(new JLabel("E-Signature:"));
        formPanel.add(signatureField);

        // ボタンパネル
        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 30, 10));
        JButton recordButton = new JButton("Record");
        JButton clearButton = new JButton("Clear");
        JButton exitButton = new JButton("Exit");

        recordButton.addActionListener(new RecordListener());
        clearButton.addActionListener(e -> clearFields());
        exitButton.addActionListener(e -> System.exit(0));

        buttonPanel.add(recordButton);
        buttonPanel.add(clearButton);
        buttonPanel.add(exitButton);

        // メインに追加
        add(formPanel, BorderLayout.CENTER);
        add(buttonPanel, BorderLayout.SOUTH);

        // 初回に時刻と署名を設定
        updateTimeAndSignature();

        // 毎秒更新したい場合はタイマー（オプション）
        // new Timer(1000, e -> updateTimeAndSignature()).start();
    }

    private void updateTimeAndSignature() {
        // 現在時刻のフォーマット
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        timeField.setText(LocalDateTime.now().format(formatter));

        // ユニークな署名（UUID）
        signatureField.setText(UUID.randomUUID().toString());
    }

    private void clearFields() {
        nameField.setText("");
        courseField.setText("");
        updateTimeAndSignature();
    }

    // 記録ボタンの処理
    private class RecordListener implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            String name = nameField.getText().trim();
            String course = courseField.getText().trim();

            if (name.isEmpty() || course.isEmpty()) {
                JOptionPane.showMessageDialog(null,
                        "Please type Name and Course/Year",
                        "Input Error", JOptionPane.WARNING_MESSAGE);
                return;
            }

            // 記録直前に最新の時刻・署名を更新（重要）
            updateTimeAndSignature();

            String time = timeField.getText();
            String signature = signatureField.getText();

            // txtファイルに追記
            String today = LocalDate.now().format(DateTimeFormatter.ofPattern("yyyyMMdd"));
            String fileName = "attendance_log_" + today + "_NobutoshiOchi.txt";
            try (FileWriter writer = new FileWriter(fileName, true)) {  // true = 追記モード
                String line = String.format("%s,%s,%s,%s%n",
                        name, course, time, signature);
                writer.write(line);
                JOptionPane.showMessageDialog(null,
                        "Recorded!\n" + name + " (" + course + ")",
                        "SUCCESS", JOptionPane.INFORMATION_MESSAGE);
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(null,
                        "ファイル保存に失敗しました。\n" + ex.getMessage(),
                        "Error", JOptionPane.ERROR_MESSAGE);
            }

            // 入力クリアして次の記録へ
            clearFields();
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new AttendanceTracker().setVisible(true);
        });
    }
}
