import datetime
import smtplib
import random

random.seed(datetime.datetime.now().timestamp())

my_email = "theprofessionalworkerz@gmail.com"
my_password = "exsuaxrqjtqlfgqo"
recipient_email = "thetheprofessionalworker@yahoo.com"

now = datetime.datetime.now()
day = now.strftime("%A")
# day = now.weekday()
if day == "Saturday" or day == 5:
    with open("quotes.txt", "r") as file:
        quotes_list = file.readlines()
        random_quote = random.choice(quotes_list)
        print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:Motivation Quote For Today!\n\n{random_quote}"
        )
