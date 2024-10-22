import requests

# Define the URL of the API you want to use
api_url = "https://api.example.com/data"

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()
    
    # Now you can work with the data
    # For example, print the data
    print(data)
else:
    # If the request was not successful, print the error code
    print("Error:", response.status_code)

