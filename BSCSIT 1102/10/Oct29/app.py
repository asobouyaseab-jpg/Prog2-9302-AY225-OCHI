# Step 1: Install the Gemini library (run this once in terminal)
# pip install google-generativeai

import os
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GRPC_CPP_LOG_LEVEL"] = "NONE"
os.environ["ABSL_LOGGING_MIN_LOG_LEVEL"] = "3"

# Step 2: Python code
import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDAIr0zl69QrbZpCXR19l38G3zwg_wO-yc")

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="Replies should be in poetry"
)

# Generate content
response = model.generate_content("What is Integrated Programing and Tech?")

# Print the model's response
print(response.text)