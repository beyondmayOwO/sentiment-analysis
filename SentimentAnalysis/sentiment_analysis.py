import requests, os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv('ibm-credentials.env')

API_KEY = os.getenv("NATURAL_LANGUAGE_UNDERSTANDING_APIKEY")
API_URL = os.getenv("NATURAL_LANGUAGE_UNDERSTANDING_URL")

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
    header = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=myobj, headers=header, auth=('apikey', API_KEY))

    dict_response = response.json()

    # Initialize the score and label
    score = None
    label = None

    # Extract score and label and handle the error
    if response.status_code == 200:
        score = dict_response['sentiment']['document']['score']
        label = dict_response['sentiment']['document']['label']
    elif response.status_code == 500:
        score = None
        label = None

    return {"Score": score, "Label": label}