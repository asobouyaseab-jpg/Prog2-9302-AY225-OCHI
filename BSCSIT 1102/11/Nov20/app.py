# app.py
from flask import Flask, request, jsonify
import google.generativeai as genai
import os

os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_CPP_LOG_LEVEL"] = "NONE"
os.environ["ABSL_LOGGING_MIN_LOG_LEVEL"] = "3"

app = Flask(__name__)

genai.configure(api_key="AIzaSyDAIr0zl69QrbZpCXR19l38G3zwg_wO-yc")

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="Replies should be in poetry."
)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>Gemini 詩人ボット</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; padding: 40px; }
            h1 { color: #4a90e2; text-align: center; }
            .chat { max-width: 700px; margin: 0 auto; background: white; border-radius: 15px; padding: 20px; box-shadow: 0 5px 20px rgba(0,0,0,0.1); }
            input, button { padding: 12px; font-size: 16px; }
            input { width: 70%; border: 1px solid #ddd; border-radius: 8px; }
            button { width: 25%; background: #4a90e2; color: white; border: none; border-radius: 8px; cursor: pointer; }
            .response { margin-top: 20px; padding: 20px; background: #f9f9f9; border-radius: 10px; white-space: pre-wrap; font-size: 18px; line-height: 1.8; }
        </style>
    </head>
    <body>
        <h1>Gemini 詩人ボット</h1>
        <div class="chat">
            <p style="text-align:center;color:#666;">何でも聞いてみてね。答えは必ず詩で返します</p>
            <input type="text" id="msg" placeholder="例：愛って何？ / 今日の運勢は？ / 死ぬってどういうこと？" onkeypress="if(event.key==='Enter')send()">
            <button onclick="send()">詩で答えて</button>
            <div id="result" class="response"></div>
        </div>

        <script>
            async function send() {
                const input = document.getElementById('msg');
                const result = document.getElementById('result');
                const message = input.value.trim();
                if (!message) return;

                result.innerHTML = "詩を紡いでいます...";

                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: message})
                });

                const data = await response.json();
                if (data.reply) {
                    result.innerHTML = "<strong>詩：</strong><br>" + data.reply.replace(/\\n/g, '<br>');
                } else {
                    result.innerHTML = "エラー: " + data.error;
                }
                input.value = "";
            }
        </script>
    </body>
    </html>
    """

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        if not user_message:
            return jsonify({"error": "メッセージが空です"}), 400

        response = model.generate_content(user_message)
        poem = response.text.strip()
        return jsonify({"reply": poem})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("詩人ボット起動中 → http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)