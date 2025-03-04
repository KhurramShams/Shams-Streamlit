import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact Us")
def show_contect_form():
    contact_form()



col1, col2 = st.columns(2,gap="small",vertical_alignment="center")

with col1:
    st.image("assets/Profile picture.png",width=200)

with col2:
    st.title("Shams Shaikh", anchor=False)
    st.write("🌐 Expert WordPress Developer | 🚀 Digital Marketing Manager | 🎯 Help Businesses To Move Forward.")
    if st.button("Contect Me"):
        show_contect_form()
        

st.write("""As a skilled WordPress Developer with over one year of hands-on experience. I excel in developing dynamic, user-friendly websites, backed by strong communication skills and a solid educational and professional background. I strive to deliver impactful digital solutions while maintaining a high standard of professionalism.
Additionally, I am a dedicated Digital Marketer with extensive experience in setting up social media marketing campaigns, managing social media accounts, and creating engaging posts. My technical skills enable me to effectively interact with a diverse range of clients. I am always eager to embrace new challenges to grow and refine my skills further.
""")        


col3,col4 = st.columns(2,gap="small",vertical_alignment="center")

with col3:
    st.title("Education")
    st.markdown("**HSC | SAL Degree Science Collage Mirpurhas**")
    st.text("-Actively participated in academic and co-curricular activities, enhancing teamwork and communication abilities.")
    st.markdown("**Computer Science | Sukkur IBA University**")
    st.text("""-BS Degree in Process
    -Worked on multiple academic projects, including web and mobile applications, showcasing strong technical and collaborative skills.""")

    
with col4:
    st.title("Experience")
    st.markdown("**WordPress Developer | Freelancing**")
    st.text("""-Collaborated with local and international clients, including Fly Easy, Sky Trips, and Margalla Trail Runners, Mirpurkhas Mangoes, to create tailored web solutions.
-Worked with over 15+ small scale web based projects and 1+ large-scale web applications. """)
    st.markdown("**Web Developer and Media Accounts Manager | Softech Source**")
    st.text("""-Managed the company website, ensuring up-to-date content and seamless functionality.
-Handled social media accounts, creating and scheduling weekly posts to engage the target audience.
-Responded promptly to client inquiries, providing detailed information about the company's services.""")
