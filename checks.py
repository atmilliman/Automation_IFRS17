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

            with urlopen("https://versicherungswirtschaft-heute.de/") as response:
                body = response.read()

            decoded_body = body.decode("utf-8")

            result = re.findall(str_regex, decoded_body)
            result = set(result)

            dict_result = {}
            for count, article in enumerate(result):
                dict_result["Article {}".format(count + 1)] = (
                    " ".join(article.split("-")).upper().strip("/") + "."
                )

            article_string = ""
            for article in dict_result:
                article_string = article_string + "<p>{}</p>".format(
                    dict_result[article]
                )


            html_str = r"""
            <!DOCTYPE html>
            <html>
            <head>
            <style>
            .logo {
                position: relative;
                left: 5px;
                top: -55px;
                text-align:left;
                }    
            .text {
                position: relative;
                right: 5px;
                top: -145px;
                text-align:right;
                font-family:'Open Sans',sans-serif;
                font-size:28px;
                color:grey;
                opacity: 0.85;
                }         
            .article {
                height:80px; 
                background-color:lightgrey;
                margin-left: 25px;
                margin-right: 25px;
                margin-top: 10px;
            }
            .article_text {
                display: inline-block;
                vertical-align: bottom;
                margin-top: 4%;
                }
            </style>
            </head>
            <body style="background-color:grey">
                <div style="height:800px;width:600px;text-align:center;background-color:white">
                    <div style="height:15%">
                        <div class="logo">
                            <img src="C:\Users\Andreas.Thiele\OneDrive - Milliman\Desktop\Project_1\E-Mail-Newsletter\milliman_logo_dark.svg" width="150" height="150"> 
                        </div>    
                        <div class="text">
                            <strong>Nachrichtenübersicht</strong>
                        </div>   
                    </div>
                    <div>
                        <div class="article">
                            <span class="article_text">WIRTSCHAFTSMINISTERIUM BEFREIT 34F VERMITTLER VON ESG ABRAGEPFLICHT</span>
                        </div>
                        <div class="article">
                            <span class="article_text">VERSICHERUNGSPRODUKTE DER WOCHE KW23 2022</span>
                        </div>
                    </div>
                </div>
            </body>
            </html>
            """

            EMAIL_ADDRESS = "andreas.i.thiele.m@gmail.com"
            EMAIL_PASSWORD = "cjupjlrcinjayshh"

            msg = EmailMessage()
            msg["Subject"] = "Artikel vom {}".format(str_date_eu)
            msg["To"] = "andreas.thiele@milliman.com"
            msg.set_content(html_str, subtype="html")

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

        except Exception as e:
            print("Es ist ein Fehler passiert.", e.__class, "Bitte überprüfen!")
		print("Es ist ein Fehler passiert.", e.__class, "Bitte überprüfen!")
            break

    else:
        pass