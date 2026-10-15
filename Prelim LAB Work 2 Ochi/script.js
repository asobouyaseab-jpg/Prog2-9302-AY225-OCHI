// script.js
// beep.mp3 を読み込んで再生準備
const beepSound = new Audio('beep.mp3');

document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;

    // This is also my name and student ID number. I don't know if I should change it when I submit it.
    const correctUsername = "Nobutoshi Ochi";   
    const correctPassword = "241786978";      

    if (username === correctUsername && password === correctPassword) {
        // ログイン成功

        // 現在時刻を取得・フォーマット
        const now = new Date();
        const timestamp = now.getFullYear() + '-' +
                          String(now.getMonth() + 1).padStart(2, '0') + '-' +
                          String(now.getDate()).padStart(2, '0') + ' ' +
                          String(now.getHours()).padStart(2, '0') + ':' +
                          String(now.getMinutes()).padStart(2, '0') + ':' +
                          String(now.getSeconds()).padStart(2, '0');

        // 表示
        document.getElementById('displayName').textContent = username;
        document.getElementById('timestamp').textContent = timestamp;
        document.getElementById('welcome').style.display = 'block';

        // 出席記録ファイルの自動ダウンロード
        const attendanceText = `Username: ${username}\nTimestamp: ${timestamp}\n`;
        const blob = new Blob([attendanceText], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);

        const a = document.createElement('a');
        a.href = url;
        a.download = 'attendance_summary.txt';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

    }else {
        // ログイン失敗 → 指示通りに beep.mp3 を再生
        beepSound.currentTime = 0;  // 最初から再生（連続失敗しても重ねない）
        beepSound.play();
        alert('Username or password is incorrect. Please try again.');
    }
});