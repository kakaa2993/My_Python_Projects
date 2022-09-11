import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "test@gmail.com"  # put your email
MY_PASSWORD = ""             # put your password
SMTP = "smtp.gmail.com"      # this is for Google gmail email only
MY_LAT = 0   # put Your latitude
MY_LONG = 0  # put Your longitude


def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        return True


def is_it_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if sunset < time_now > sunrise:
        return True


while True:
    if is_it_night() and is_above():
        with smtplib.SMTP(SMTP) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:LOOK UP!\n\nThe iss is near to you"
            )
    time.sleep(60)
