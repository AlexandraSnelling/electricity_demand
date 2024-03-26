import streamlit as st
from Toronto_2024_Electricity_Demand_Forecast import show_Toronto_2024_Electricity_Demand_Forecast

# Set the page config here, as the very first Streamlit call
st.set_page_config(layout="wide", page_title="Electricity Demand Forecast")

# Page selection
page = st.sidebar.selectbox("Choose a page", ["Home", "Forecast"])

if page == "Home":
    st.title("This is your home page.")
elif page == "Forecast":
    show_Toronto_2024_Electricity_Demand_Forecast()