import streamlit as st

st.title("Chat Bot")

st.text_input("Text Input")
button = st.button("Get Response")
if button:
    st.error("Network Error")
    st.stop()