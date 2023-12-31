import smtplib, ssl
import os
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = st.secrets["db_username"]
    password = st.secrets["db_password"]
    receiver = st.secrets["db_username"]
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
            print("Email sent successfully")
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the email: {e}")