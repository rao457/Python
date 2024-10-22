import google.generativeai as genai

# Set your API key
API_KEY = "AIzaSyDTca4IoI8Arh_Y9QiEupClaLnGTbxYh_c"

# Configure the generative AI client with the API key
genai.configure(api_key=API_KEY)

# Initialize the model with the correct identifier
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate content using the model
response = model.generate_content("What is meaning of name of Zenub")

# Print the generated content
print(response.text)
