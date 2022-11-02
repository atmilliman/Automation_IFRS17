import re
import smtplib
from datetime import date, datetime
from email.message import EmailMessage
from urllib.request import urlopen

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if (current_time == "10:25:00") and (date.today().weekday() in [0, 1, 2, 3, 4]):
        try:
            str_date = str(date.today())
            str_regex = r"(?<={}/).*?/".format(str_date)

            day = str_date[-2:]
            month = str_date[-5:-3]
            year = str_date[:4]
            str_date_eu = "{}.{}.{}".format(day, month, year)

    else:
        pass