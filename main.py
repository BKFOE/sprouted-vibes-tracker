import streamlit as st
import pandas
import send_email as email
import data_collection as dc

st.set_page_config(page_title="Vibes Tracker", page_icon="ed_logo.png")

# Create page header
st.header("What's your :blue[vibe] today?")

# Read the csv file
df = pandas.read_csv("roles.csv")
titles = df["title"]

# Ask user to select their role
user_role = st.selectbox("What is your title?", titles)

# Ask user to submit their vibe for the day, send the email, and write it to
# the csv file
vibe = st.radio("Select one", [":tired_face:", ":grimacing:",
                               ":neutral_face:", ":relieved:", ":grinning:"],
                horizontal=True,
                captions=["Overwhelmed", "Anxious", "Balanced", "Peaceful",
                          "Enlightened"])
if vibe:
    st.write(f'You selected {vibe}!')
    raw_message = st.text_area("Additional comments", max_chars=140)
    message = f"""\
Subject: New vibes submission

From: {user_role}
Vibe selected: {vibe}
Additional comments: {raw_message}
"""
    button = st.button("Submit")
    if button:
        email.send_email(message)
        st.success("Your vibe was submitted successfully!")
        dc.data_collection(user_role, vibe, raw_message)
else:
    st.error("We encountered an error with your submission!")

st.caption("_This is an anonymous way for leaders to understand "
           "how you are experiencing work and to support our "
           "school's continuous improvement plan._")

# st.dataframe(pandas.read_csv("notes.csv", names=["Title", "Vibe",
#                                                  "Note"]), height=300)
