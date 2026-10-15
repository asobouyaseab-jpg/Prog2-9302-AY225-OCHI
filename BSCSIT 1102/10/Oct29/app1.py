import os
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_CPP_LOG_LEVEL"] = "NONE"
os.environ["ABSL_LOGGING_MIN_LOG_LEVEL"] = "3"

import google.generativeai as genai

# APIキーはここだけで設定（一度だけ）
genai.configure(api_key="AIzaSyDAIr0zl69QrbZpCXR19l38G3zwg_wO-yc")

# 正しい書き方：api_keyは書かず、model_nameに正しい名前を入れる
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",                 # ← 正しいモデル名（綴り注意！）
    system_instruction="Replies should be in poetry"
)

# 質問してみる
response = model.generate_content("What is Integrated Programming and Tech?")

# 結果を表示（詩で返ってきます）
print(response.text)