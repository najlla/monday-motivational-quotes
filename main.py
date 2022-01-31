import random
import datetime as dt
import smtplib

with open("quotes.txt", mode="r") as quote_file:
    motivational_quotes = quote_file.readlines()
    monday_quote = random.choice(motivational_quotes)

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    my_email = "najlla.meraj@gmail.com"
    password = "Najllameraj1996$"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="angel.rahim@yahoo.com",
                            msg=f"Subject: Monday Motivation \n \n{monday_quote}")



