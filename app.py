import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

# Set the page layout to wide
st.set_page_config(layout="wide")

# Main content
st.title("My Portfolio Website")
st.subheader("Hey Guys 👋")
st.write("Welcome to my portfolio website! 😊 Here, you can explore my work and learn more about me. Navigate through the sections to discover my projects, educational background, and additional skills.")

st.write("___")

# Navigation menu
with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

    # Content based on the selected menu option
    if selected == 'About':
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.image("me.jpg", width=300)  # Optional: Add a photo
            with col2:
                st.subheader("I am Janicka Marie P. Algonas")
                st.markdown("I am currently an undergraduate student at Cebu Institute of Technology University, pursuing a degree in Information Technology.")
                st.markdown("I have a strong passion for UI/UX design, where I strive to create engaging and intuitive user experiences.")
                st.markdown("Additionally, I am learning to deploy machine learning models using Streamlit. Feel free to explore my projects and get in touch through the contact page!")

            st.write("___")
            # Additional sections for Education and Skills
            with st.container():
                col3, col4 = st.columns(2)
                with col3:
                    st.subheader("Education")
                    st.write("- **Cebu Institute of Technology University**")
                    st.write("  - Accountancy, Business, and Management")
                    st.write("  - Honors: With Honor")
                    st.write("- **Cebu Institute of Technology University**")
                    st.write("  - Junior High School")
                    st.write("  - Honors: With High Honor")
                    st.write("- **Pardo Extension Elementary School**")
                    st.write("  - Elementary School")
                    st.write("  - Honors: Valedictorian")

                with col4:              
                    st.subheader("Additional Skills")
                    st.write("- Proficient in MS Office (Word, Excel, PowerPoint)")
                    st.write("- Work-oriented")
                    st.write("- Ability to work independently and as part of a team")

    if selected == 'Projects':
        with st.container():
            st.header("My Projects")
            st.write("Here are some of the projects I have worked on:")

            # Project 1
            st.subheader("Machine Learning App Development")
            st.write("Developed a machine learning app featuring a traffic sign predictor and a sentence sentiment analyzer using Python and TensorFlow. Collaborated with a team to design and implement the user interface, ensuring an intuitive and smooth user experience. The app's performance was optimized through iterative testing with real-world data, resulting in improved model accuracy.")

            st.write("___")

            # Project 2
            st.subheader("Library System Website Development")
            st.write("Created a comprehensive library management website using Python Django. The system facilitates book searches, reservations, and account management. Focused on delivering a clean and user-friendly front-end design while working on back-end integration to ensure a seamless and functional user experience.")

            st.write("___")

            # Project 3
            st.subheader("Business Prototype Design")
            st.write("Designed a business app prototype based on extensive market research and user needs. Utilized Figma to create interactive prototypes and developed a brochure for presentations. The prototype aimed to address specific business requirements and improve user engagement through effective design solutions.")

    if selected == 'Contact':
        with st.container():
            st.header("Contact Me")
            st.write("Feel free to reach out to me via the following channels:")
            st.write("- **Email:** janickamariealgonas@gmail.com")
            st.write("- **GitHub:** [Janicka Marie P. Algonas](https://github.com/janickaalgonas)")
