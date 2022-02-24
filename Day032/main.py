import smtplib
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

my_email = os.getenv('MYMAIL')
reciever_email = os.getenv('RECMAIL')
password = os.getenv('PASSWORD')

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=reciever_email, 
        msg="Subject:Automated mail\n\nBody for the automated mail"
        )
    # connection.close()