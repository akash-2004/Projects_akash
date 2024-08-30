import smtplib
import time
import requests
import json
import datetime as dt
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL=os.getenv('MY_EMAIL')
MY_PASSWORD=os.getenv('MY_PASSWORD')
MY_LAT=os.getenv('MY_LAT')
MY_LONG=os.getenv('MY_LONG')

# INTERNATIONAL SPACE STATION!

# LEARN ABOUT STATUS CODES

# print(response.status_code)
# 1XX: Hold on, the process is still happening
# 2XX: Here you go, successfull, you should be getting the data you expected
# 3XX: Go away, you don't have permission to access the data
# 4XX: You screwed up, for example- 404 means the thing you're looking for doesn't exist
# 5XX: The server(the external system) you're requesting from screwed up
# response.raise_for_status()
def lat_lng_vicinity():
    """"Returns True if it's past sunset and ISS's lat and long are near our lat long, otherwise False"""
    response_ISS = requests.get(url="http://api.open-notify.org/iss-now.json")
    data_position = response_ISS.json()["iss_position"]

    longitude = int(float(data_position["longitude"]))
    latitude = int(float(data_position["latitude"]))

    lat_in_vicinity = int(MY_LAT) in range(latitude-5, latitude+5)
    lng_in_vicinity = int(MY_LONG) in range(longitude-5, longitude+5)

    if lat_in_vicinity and lng_in_vicinity:
        print("YEah")
        return True
    return False

def nighttime_or_not():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data_sunrise_sunsets = response.json()["results"]
    sunrise_hour = int(data_sunrise_sunsets["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data_sunrise_sunsets["sunset"].split("T")[1].split(":")[0])
    hour_now = dt.datetime.utcnow().hour

    if hour_now >= sunset_hour or hour_now <= sunrise_hour:
        return True
    return False



while True:
    if lat_lng_vicinity() and nighttime_or_not():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="akashthegamer01@gmail.com",
                            msg="Subject:Look Up!\n\nThe International Space Station should be visible from your location around this time!"
                            )
        connection.close()

        account_sid=os.getenv('account_sid')
        auth_token=os.getenv('auth_token')        
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body="Look Up!\n\nThe International Space Station should be visible from your location around this time!",
            from_=os.getenv('from_'),
            to=os.getenv('to'))
        break
    else:
        time.sleep(20)



