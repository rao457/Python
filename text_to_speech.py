import speech_recognition as sr
import google.generativeai as genai
import os
API_KEY = 'AIzaSyCLZWr5EvUYl9d4nSc6Pz3c2L90Kyg4mHU'
genai.configure(api_key=API_KEY)
model  = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Write a story about AI and magic")
print(response.text)

