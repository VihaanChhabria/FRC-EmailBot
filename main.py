import google.generativeai as genai

APIKey = open("/home/vihaan/keys/GeminiAPIKey.txt").read()[:-1]

genai.configure(api_key=APIKey)

model = genai.GenerativeModel(model_name='gemini-1.5-flash')
response = model.generate_content('What is AI?')

print(response.text)