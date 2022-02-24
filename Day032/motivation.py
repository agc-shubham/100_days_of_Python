import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

my_email = os.getenv('MYMAIL')
reciever_email = os.getenv('RECMAIL')
password = os.getenv('PASSWORD')

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=reciever_email, 
            msg=f"Subject:Monday Motivation\n\n{quote}"
            )