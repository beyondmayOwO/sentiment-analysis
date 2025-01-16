import requests, os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv('ibm-credentials.env')

API_KEY = os.getenv("NATURAL_LANGUAGE_UNDERSTANDING_APIKEY")
API_URL = os.getenv("NATURAL_LANGUAGE_UNDERSTANDING_URL")

# print(API_KEY)
# print(API_URL)

def sentiment_analyzer(text_to_analyse):
    url = f"{API_URL}/v1/analyze?version=2019-07-12"
    myobj = {
        "text": text_to_analyse,
        "features": {
            "sentiment": {},
            "keywords": {
                "emotion": True
            }
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=myobj, headers=headers, auth=('apikey', API_KEY))

    return response.json()