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

    # Convert 'ds' to datetime just in case it's not in the right format
    forecast_data_2023['ds'] = pd.to_datetime(forecast_data_2023['ds'])

    # Calculate min and max dates for the slider
    min_date = forecast_data_2023['ds'].min()
    max_date = forecast_data_2023['ds'].max()

    # Safety check: If there's any NaT or NaN values after conversion, slider will throw an error.
    if pd.isnull(min_date) or pd.isnull(max_date):
        st.error('Date range is invalid. Please check your "ds" column for NaN or NaT values.')
        st.stop()

    # Step 1: Widget for date range selection
    start_date, end_date = st.slider(
        'Date range:',
        min_value=min_date.to_pydatetime(),  # Convert to Python datetime just in case
        max_value=max_date.to_pydatetime(),  # Convert to Python datetime just in case
        value=(min_date.to_pydatetime(), max_date.to_pydatetime()),  # Ensure both are the same type
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
    fig, ax = plt.subplots(figsize=(34, 12))
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
    plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotate labels and set font size
    plt.tight_layout()  # This will make sure the labels and title fit into the figure area
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
