##################### Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter
# templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import random
import datetime as dt
import pandas
now = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
my_email = ""
my_password = ""
letter_templates_list = ["letter_1.txt", "letter_2.txt","letter_3.txt"]
print(data)
for index, is_birthday_person in data.iterrows():
    if is_birthday_person.day == now.day and is_birthday_person.month == now.month:
        recipe = is_birthday_person.email
        # with open(random.choice(letter_templates_list), "r") as letter_file:
        #     letter_file.readlines()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=recipe,
                msg="Subject:Happy birthday!\n\n{}"
            )













