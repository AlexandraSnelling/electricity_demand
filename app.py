import streamlit as st
from streamlit.components.v1 import components  # Add this line to import components
from LHL_Demo_Day_Slideshow import show_LHL_Demo_Day_Slideshow
from Toronto_2024_Electricity_Demand_Forecast import show_Toronto_2024_Electricity_Demand_Forecast
from Toronto_2023_Electricity_Demand_Modeling import show_Toronto_2023_Electricity_Demand_Modeling

# Set the page config here, as the very first Streamlit call
st.set_page_config(layout="wide", page_title="Electricity Demand Forecast", initial_sidebar_state="expanded")

# Using session state to store the current page
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'Home'

# Define the navigation function
def navigate(page):
    st.session_state['current_page'] = page

# Custom CSS to style the sidebar buttons and background
custom_css = """
    <style>
        /* Change the color of the top bar */
        [data-testid="stHeader"] {
            background-color: #000000 !important;
        }
        
        /* Change the color of the text in the toolbar to white */
        [data-testid="stToolbarActions"] button,
        [data-testid="stToolbarActions"] svg,
        [data-testid="stActionButtonLabel"] {
            color: white !important;
            fill: white !important;
        }

        /* Change the color of the text and icons inside the action buttons to white */
        [data-testid="stActionButton"] button,
        [data-testid="stActionButton"] svg,
        [data-testid="stActionButtonIcon"] svg {
            color: white !important;
            fill: white !important;
        }

        /* Change color of dropdown menu icon */
        [data-testid="stMainMenu"] button,
        [data-testid="stMainMenu"] svg {
            color: white !important;
            fill: white !important;
        }

        /* Additional styling to ensure SVG icons are white */
        [data-testid="baseButton-header"] svg,
        [data-testid="stActionButtonIcon"] {
            color: white !important;
            fill: white !important;
        }
        
        /* Main sidebar style */
        [data-testid="stSidebarContent"] {
            background-color: #000000 !important;
        }

        /* Style the buttons to look more like tabs */
        .stButton > button {
            display: block;
            width: 100%;
            padding: 10px;
            text-align: left;
            border: none;
            border-radius: 0;
            margin: 0;
            color: white;
            background-color: #000000;
            font-size: 16px;
        }
        .stButton > button:hover {
            background-color: #555555;
        }
        .stButton > button:focus {
            outline: none;
            box-shadow: none;
        }
    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# # Sidebar navigation
# st.sidebar.button("🏠 Home", on_click=navigate, args=('Home',))
# st.sidebar.button("🔮 Forecast", on_click=navigate, args=('Forecast',))
# st.sidebar.button("📊 Modeling", on_click=navigate, args=('Modeling',))

# Sidebar navigation
st.sidebar.button("Home", on_click=navigate, args=('Home',))
st.sidebar.button("LHL Demo Day", on_click=navigate, args=('LHL Demo Day',))
st.sidebar.button("Forecast", on_click=navigate, args=('Forecast',))
st.sidebar.button("Modeling", on_click=navigate, args=('Modeling',))

# Page display logic
# Page display logic
if st.session_state['current_page'] == 'Home':
    # Only apply this style on the home page
    home_style = """
        <style>
            /* Applied to main content area of Streamlit for the homepage */
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
    st.markdown(home_style, unsafe_allow_html=True)

    # Remove st.title if you're not using it
    # st.title("This is your home page.")

    # # Responsive iframe for Google Slides
    # st.markdown("""
    # <div class="iframe-container">
    #     <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRbaUc-_mCv8y5FlWOnOfxNjGEqej_AaXMBgHDYRyQ2A_3AZ2DSxG_1XKzZQqaU8FG9ptALM0ic3KmK/embed?start=false&loop=false&delayms=15000" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    # </div>
    # """, unsafe_allow_html=True)
    
    # Responsive iframe for YouTube Video
    st.markdown("""
    <div class="iframe-container">
        <iframe src="https://www.youtube.com/embed/fEx-GFKU_qk" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    </div>
    """, unsafe_allow_html=True)


elif st.session_state['current_page'] == 'LHL Demo Day':
    show_LHL_Demo_Day_Slideshow()  # function that shows the demo day page
elif st.session_state['current_page'] == 'Forecast':
    show_Toronto_2024_Electricity_Demand_Forecast()  # function that shows the forecast page
elif st.session_state['current_page'] == 'Modeling':
    show_Toronto_2023_Electricity_Demand_Modeling()  # function that shows the modeling page