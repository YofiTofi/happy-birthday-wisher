import datetime as dt
import random
import smtplib
import pandas

EMAIL = ""
PASSWORD = ""

bday_df = pandas.read_csv("birthdays.csv")
bday_list = bday_df.to_dict(orient="records")
born_today = []

now = dt.datetime.now()
day = now.day
month = now.month

for person in bday_list:
    if person["month"] == month and person["day"] == day:
        letter_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_number}.txt", "r") as template:
            letter = template.read()
        letter = letter.replace("[NAME]", person["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=person["email"], msg=f"Subject:Happy Birthday!\n\n{letter}")
