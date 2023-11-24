import requests
from datetime import datetime
import os

# DETAILS
GENDER = "male"
AGE = 20
HEIGHT = 172.7
WEIGHT = 66
TODAY = datetime.now().strftime("%d/%m/%Y")
TIME = datetime.now().strftime('%X')


# NUTRITIONIX API
APP_ID = os.environ.get("API_ID")
APP_KEY = os.environ.get("API_KEY")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

# SHEETY API
Sheety_API_ENDPOINT = "https://api.sheety.co/daee2bd4fbe4d80a33353bf438c3fb55/myWorkouts/workouts"


query = input("What exercises did you do today? ")
BODY = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=API_ENDPOINT, headers=HEADERS, json=BODY)
workout_details = response.json()

Sheety_HEADERS = {
    "Authorization": "Bearer boy1home$drst0ne1091j0ke&91"
}

for v in workout_details['exercises']:
    Sheety_BODY = {
        "workout": {
            "date": TODAY,
            "time": TIME,
            "exercise": v['name'].title(),
            "duration": v['duration_min'],
            "calories": v["nf_calories"]
        }
    }

    sheety_response = requests.post(url=Sheety_API_ENDPOINT, json=Sheety_BODY, headers=Sheety_HEADERS)
    print(sheety_response.text)
