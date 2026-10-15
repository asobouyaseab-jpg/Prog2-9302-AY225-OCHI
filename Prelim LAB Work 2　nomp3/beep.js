// beep.js - Audioファイルなしでビープ音を鳴らす
function beep() {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) {
        console.log("Web Audio API not supported");
        return;
    }

    const audioCtx = new AudioContext();

    const oscillator = audioCtx.createOscillator();
    oscillator.type = "square";           // ビープらしい音
    oscillator.frequency.setValueAtTime(800, audioCtx.currentTime); // 800Hz

    const gainNode = audioCtx.createGain();
    gainNode.gain.setValueAtTime(0.2, audioCtx.currentTime);       // 音量控えめ

    oscillator.connect(gainNode);
    gainNode.connect(audioCtx.destination);

    oscillator.start();
    oscillator.stop(audioCtx.currentTime + 0.5); // 指定した秒のビープ
}