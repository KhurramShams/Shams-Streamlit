import streamlit as st


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Enter Name")
        email = st.text_input("Enter Email")
        message = st.text_area("Enter Message")
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            if not name:
                st.error("Enter Your Name")
                st.stop()
            if not email:
                st.error("Enter Your Email")
                st.stop()
            if not message:
                st.error("Enter Your Message")
                st.stop()
            else:
                st.success("Message Done")