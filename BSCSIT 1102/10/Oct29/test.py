# test.py
import google.generativeai as genai

# ここに自分のAPIキーを入れる
API_KEY = "AIzaSyDAIr0zl69QrbZpCXR19l38G3zwg_wO-yc"  # ← ここを置き換え

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Hello")
print(response.text)