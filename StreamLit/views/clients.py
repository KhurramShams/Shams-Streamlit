import streamlit as st

st.title("Clients", anchor=False )
st.text("")

col1,col2,col3 = st.columns(3,gap="small",vertical_alignment="top")

with col1:
    st.markdown("**Fly Easy Travel and Tours Pvt Ltd**") 
    st.image("assets/Flyeasy.png",width=150)
    
with col2:
    st.markdown("**Mirpurkhas Testing Service**") 
    st.image("assets/MTS.png",width=80)
   
   
with col3:
    st.markdown("**Regal Elite (E-Commerce)**") 
    st.image("assets/RegalElite.png",width=80)
    st.write("")

col4,col5,col6 = st.columns(3,gap="small",vertical_alignment="top")

with col4:
    st.markdown("**Margalla Trail Runners**") 
    st.image("assets/logo.png",width=150)
    
with col5:
    st.markdown("**Sky Trips Travel and Tours**") 
    st.image("assets/SkyTrips.png",width=150)
    
with col6:
    st.markdown("**Mirpurkhas Mangoes**")
    st.image("assets/MM.png",width=100)
    