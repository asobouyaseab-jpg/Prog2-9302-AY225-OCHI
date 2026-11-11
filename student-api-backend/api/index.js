const connectToDatabase = require('../db'); // 1つ上の階層にあるdb.jsを読み込む
const mongoose = require('mongoose');

// 1. 出席データ用の「形」を決める設計図（課題指定の4項目）
const AttendanceSchema = new mongoose.Schema({
  date: { type: String, required: true },        // 日付 (例: "2026-11-12")
  subjectName: { type: String, required: true }, // 科目名 (例: "Database Systems")
  section: { type: String, required: true },     // セクション (例: "BSIT-3A")
  studentName: { type: String, required: true }  // 学生名 (例: "Taro Yamada")
}, { timestamps: true });

// 2. 設計図を元に、データを操作するための「Attendance」モデルを作る
const Attendance = mongoose.models.Attendance || mongoose.model('Attendance', AttendanceSchema);

module.exports = async (req, res) => {
  // CORS設定（GET, POST, PUT, DELETE すべてを許可するように拡張）
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // ブラウザの事前確認（OPTIONS）への返答
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  try {
    await connectToDatabase(); // データベースに接続

    // 【Read: 読込】すべての出席記録を取得する
    if (req.method === 'GET') {
      const records = await Attendance.find({}).sort({ createdAt: -1 });
      return res.status(200).json(records);
    }

    // 【Create: 作成】新しい出席記録を追加する
    if (req.method === 'POST') {
      const newRecord = await Attendance.create(req.body);
      return res.status(201).json(newRecord);
    }

    // 【Update: 更新】既存の出席記録を編集する（URLの ?id=... で対象を指定）
    if (req.method === 'PUT') {
      const { id } = req.query;
      if (!id) {
        return res.status(400).json({ error: '更新するデータのIDが必要です' });
      }
      const updatedRecord = await Attendance.findByIdAndUpdate(id, req.body, {
        new: true, // 更新後の新しいデータを返す設定
        runValidators: true
      });
      if (!updatedRecord) {
        return res.status(404).json({ error: '指定されたデータが見つかりません' });
      }
      return res.status(200).json(updatedRecord);
    }

    // 【Delete: 削除】誤った・重複した出席記録を削除する（URLの ?id=... で対象を指定）
    if (req.method === 'DELETE') {
      const { id } = req.query;
      if (!id) {
        return res.status(400).json({ error: '削除するデータのIDが必要です' });
      }
      const deletedRecord = await Attendance.findByIdAndDelete(id);
      if (!deletedRecord) {
        return res.status(404).json({ error: '指定されたデータが見つかりません' });
      }
      return res.status(200).json({ message: '削除に成功しました', id });
    }

    // 上記以外の通信メソッドが来た場合
    return res.status(405).json({ error: 'Method Not Allowed' });

  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: 'サーバーまたはデータベースのエラーが発生しました' });
  }
};
