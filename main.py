import streamlit as st

st.header("What's your vibe today?")
vibe = st.radio("Select One", [":tired_face:", ":grimacing:",
                               ":neutral_face:", ":relieved:", ":grinning:"],
                horizontal=True,
                captions=["Overwhelmed", "Anxious", "Balanced", "Peaceful",
                          "Enlightened"])
if vibe:
    st.write(f'You selected {vibe}!')

st.text_area("Additional comments")

button = st.button("Submit")
if button:
    st.info("Your vibe was submitted successfully")
