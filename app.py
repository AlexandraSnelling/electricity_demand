import streamlit as st
from Toronto_2024_Electricity_Demand_Forecast import show_Toronto_2024_Electricity_Demand_Forecast
from Toronto_2023_Electricity_Demand_Modeling import show_Toronto_2023_Electricity_Demand_Modeling

# Set page config
st.set_page_config(layout="wide", page_title="Electricity Demand Forecast")

# Custom CSS to inject contained in a string
custom_css = """
    <style>
        .css-18e3th9 {
            background-color: black;
            color: white;
        }
        .css-1d391kg {
            background-color: black;
            color: white;
        }
        .stButton>button {
            width: 100%;
            border-radius: 0px;
            margin: 3px 0px;
            background-color: #000000;
            color: #ffffff;
        }
        .stButton>button:hover {
            background-color: #ffffff;
            color: #000000;
            border: 1px solid #000000;
        }
    </style>
"""

# Inject custom CSS with Markdown
st.markdown(custom_css, unsafe_allow_html=True)

# Page selection using buttons
def render_page(page_name):
    st.title(f"This is your {page_name.lower()} page.")

# Define buttons for navigation
if st.sidebar.button("Home"):
    render_page("Home")
if st.sidebar.button("Forecast"):
    render_page("Forecast")
if st.sidebar.button("Modeling"):
    render_page("Modeling")

# # Page selection
# page = st.sidebar.radio("Navigate", ["Home", "Forecast", "Modeling"])

if page == "Home":
    st.title("This is your home page.")
    # Use st.markdown to embed the Google Slides iframe
    st.markdown("""
    <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRbaUc-_mCv8y5FlWOnOfxNjGEqej_AaXMBgHDYRyQ2A_3AZ2DSxG_1XKzZQqaU8FG9ptALM0ic3KmK/embed?start=false&loop=false&delayms=15000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    """, unsafe_allow_html=True)
elif page == "Forecast":
    show_Toronto_2024_Electricity_Demand_Forecast()
elif page == "Modeling":
    show_Toronto_2023_Electricity_Demand_Modeling()




# import streamlit as st
# from Toronto_2024_Electricity_Demand_Forecast import show_Toronto_2024_Electricity_Demand_Forecast
# from Toronto_2023_Electricity_Demand_Modeling import show_Toronto_2023_Electricity_Demand_Modeling

# # Set the page config here, as the very first Streamlit call
# st.set_page_config(layout="wide", page_title="Electricity Demand Forecast")

# # Custom CSS to inject into the Streamlit page
# st.markdown(
#     """
#     <style>
#     /* This creates a black sidebar with white text */
#     .css-1d391kg {
#         background-color: #000000;
#         color: #ffffff;
#     }
#     /* This changes the color of the text and the buttons in the sidebar */
#     .css-hi6a2p {
#         color: #ffffff;
#     }
#     .st-ae {
#         color: #ffffff;
#     }
#     .st-ae:hover {
#         color: #ffffff;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Page selection
# page = st.sidebar.radio("Navigate", ["Home", "Forecast", "Modeling"])

# if page == "Home":
#     st.title("This is your home page.")
#     # Use st.markdown to embed the Google Slides iframe
#     st.markdown("""
#     <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vRbaUc-_mCv8y5FlWOnOfxNjGEqej_AaXMBgHDYRyQ2A_3AZ2DSxG_1XKzZQqaU8FG9ptALM0ic3KmK/embed?start=false&loop=false&delayms=15000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
#     """, unsafe_allow_html=True)
# elif page == "Forecast":
#     show_Toronto_2024_Electricity_Demand_Forecast()
# elif page == "Modeling":
#     show_Toronto_2023_Electricity_Demand_Modeling()


# import streamlit as st
# from streamlit.components.v1 import components  # Add this line to import components
# from Toronto_2024_Electricity_Demand_Forecast import show_Toronto_2024_Electricity_Demand_Forecast
# from Toronto_2023_Electricity_Demand_Modeling import show_Toronto_2023_Electricity_Demand_Modeling

# # Set the page config here, as the very first Streamlit call
# st.set_page_config(layout="wide", page_title="Electricity Demand Forecast")

# # Page selection
# page = st.sidebar.selectbox("Choose a page", ["Home", "Forecast", "Modeling"])

# if page == "Home":
#     st.title("This is your home page.")
#     # Place the components.iframe call inside the condition where you want it to appear
#     components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRbaUc-_mCv8y5FlWOnOfxNjGEqej_AaXMBgHDYRyQ2A_3AZ2DSxG_1XKzZQqaU8FG9ptALM0ic3KmK/embed?start=true&loop=true&delayms=3000", height=569)
# elif page == "Forecast":
#     show_Toronto_2024_Electricity_Demand_Forecast()
# elif page == "Modeling":
#     show_Toronto_2023_Electricity_Demand_Modeling()

    
# import streamlit as st
# from Toronto_2024_Electricity_Demand_Forecast import show_Toronto_2024_Electricity_Demand_Forecast
# from Toronto_2023_Electricity_Demand_Modeling import show_Toronto_2023_Electricity_Demand_Modeling

# # Set the page config here, as the very first Streamlit call
# st.set_page_config(layout="wide", page_title="Electricity Demand Forecast")

# # Page selection
# page = st.sidebar.selectbox("Choose a page", ["Home", "Forecast", "Modeling"])

# if page == "Home":
#     st.title("This is your home page.")
# elif page == "Forecast":
#     show_Toronto_2024_Electricity_Demand_Forecast()
# elif page == "Modeling":
#     show_Toronto_2023_Electricity_Demand_Modeling()
    
# components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRbaUc-_mCv8y5FlWOnOfxNjGEqej_AaXMBgHDYRyQ2A_3AZ2DSxG_1XKzZQqaU8FG9ptALM0ic3KmK/embed?start=true&loop=true&delayms=3000", height=569)
