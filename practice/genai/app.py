import google.generativeai as genai

try:
 genai.configure(api_key="AIzaSyCHwCpVOvHQlIUQIB-m-CvOf46MHpO3PbY")
 model = genai.GenerativeModel("gemini-1.5-flash")
 response = model.generate_content("Explain how AI works")
 print(response.text)

except Exception as e:
 print(f"An error occurred: {e}")