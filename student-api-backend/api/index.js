const connectToDatabase = require('../db.js');  // さっき作ったdb.jsを読み込んで使えるようにする
const mongoose = require('mongoose');

// 1. データベースに保存するデータの「形」を決める設計図
const RecordSchema = new mongoose.Schema({
  title: String,   // タイトル（文字列）
  content: String  // 内容（文字列）
}, { timestamps: true }); // 自動で「作成日時」と「更新日時」を記録する機能

// 2. 設計図を元に、データを操作するための「Record」という名前のロボット（モデル）を作る
const Record = mongoose.models.Record || mongoose.model('Record', RecordSchema);

module.exports = async (req, res) => {

      res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');   // 全てのウェブサイトからの通信を許可する
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS'); // 許可する通信の種類
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // ブラウザが最初に行う「通信して大丈夫？」という事前確認（OPTIONS）に対する返答
  if (req.method === 'OPTIONS') {
    return res.status(200).end(); // 「大丈夫だよ」とだけ返す
  }

    try {
    await connectToDatabase(); // まず、さっきのdb.jsを呼び出してデータベースに繋ぐ

        if (req.method === 'GET') {
      // データベースからすべてのデータを検索（find）し、作成日時が新しい順（createdAt: -1）に並び替える
      const records = await Record.find({}).sort({ createdAt: -1 });
      return res.status(200).json(records); // 取得したデータを画面に送る
    }

        if (req.method === 'POST') {
      // 画面から送られてきたデータ（req.body）をそのままデータベースに保存（create）する
      const newRecord = await Record.create(req.body);
      return res.status(201).json(newRecord); // 保存完了したデータを画面に「成功したよ」と送る
    }

        // GETでもPOSTでもない怪しい通信が来たらエラーにする
    return res.status(405).json({ error: 'Method Not Allowed' });
  } catch (error) {
    console.error(error); // エラー内容をログに記録
    // データベース接続失敗などの重大なエラーは「500」を返す
    return res.status(500).json({ error: 'Database connection failed' });
  }
};
