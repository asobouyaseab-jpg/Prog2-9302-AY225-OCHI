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
    system_instruction="""
You are an expert assistant for the Integrated Programming and Technology (IPT) assignment.

You may ONLY answer questions that clearly relate to IPT and match the meaning of one of these 20 topics (even with different wording):

[Allowed English Topics]
1. What is Integrated Programming and Technology?
2. What are the main components of IPT?
3. How does IPT differ from traditional programming?
4. What are the benefits of using IPT in modern development?
5. Give an example of IPT in real-world applications.
6. What tools or frameworks are commonly used in IPT?
7. How does hardware-software integration work in IPT?
8. What is the role of APIs in Integrated Programming and Tech?
9. Explain the concept of full-stack development in IPT context.
10. Why is IPT important for future technology?

[Allowed Japanese Topics]
1. IPT（統合プログラミング技術）とは何ですか？
2. IPTの主な構成要素は何ですか？
3. IPTは従来のプログラミング言語とどう違いますか？
4. 現代の開発においてIPTを使用するメリットは何ですか？
5. 実際のアプリケーションにおけるIPTの適用例を挙げてください。
6. IPTで一般的に使用されるツールやフレームワークは何ですか？
7. IPTにおけるハードウェアとソフトウェアの統合はどのように機能しますか？
8. IPTにおけるAPIの役割は何ですか？
9. IPTにおけるフルスタック開発の概念を説明してください。
10. IPTは将来のテクノロジーにとってなぜ重要ですか？

[CRITICAL RULES - MUST FOLLOW EXACTLY]
- If the user's question is in Japanese → Answer in Japanese only.
- If the user's question is in English → Answer in English only.
- Answer in clear, professional, and detailed language.
- Respond within 2 minutes.
- For ANY question that does NOT clearly match one of the 20 IPT topics above:
   → If question is in Japanese: Reply exactly "申し訳ありませんが、IPT（統合プログラミング技術）に関する質問のみ対応しています。"
   → If question is in English: Reply exactly "Sorry, I can only answer questions related to Integrated Programming and Technology (IPT)."
- Never answer off-topic questions (love, weather, jokes, other subjects, etc.).
"""
)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>IPT Assistant - Integrated Programming and Technology</title>
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
        <h1>IPT Chatbot</h1>
        <div class="chat">
            <p style="text-align:center;color:#666;">I can answer questions in both Japanese and English, but I will only answer specific questions.</p>
            <input type="text" id="msg" placeholder="例: What is IPT? / IPTとは何ですか？" onkeypress="if(event.key==='Enter')send()">
            <button onclick="send()">Ask</button>
            <div id="result" class="response"></div>
        </div>

        <script>
            async function send() {
                const input = document.getElementById('msg');
                const result = document.getElementById('result');
                const message = input.value.trim();
                if (!message) return;

                result.innerHTML = "Preparing a detailed answer...";

                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: message})
                });

            const data = await response.json();
                if (data.reply) {
                    result.innerHTML = data.reply.replace(/\\n/g, '<br>');
                } else {
                    result.innerHTML = "<span style='color:red;'>Error: " + data.error + "</span>";
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
            return jsonify({"error": "Please enter a question"}), 400

        response = model.generate_content(user_message)
        answer = response.text.strip()
        return jsonify({"reply": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("IPT Assistant起動中 → http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)