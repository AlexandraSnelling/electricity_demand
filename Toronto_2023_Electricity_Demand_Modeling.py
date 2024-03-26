import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def show_Toronto_2023_Electricity_Demand_Modeling():
    # st.title("Forecast Page")

    # Title of your app
    st.title('2023 Hourly Electricity Demand: Toronto Ontario')

    # Inject custom CSS with the <style> tag
    style = """
    <style>
        .stApp {
            background-image: linear-gradient(to bottom, yellow, orange, black);
            color: #fff;
        }
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)

    # load .csv files for 2023 forecast data to dataframe
    forecast_data_2023 = pd.read_csv('data/forecast_data_2023.csv')
    
    # ensure 'ds' is datetime type in all DataFrames
    forecast_data_2023['ds'] = pd.to_datetime(forecast_data_2023['ds'])

    # # Streamlit application start
    # st.title('Electricity Demand Forecast Visualization')

    # Step 1: Widget for date range selection
    st.subheader('Select Date Range')
    start_date, end_date = st.slider(
        'Date range:',
        min_value=forecast_data_2023['ds'].min(),
        max_value=forecast_data_2023['ds'].max(),
        value=(forecast_data_2023['ds'].min(), forecast_data_2023['ds'].max()),
        format='MM/DD/YYYY'
    )

    # Widget for selecting which predictions to display
    prediction_options = st.multiselect(
        'Select prediction lines to display:',
        options=['y_pred_lstm', 'y_pred_prophet', 'y_pred_xgb'],
        default=['y_pred_lstm', 'y_pred_prophet', 'y_pred_xgb']
    )

    # Filter data based on selected date range
    filtered_data = forecast_data_2023[(forecast_data_2023['ds'] >= start_date) & (forecast_data_2023['ds'] <= end_date)]

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(filtered_data['ds'], filtered_data['y'], label='Actual Demand')

    # Dynamically add selected prediction lines
    if 'y_pred_lstm' in prediction_options:
        ax.plot(filtered_data['ds'], filtered_data['y_pred_lstm'], label='LSTM Predictions')
    if 'y_pred_prophet' in prediction_options:
        ax.plot(filtered_data['ds'], filtered_data['y_pred_prophet'], label='Prophet Predictions')
    if 'y_pred_xgb' in prediction_options:
        ax.plot(filtered_data['ds'], filtered_data['y_pred_xgb'], label='XGBoost Predictions')

    ax.set_xlabel('Date/Time')
    ax.set_ylabel('Demand')
    ax.legend()
    st.pyplot(fig)

    # MAPE and Max Absolute Percentage Error Calculation & Display
    for option in prediction_options:
        y_true = filtered_data['y']
        y_pred = filtered_data[option]

        # Calculate MAPE
        mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
        # Calculate Max Absolute Percentage Error
        max_error = np.max(np.abs((y_true - y_pred) / y_true)) * 100

        st.write(f"MAPE for {option}: {mape:.2f}%")
        st.write(f"Max Absolute Percentage Error for {option}: {max_error:.2f}%")
