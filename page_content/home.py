import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Qinghan Chen</h4>
        <p>Recent Bachelor's Graduate in Economics<br>
        Chinese University of Hong Kong<br>
        <a href="mailto:zhaozhaochen2001@163.com">zhaozhaochen2001@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    # 使用绝对路径加载图片
    image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                             "static", "images", "image.jpg")
    
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning(f"找不到图片文件: {image_path}")
    
    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I graduated from the University of International Business and Economics with a major in International Economics and Trade. I have excellent academic performance and outstanding English proficiency, achieving an IELTS score of 7.5 and passing the TEM-8 (Test for English Majors - Band 8) with distinction.

        During my undergraduate studies, I actively participated in various academic, business, and entrepreneurship competitions. A cultural and educational entrepreneurship project I led as an undergraduate was selected as a national key-supported entrepreneurship project. I have also interned in the industry research department of a securities firm, at Meituan, and in the marketing department of a foreign enterprise. 

        Currently, I am pursuing a master's degree in Marketing at the Business School of The Chinese University of Hong Kong, focusing on big data-related marketing courses in the Hong Kong market.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Office: Word, Excel, PPT, SPSS, MindManager
        - Creativity: Photoshop, Premiere, Xiumi
        - Language: Mandarin (Native), English (CET-6: 622; IELTS: 7.5; GRE: 325), French (Basic Conversational Level)
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page