import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "tirrell@usprouted.com"
    password = os.getenv("PASSWORD")
    receiver = "tirrell@usprouted.com"
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
            print("Email sent successfully")
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the email: {e}")