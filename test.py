import google.generativeai as genai

genai.configure(api_key="AIzaSyDhhsJ3eEYr-p44xmTs53MmNvfOW-Wv2tA")

print("Listing models...")

for model in genai.list_models():
    print(model.name)