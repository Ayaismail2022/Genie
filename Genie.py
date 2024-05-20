import requests
import json
import sys

# Replace with your actual API key
API_KEY = "AIzaSyApO5YQBCsVCvLAo5Wl55N_h1pWjqSTzWY"

text = " "
if len(sys.argv) > 1:
  text =' Help with any question i ask about linux bash commands only. other wise if my question is off topic please only say : "I only answer bash specific questions " So my questions is' + sys.argv[1]
else:
  exit()

# Define the request body (unchanged)
request_body = {
  "contents": [
    {
      "parts": [
        {
          "text": text
        }
      ]
    }
  ]
}

# Build the URL with your API key (unchanged)
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

# Set headers (unchanged)
headers = {'Content-Type': 'application/json'}

# Send the POST request (unchanged)
response = requests.post(url, headers=headers, json=request_body)

# Check for successful response (unchanged)
if response.status_code == 200:
  # Parse the JSON response (unchanged)
  data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')
  # Access the generated text (unchanged)
  print(data)
else:
  print(f"Error: {response.status_code}")
