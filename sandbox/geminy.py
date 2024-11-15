import google.generativeai as genai
# import os

api_key = ""

prompt = """
Traduis "castor" en serbe. Affiche la réponse et la traduction.
"""

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
print(response.text)
