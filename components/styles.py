import streamlit as st
import os

def load_css():
    """Load custom CSS from the static/css directory"""
    # 使用绝对路径
    css_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                           "static", "css", "style.css")
    
    # Check if the file exists
    if os.path.exists(css_file):
        with open(css_file, "r") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file not found: {css_file}")
        
def apply_custom_css():
    """Apply custom CSS styles directly"""
    st.markdown("""
    <style>
    @import url('static/css/style.css');
    </style>
    """, unsafe_allow_html=True)