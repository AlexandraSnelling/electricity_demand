import streamlit as st
from streamlit.components.v1 import components  # Add this line to import components
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

# Custom CSS to style the sidebar buttons
custom_css = """
    <style>
        .sidebar .sidebar-content {
            background-color: #2e2e2e;
        }
        .css-1aumxhk {
            background-color: #2e2e2e;
            color: white;
            padding: 10px;
        }
        .stButton>button {
            display: block;
            width: 100%;
            border: none;
            border-radius: 0;
            margin: 0;
            padding: 10px;
            text-align: left;
            color: white;
            background-color: #2e2e2e;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #444;
        }
        .stButton>button:focus {
            outline: none;
            box-shadow: none;
        }
        .stButton>button:active {
            background-color: #666;
        }
    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.button("🏠 Home", on_click=navigate, args=('Home',))
st.sidebar.button("🔮 Forecast", on_click=navigate, args=('Forecast',))
st.sidebar.button("📊 Modeling", on_click=navigate, args=('Modeling',))

# Page display logic
if st.session_state['current_page'] == 'Home':
    st.title("This is your home page.")
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRbaUc-_mCv8y5FlWOnOfxNjGEqej_AaXMBgHDYRyQ2A_3AZ2DSxG_1XKzZQqaU8FG9ptALM0ic3KmK/embed?start=true&loop=true&delayms=3000", height=569)
elif st.session_state['current_page'] == 'Forecast':
    show_Toronto_2024_Electricity_Demand_Forecast()  # function that shows the forecast page
elif st.session_state['current_page'] == 'Modeling':
    show_Toronto_2023_Electricity_Demand_Modeling()  # function that shows the modeling page




# # Set page config
# st.set_page_config(layout="wide", page_title="Electricity Demand Forecast")

# # Custom CSS to inject contained in a string
# custom_css = """
#     <style>
#         .sidebar .sidebar-content {
#             background-color: #2e2e2e;
#             color: white;
#         }
#         .css-1aumxhk {
#             background-color: #2e2e2e;
#             color: white;
#         }
#         .stMarkdown > div > div {
#             background-color: #2e2e2e;
#             padding: 10px;
#             border-radius: 0.5rem;
#             margin-bottom: 10px;
#             border: 1px solid #444;
#         }
#         .stMarkdown a {
#             color: white;
#             text-decoration: none;
#         }
#         .stMarkdown a:hover {
#             color: #0c6efc;
#         }
#         .stMarkdown a:active {
#             color: #0c6efc;
#         }
#     </style>
# """

# # Inject custom CSS with Markdown
# st.markdown(custom_css, unsafe_allow_html=True)

# # Page selection using markdown with navigation links
# def create_sidebar_item(text, emoji, page_key):
#     st.markdown(f"""
#     <div>
#         <a href="#{page_key}" style="font-size: 1.25em; font-weight: bold;">
#             {emoji} {text}
#         </a>
#     </div>
#     """, unsafe_allow_html=True)

# create_sidebar_item("Home", "🏠", "home")
# create_sidebar_item("Forecast", "🔮", "forecast")
# create_sidebar_item("Modeling", "📊", "modeling")

# # Main area
# page = st.experimental_get_query_params().get("page", ["home"])[0]

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

# # Set page config
# st.set_page_config(layout="wide", page_title="Electricity Demand Forecast")

# # Custom CSS to inject contained in a string
# custom_css = """
#     <style>
#         .css-18e3th9 {
#             background-color: black;
#             color: white;
#         }
#         .css-1d391kg {
#             background-color: black;
#             color: white;
#         }
#         .stButton>button {
#             width: 100%;
#             border-radius: 0px;
#             margin: 3px 0px;
#             background-color: #000000;
#             color: #ffffff;
#         }
#         .stButton>button:hover {
#             background-color: #ffffff;
#             color: #000000;
#             border: 1px solid #000000;
#         }
#     </style>
# """

# # Inject custom CSS with Markdown
# st.markdown(custom_css, unsafe_allow_html=True)

# # Page selection using buttons
# def render_page(page_name):
#     st.title(f"This is your {page_name.lower()} page.")

# # Define buttons for navigation
# if st.sidebar.button("Home"):
#     render_page("Home")
# if st.sidebar.button("Forecast"):
#     render_page("Forecast")
# if st.sidebar.button("Modeling"):
#     render_page("Modeling")

# # # Page selection
# # page = st.sidebar.radio("Navigate", ["Home", "Forecast", "Modeling"])

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
