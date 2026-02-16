from langchain.chat_models import init_chat_model
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyB_rB13i6lJ5R7dN1kG3MpsmKSED9ZErFo"

# Correct syntax: use model_provider as keyword argument
model = init_chat_model("gemini-2.5-flash-lite", model_provider="google_genai")

promptA = "Suggest a unique name for a white cat."
promptB = "Give one creative cat name for a white-colored kitten."

responseA = model.invoke(promptA).content
responseB = model.invoke(promptB).content

print(f"Response A: {responseA}")
print()
print(f"Response B: {responseB}")
