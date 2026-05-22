import google.generativeai as genai

genai.configure(api_key="AIzaSyDhhsJ3eEYr-p44xmTs53MmNvfOW-Wv2tA")

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("Say hello")

print(response.text)