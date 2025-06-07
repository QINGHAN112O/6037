import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Internship Experience")
    
    st.markdown("""
    ### Comprehensive Operation Intern
    **Beijing Sankuai Network Technology Co., LTD** | *June 2023 - September 2023*
    
    - Conducted research into the culture and tourism industry and carried out benchmarking analysis to facilitate the development of Chinese Culture and Tourism Think Tank; analyzed data through dashboards and wrote reports on the potential attractions of scenery areas.
    - Controlled the density of stores as Points of Interest (POIs ) and Areas of Interest (AOIs) in the high street and marketplace mapping to ensure the digital product informativeness and accuracy in collaboration with business analysts and product managers.
    - Broke down the overall objective of product operation in a quantitative approach and offered development strategies and suggestions on improvement based on thorough data analysis regarding the POI density, Unique Visitor (UV), etc.
    - Formulated the Standard Operating Procedure (SOP) of Meituan monthly marketplace-themed events, designed the feature pages based on collected trending topics, drove engagement by selecting appropriate webinar topics and invited prospective brands to set up market stalls.
    - Responsible for the operation of 10 pilot projects of “Lehuo High Street”, a consumption-driving program initiated by the Chinese government and Meituan, by writing publicity copy, planning marketing events, sorting out the list of participating merchants, and developing, testing, updating and maintaining the Web page for the events.
    """)
    
    st.markdown("""
    ### Industry Research Intern
    **Great Wall Securities** | *February 2023 - May 2023*
    
    - Collected and analyzed statistics regarding macroeconomic development, building materials companies and the overall industry for two independently-completed in-depth company reports and three jointly-formulated in-depth company reports.
    - Independently wrote 12 annual and quarterly report reviews, tracked market dynamics, updated industry daily and weekly reports, and managed the team's official WeChat account.
    """)
    
    st.markdown("""
    ### Intern in Government Affairs, Business Development and Marketing Dept.
    **Knorr-Bremse Systems for Rail Vehicles Enterprise Management (Beijing) Co., Ltd.** | *June 2022 - March 2023*
    
    - Participated in the target corporate government affairs projects, wrote speeches for government-to-enterprise dialogues and economic forums, kept abreast of, analyzed and summarized Chinese policies, completed reports on international topics such as Sino-European and Sino-German relations, supply chain due diligence law, etc., made internal training materials for business practices, extracted key messages from the target company ESG reports, and supervised the subsequent publicity efforts on new media platforms for the government affairs projects
    - Involved in the department's market expansion and business investigation projects, analyzed potential acquisition candidates, and prepared for the establishment of KB China Innovation Center
    """)
    
    st.markdown("---")
    
    st.markdown("## Entrepreneurship Projects")
    
    Projects = [
        {
            "title": "Pocket Museum",
            "description": "The Pocket Museum aimed to provide entertaining and informative educative activities regarding culture, museology, and aesthetics for Beijing-based primary and secondary school students, develop a famous cultural brand by creating immersive experience, and design and organize innovative programs such as orienteering research activities",
            "Responsibility": "Co-authored a business plan of over 46,000 words by organizing an entrepreneurship team of 10 in a commercial project, which was recognized as a prioritized entrepreneurship project of the 'National College Students Innovation and Entrepreneurship Training Program', and was the recipient of a RMB 50,000 sponsorship from UIBE after three rounds of achievement assessment; Formulated the project guiding development strategy and tailored operation tactics based on market analysis, explored methods of capitalizing on trending cultural topics and the fan base, and made HTML5 animations and designed User Interface (UI) for better interactive experience, leading to the successful launch of two original immersive museum-themed script games",
            "outcome": "Approached partners and investors for cooperation, launched 18 products in 15 marketing campaigns, which won rave comments from over 300 clients, of which over 200 became regular customers."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Responsibility:** {', '.join(project['responsibility'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # Add the interactive visualization demo
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Computer Skills
        - **Office:** Word, Excel, PPT, SPSS, MindManager
        - **Creativity:** Photoshop, Premiere, Xiumi
        """)
        
    with col2:
        st.markdown("""
        ### Language Skills
        - **Communication:** Mandarin (Native), English (CET-6: 622; IELTS: 7.5; GRE: 325), French (Basic Conversational Level)
        """)
    
    st.markdown("---") 