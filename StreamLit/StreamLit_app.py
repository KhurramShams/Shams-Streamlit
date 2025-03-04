import streamlit as st

# --------- Page SetUp ------------#
AboutPage=st.Page(
    page="views/about_me.py",
    title= "About Me",
    icon = ":material/account_circle:",
    default= True
)

ChatBot=st.Page(
    page="views/chat_bot.py",
    title="Chat-Bot",
    icon=":material/smart_toy:",
)

Clients = st.Page(
    page="views/clients.py",
    title="Clients",
    icon=":material/account_circle:"
)

#--------- Navigation Menu --------#

Appmenu = st.navigation(pages=[AboutPage,Clients,ChatBot])

Appmenu.run()

#-------- Header Footer -----------#

st.logo("assets/logo.png")
st.sidebar.text("Develop with ❤ By Shams")