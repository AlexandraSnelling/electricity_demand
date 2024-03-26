import streamlit as st
from streamlit.components.v1 import components  # Add this line to import components
from Toronto_2024_Electricity_Demand_Forecast import show_Toronto_2024_Electricity_Demand_Forecast
from Toronto_2023_Electricity_Demand_Modeling import show_Toronto_2023_Electricity_Demand_Modeling

# Set the page config here, as the very first Streamlit call
st.set_page_config(layout="wide", page_title="Electricity Demand Forecast")

# Page selection
page = st.sidebar.selectbox("Choose a page", ["Home", "Forecast", "Modeling"])

if page == "Home":
    st.title("This is your home page.")
    # Place the components.iframe call inside the condition where you want it to appear
    components.iframe("https://docs.google.com/presentation/d/e/2PACX-1vRbaUc-_mCv8y5FlWOnOfxNjGEqej_AaXMBgHDYRyQ2A_3AZ2DSxG_1XKzZQqaU8FG9ptALM0ic3KmK/embed?start=true&loop=true&delayms=3000", height=569)
elif page == "Forecast":
    show_Toronto_2024_Electricity_Demand_Forecast()
elif page == "Modeling":
    show_Toronto_2023_Electricity_Demand_Modeling()

    
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
