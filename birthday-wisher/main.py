#!/usr/bin/env python3
import smtplib
import random
import datetime as dt
import pandas


my_email = "Test@gmail.com"     # <-- write your email
my_password = "password"        # <-- write your password
letter_templates_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# compare the current day and the current month with the birthdays of the people in the birthdays.csv file
now = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")

for index, is_birthday_person in data.iterrows():
    if is_birthday_person.day == now.day and is_birthday_person.month == now.month:

        # create the letter tha will send
        recipient_email = is_birthday_person.email
        recipient_name = is_birthday_person["name"]
        with open(f"letter_templates/{random.choice(letter_templates_list)}", "r") as letter_file:
            letter_list = letter_file.readlines()
            letter_list[0] = letter_list[0][0:letter_list[0].index("[")] + recipient_name + ",\n"
        letter = "".join(letter_list)

        # Send letter to that person
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipient_email,
                msg=f"Subject:Happy birthday {recipient_name}!\n\n{letter}"
            )

