import streamlit as st

# function called from app.py homepage when Modeling button selected
def show_LHL_Demo_Day_Slideshow():
    # Responsive iframe for Google Slides
    st.markdown("""
    <div class="iframe-container">
        <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRbaUc-_mCv8y5FlWOnOfxNjGEqej_AaXMBgHDYRyQ2A_3AZ2DSxG_1XKzZQqaU8FG9ptALM0ic3KmK/embed?start=false&loop=false&delayms=15000" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    </div>
    """, unsafe_allow_html=True)