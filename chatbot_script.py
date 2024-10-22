def chatbot_respose(user_input):
    responses = {
        "hello" : 'Hi, How can I help you?',
        "hi": 'Hello! How can i assist you?',
        "how are you?": 'I am fine and you?',
        "What's your name" : 'I am chatbot, your virtual assistant',
        'bye': 'Bye, Have a good Day!' 
    }
    user_input = user_input.lower()
    if user_input in responses:
        return responses[user_input]
    return "Sorry, I didn't understand. Can you rephrase?"
def chat():
    print("Chatbot: Hello! I'm Chatbot. Type \'bye\' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Bye! Have a good day.")
            break
        response = chatbot_respose(user_input)
        print(f"Chatbot: {response}")
if __name__ == "__main__":
    chat()
