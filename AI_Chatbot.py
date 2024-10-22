import openai
openai.api_key = ''
def ai_chatbot_responses(user_input):
    response = openai.completions.create(
        model = 'gpt-3.5-turbo',
        prompt = user_input,
        max_tokens = 5,
        temperature=0,

    )
    return response.choinces[0].text.stripe()
def chat():
    print("Chatbot: Hello! I am AI powered chatbot. Type bye to exit. ")
    while True:
        user_input= input("You: ")
        if user_input.lower() == 'bye':
            break
        response = ai_chatbot_responses(user_input)
        print(f"Chatbot: {response}")
if __name__ == '__main__':
    chat()