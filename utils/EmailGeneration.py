import google.generativeai as genai

__API_KEY = open("/home/vihaan/keys/GeminiAPIKey.txt").readline(1).strip("\n")

def generateEmail(company):
    prompt = f"Make an email to {company} asking for a sponsorship for FRC team 7414. Make it so i can copy it and send it without needing to edit or substitute anything. DO NOT ADD ANY SUBSTITUTE PLACES SUCH AS '[your name]'. My name is Vihaan. Describe what FRC is. Benefits are having your logo on the robot, recognition on our team social media platforms, and many more. Also add how their company's field is related to FRC. Social media is https://www.instagram.com/perkiomenvalleyrobotics/ and https://www.facebook.com/FRC7414/. For adding links you do not just add the link. Dont use any *s to bold"
    return __callGemini(prompt)

def __callGemini(prompt):
    genai.configure(api_key=__API_KEY)

    model = genai.GenerativeModel(model_name='gemini-1.5-pro')
    response = model.generate_content(prompt)

    return response.text