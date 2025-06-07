import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Qinghan_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Qinghan Chen")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** zhaozhaochen2001@163.com
    - **Phone:** +852 55347874
    """)

    st.header("Internship Experience")
    st.markdown("""
    **Comprehensive Operation Intern, Beijing Sankuai Network Technology Co., LTD**
    - *June 2023 - September 2023*
    - Conducted research into the culture and tourism industry and carried out benchmarking analysis to facilitate the development of China Culture and Tourism Think Tank; analyzed data through dashboards and wrote reports on the potential attractions of scenery areas.
    - Controlled the density of stores as Points of Interest (POIs ) and Areas of Interest (AOIs) in the high street and marketplace mapping to ensure the digital product informativeness and accuracy in collaboration with business analysts and product managers
    - Broke down the overall objective of product operation in a quantitative approach and offered development strategies and suggestions on improvement based on thorough data analysis regarding the POI density, Unique Visitor (UV), etc.
    - Formulated the Standard Operating Procedure (SOP) of Meituan monthly marketplace-themed events, designed the feature pages based on collected trending topics, drove engagement by selecting appropriate webinar topics and invited prospective brands to set up market stalls.
    - Responsible for the operation of 10 pilot projects of “Lehuo High Street”, a consumption-driving program initiated by the Chinese government and Meituan, by writing publicity copy, planning marketing events, sorting out the list of participating merchants, and developing, testing, updating and maintaining the Web page for the events.

    **Industry Research Intern, Great Wall Securities**
    - *February 2023 - May 2023*
    - Collected and analyzed statistics regarding macroeconomic development, building materials companies and the overall industry for two independently-completed in-depth company reports and three jointly-formulated in-depth company reports.
    - Independently wrote 12 annual and quarterly report reviews, tracked market dynamics, updated industry daily and weekly reports, and managed the team's official WeChat account.
    """)

    st.header("Education")
    st.markdown("""
    **Bachelor of Economics in International Economics and Trade**
    - University of International Business and Economics
    - *Graduated: June 2024*
    - GPA: 3.7/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, R
    - **Office:** Word, Excel, PPT, SPSS, MindManager
    - **Creativity:** Photoshop, Premiere, Xiumi
    """)

    st.header("Languages")
    st.markdown("""
    - **Mandarin:** Native
    - **English:** CET-6: 622; IELTS: 7.5; GRE: 325
    - **French:** Basic Conversational Level
    """)

    st.header("Interests")
    st.markdown("""
    - Arts & Museum
    - Hiking and outdoor activities
    """)

    st.markdown("---") 