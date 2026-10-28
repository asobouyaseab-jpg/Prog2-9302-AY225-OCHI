const connectToDatabase = require('../db.js'); // 1つ上のフォルダにあるdb.jsを読み込む
const mongoose = require('mongoose');

// 1. データベースに保存するデータの「形」を決める設計図
const RecordSchema = new mongoose.Schema({
  title: String,   // タイトル（文字列）
  content: String  // 内容（文字列）
}, { timestamps: true }); // 自動で「作成日時」と「更新日時」を記録する機能

// 2. 設計図を元に、データを操作するための「Record」という名前のモデルを作る
const Record = mongoose.models.Record || mongoose.model('Record', RecordSchema);

module.exports = async (req, res) => {
  // CORS設定（フロントエンドのウェブサイトからの通信を許可する設定）
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');   // 全てのウェブサイトからの通信を許可する
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS'); // 許可する通信の種類
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // ブラウザが最初に行う「通信して大丈夫？」という事前確認（OPTIONS）に対する返答
  if (req.method === 'OPTIONS') {
    return res.status(200).end(); // 「大丈夫だよ」とだけ返す
  }

  try {
    await connectToDatabase(); // db.jsを呼び出してデータベースに繋ぐ

    // データの取得処理（GETリクエスト）
    if (req.method === 'GET') {
      // データベースからすべてのデータを検索し、作成日時が新しい順に並び替える
      const records = await Record.find({}).sort({ createdAt: -1 });
      return res.status(200).json(records); // 取得したデータをJSON形式で画面に送る
    }

    // データの保存処理（POSTリクエスト）
    if (req.method === 'POST') {
      // 画面から送られてきたデータをそのままデータベースに保存する
      const newRecord = await Record.create(req.body);
      return res.status(201).json(newRecord); // 保存完了したデータを画面に送る
    }

    // GETでもPOSTでもない通信が来たらエラーにする
    return res.status(405).json({ error: 'Method Not Allowed' });
    
  } catch (error) {
    console.error(error); // エラー内容をVercelのログに記録
    return res.status(500).json({ error: 'Database connection failed' });
  }
};
