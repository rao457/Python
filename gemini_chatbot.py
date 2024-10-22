import google.generativeai as genai

def gemini_chatbot(message):
    API_KEY = "AIzaSyDTca4IoI8Arh_Y9QiEupClaLnGTbxYh_c"
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model.generate_content(message)
def chat():
    while True:
        message = input("You: ")
        if message.lower == 'exit':
            break
        response = gemini_chatbot(message)
        print("ChatBot: ", response.text)
chat()

chat()