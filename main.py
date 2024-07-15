import google.generativeai as genai

APIKEY = open("/home/vihaan/keys/GeminiAPIKey.txt").read()[:-1]

def generateEmail(company):
    def callGemini(content):
        genai.configure(api_key=APIKEY)

        model = genai.GenerativeModel(model_name='gemini-1.5-flash')
        response = model.generate_content(content)

        return response.text
    content = f"Make an email to {company} asking for a sponsorship for FRC team 7414. My name is Vihaan. Describe what FRC is. Benefits are having your logo on the robot, recognition on our team social media platforms, and many more. Also add how their company's field is related to FRC. Dont add any 'insert here' things. Social media is https://www.instagram.com/perkiomenvalleyrobotics/ and https://www.facebook.com/FRC7414/. For adding links you do not just add the link. JUST RETURN THE EMAIL."

    return callGemini(content)

print(generateEmail("JBT"))