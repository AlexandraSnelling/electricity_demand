# import streamlit as st

# # function called from app.py homepage when Modeling button selected
# def show_LHL_Demo_Day_Slideshow():
#     # Responsive iframe for Google Slides
#     st.markdown("""
#     <div class="iframe-container">
#         <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRbaUc-_mCv8y5FlWOnOfxNjGEqej_AaXMBgHDYRyQ2A_3AZ2DSxG_1XKzZQqaU8FG9ptALM0ic3KmK/embed?start=false&loop=false&delayms=15000" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
#     </div>
#     """, unsafe_allow_html=True)

import streamlit as st

def show_LHL_Demo_Day_Slideshow():
    # CSS to make iframe responsive and set the background color and text color
    demo_day_style = """
        <style>
            /* Applied to main content area of Streamlit for the LHL Demo Day page */
            .main .block-container {
                background-color: black !important;
                color: white !important; /* Change text color if needed */
            }

            /* Default style for mobile and smaller screens */
            .iframe-container {
                margin-top: 0px; /* No negative margin for mobile by default */
            }

            /* Media query for larger screens - typically desktop */
            @media (min-width: 992px) { /* Adjust this breakpoint as needed */
                .main .block-container {
                    margin-top: -50px; /* Adjust this value for desktop as needed */
                }

                .iframe-container {
                    margin-top: -150px; /* Adjust this value for desktop as needed */
                }
            }

            /* Make iframe responsive */
            .iframe-container {
                position: relative;
                padding-bottom: 75%; /* Aspect ratio */
                height: 0;
                overflow: hidden;
            }
            .iframe-container iframe {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                border: 0;
            }
        </style>
    """
    st.markdown(demo_day_style, unsafe_allow_html=True)

    # Responsive iframe for Google Slides
    st.markdown("""
    <div class="iframe-container">
        <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRbaUc-_mCv8y5FlWOnOfxNjGEqej_AaXMBgHDYRyQ2A_3AZ2DSxG_1XKzZQqaU8FG9ptALM0ic3KmK/embed?start=false&loop=false&delayms=15000" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    </div>
    """, unsafe_allow_html=True)
