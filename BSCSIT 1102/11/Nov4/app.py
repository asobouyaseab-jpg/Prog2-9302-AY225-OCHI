# app.py
from flask import Flask, request, jsonify
import google.generativeai as genai
import os

# ログを静かにする（エラー対策）
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_CPP_LOG_LEVEL"] = "NONE"
os.environ["ABSL_LOGGING_MIN_LOG_LEVEL"] = "3"

# Flaskアプリ
app = Flask(__name__)

# === Gemini設定 ===
genai.configure(api_key="AIzaSyDAIr0zl69QrbZpCXR19l38G3zwg_wO-yc") 

# モデル初期化（正しいモデル名！）
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="Replies should be in poetry."  
)

# === ルートページ（ブラウザで確認用）===
@app.route('/')
def home():
    return """
    <h1>Gemini Chatbot is Running!</h1>
    <p>Send POST to /chat with {"message": "your question"}</p>/
    """

# === チャットボットエンドポイント ===
@app.route('/chat', methods=['POST'])
def chat():
    return """
    <h1 style="color: #4a90e2; font-family: sans-serif;">Gemini Poetry Bot 起動中！</h1>
    <p style="font-size: 18px;">POSTで <code>/chat</code> に送ってね</p>
    <hr>
    <h3>テスト用コマンド（コピペでOK）</h3>
    <pre style="background:#f4f4f4;padding:15px;">
     curl -X POST http://localhost:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"message":"愛とは何ですか？"}'
    </pre>
    <hr></hr>
    <small>詩でしか答えないちょっと変わったAIです</small>
    """
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        
        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Geminiに質問
        response = model.generate_content(user_message)
        poem = response.text

        return jsonify({"reply": poem})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# === 起動 ===
if __name__ == '__main__':
    print("サーバー起動中... http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)  # ポート5000（80は権限必要）