import streamlit as st
from forms.contact import contact_form

@st.dialog("Contact Us")
def show_contect_form():
    contact_form()



col1, col2 = st.columns(2,gap="small",vertical_alignment="center")

with col1:
    st.image("StreamLit/assets/Profile picture.png",width=200)

with col2:
    st.title("Shams Shaikh", anchor=False)
    st.write("Machine Learning | LLM  |🌐 Expert WordPress Developer | 🚀 Digital Marketing Manager | 🎯 Help Businesses To Move Forward.")
    if st.button("Contect Me"):
        show_contect_form()
        

st.write("""
# 👋 Welcome to My Portfolio
I'm an aspiring **AI & Machine Learning Developer** with a strong foundation in **Python**, **LLMs**, and **LangChain**. I’m passionate about building intelligent applications that combine smart models with intuitive user experiences—often using tools like **Streamlit** to bring ideas to life in interactive ways.
---
### 💻 Technical Experience
Alongside my journey in AI, I also bring over a year of hands-on experience as a **WordPress Developer**, where I’ve built and managed dynamic, responsive websites tailored to client needs. My ability to blend design, development, and strategy ensures that every site I build is both functional and impactful.
---
### 📈 Digital Marketing Expertise

In addition, I have a solid background as a **Digital Marketer**, specializing in:
- Strategic **social media marketing campaigns**
- Managing brand presence across platforms
- Creating content that drives engagement
---
### 🌟 Why Work With Me?

This unique combination of **technical**, **creative**, and **strategic** skills allows me to approach problems from multiple angles and deliver solutions that not only work—but wow.

I'm always open to collaboration, freelance projects, or innovative ideas.

**Let’s connect and build something intelligent together! 🚀**
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
