const mongoose = require('mongoose');

let cached = global.mongoose;

if (!cached) {
  cached = global.mongoose = { conn: null, promise: null };
}

async function connectToDatabase() {
  // 1. すでに接続が完了している（connがある）なら、それをそのまま使う
  if (cached.conn) return cached.conn;

  // 2. まだ接続していない、かつ接続の「準備（promise）」も始めていない場合
  if (!cached.promise) {
    // 新しくMongoDBへの接続を開始する
    cached.promise = mongoose.connect(process.env.MONGODB_URI, {
      bufferCommands: false, // 接続が完了する前に命令を実行してエラーになるのを防ぐ安全の為の設定
    });
  }

  // 3. 接続が完了するのを待って、確定した接続（conn）を保存する
  cached.conn = await cached.promise;
  
  // つながった接続を呼び出し元（api/index.js）に返す
  return cached.conn;
}

// 他のファイル（api/index.jsなど）から、この関数を呼び出せるようにする
module.exports = connectToDatabase;
