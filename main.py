# IMPORTING LIBRARIES
import requests
import datetime as dt

# CONSTANTS
ISS_API_ENDPOINT = "http://api.open-notify.org/iss-now.json"

# GET REQUEST
response = requests.get(ISS_API_ENDPOINT)
response.raise_for_status()

# JSON DATA
data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

# Current Time
current_datetime = dt.datetime.now()
current_year = current_datetime.year
current_month = current_datetime.month
current_day = current_datetime.day
current_time = current_datetime.time()
current_hour = current_time.hour
current_minute = current_datetime.minute
current_second = current_datetime.second

# PRINT MESSAGE
message = f"The co-ordinates of ISS on {current_year}/{current_month}/{current_day} at {current_hour}:{current_minute}:{current_second} is (latitude={latitude}, longitude={longitude})."
print(message)
