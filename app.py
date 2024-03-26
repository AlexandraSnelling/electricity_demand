import streamlit as st
# Import your page functions
from Toronto_2024_Electricity_Demand_Forecast import show_Toronto_2024_Electricity_Demand_Forecast

# Page selection
page = st.sidebar.selectbox("Choose a page", ["Home", "Forecast"])

if page == "Home":
    st.write("This is your home page.")
    # You can put the content of your home page here
elif page == "Forecast":
    show_Toronto_2024_Electricity_Demand_Forecast()