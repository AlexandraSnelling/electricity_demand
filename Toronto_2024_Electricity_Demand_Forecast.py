# Required Dependencies
import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt
from joblib import load
import streamlit as st
from sklearn.metrics import max_error
from datetime import datetime

def show_Toronto_2024_Electricity_Demand_Forecast():
    # st.title("Forecast Page")

    # Title of your app
    st.title('2024 Toronto Electricity Demand Forecasting')

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

    # My Application
    # Step 1: Prepare Data 

    # load .csv files for 2024 weather and electricity demand data to dataframe
    test_data = pd.read_csv('data/test_data_2024.csv')

    X_test = test_data.iloc[:,1:-1]
    y_test = test_data.iloc[:,-1]

    # isolate 'is_holiday' column and keep other columns for scaling
    X_test_to_scale = X_test.drop('is_holiday', axis=1)

    # Load the scaler
    scalerX = load('models/scalerX_trained_2019-2023.joblib')

    # apply StandardScaler to data without 'is_holiday' column
    X_test_scaled = scalerX.transform(X_test_to_scale)

    # convert scaled array back into dataframe
    X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=X_test_to_scale.columns, index=X_test_to_scale.index)

    # add 'is_holiday' column back to scaled dataframes
    X_test_scaled_df['is_holiday'] = X_test['is_holiday']


    # Step 2: Apply Trained Model

    # initialize an instance of XGBoost Regressor
    model = xgb.XGBRegressor()

    # load trained model from json file
    model.load_model('models/xgb_model_trained_2019-2023.json')

    # apply model to data to make demand predictions
    y_predictions_xgb = model.predict(X_test_scaled)

    # create predictions dataframe
    test_data_predictions = test_data.drop(columns='y')
    test_data_predictions['y_predictions_xgb'] = y_predictions_xgb

    # define data to be used in MAPE calculation
    y = test_data['y']
    y_predict = test_data_predictions['y_predictions_xgb']

    # Calculate MAPE and round to 2 decimal places
    mape = round((abs((y - y_predict) / y).mean()) * 100, 2)

    # Calculate the Absolute Percentage Error for each prediction
    absolute_errors = round(abs(y - y_predict), 2)

    # Find the maximum absolute percentage error
    max_absolute_error = absolute_errors.max()
    
    # define data to be plotted
    plot_data = pd.concat([test_data.set_index('ds')['y'], test_data_predictions.set_index('ds')['y_predictions_xgb']], axis=1)
    plot_data.columns = ['Demand', 'XGBoost Forecast Demand']


    # Step 3: Select Dates, Plot Data and Calculate MAPE

    # Date range selection
    start_date, end_date = st.select_slider(
        'SELECT DATE RANGE',
        options=pd.to_datetime(plot_data.index).date,
        value=(pd.to_datetime(plot_data.index).min().date(), pd.to_datetime(plot_data.index).max().date())
    )

    # Filter data based on the selected date range
    plot_data_filtered = plot_data[(plot_data.index >= str(start_date)) & (plot_data.index <= str(end_date))]

    fig, ax = plt.subplots(figsize=(34, 12))  
    # plot_data.plot(ax=ax)
    plot_data_filtered.plot(ax=ax)
    ax.set_xlabel('Date/Time', fontsize=20)
    ax.set_ylabel('Demand', fontsize=20)
    plt.xticks(rotation=45, ha='right', fontsize=18)
    ax.tick_params(axis='y', labelsize=18)  
    ax.set_title('2024 Hourly Toronto Electricity XGBoost Model Forecast vs. Actual Demand', fontsize=24)
    plt.tight_layout() 
    ax.legend(fontsize=22)
    st.pyplot(fig)
    
    # # write with Streamlit
    st.write(f"XGBoost Model Mean Absolute Percentage Error (2024): {mape}%")
    st.write(f"XGBoost Model Maximum Absolute Error (2024): {max_absolute_error} (MW)")

#     # First, filter the 'test_data_predictions' DataFrame for today or future dates.
#     today = pd.Timestamp(datetime.now().date())  # Get today's date
#     test_data_predictions['ds'] = pd.to_datetime(test_data_predictions['ds'])
#     future_data = test_data_predictions[test_data_predictions['ds'] >= today]

#     # Then, create a new DataFrame with formatted columns to match the desired table structure.
#     table_to_display = future_data.copy()
#     table_to_display['Date'] = table_to_display['ds'].dt.date
#     table_to_display['Time'] = table_to_display['ds'].dt.time
#     table_to_display = table_to_display[['Date', 'Time', 'y_predictions_xgb']]

#     # Rename the 'y_predictions_xgb' column to 'XGBoost Forecast Demand' for display.
#     table_to_display.rename(columns={'y_predictions_xgb': 'XGBoost Forecast Demand (MW)'}, inplace=True)

#     # Now, display this table in the Streamlit app.
#     st.table(table_to_display)
    
#     # ... [the previous part of your Streamlit app code] ...

#     # Convert the 'ds' column to datetime if it's not already
#     test_data_predictions['ds'] = pd.to_datetime(test_data_predictions['ds'])

#     # Filter the DataFrame for dates that are today or in the future
#     today = pd.Timestamp(datetime.now().date())  # Get today's date
#     future_data = test_data_predictions[test_data_predictions['ds'] >= today]

#     # Create the table display
#     table_to_display = future_data.copy()
#     table_to_display['Date'] = table_to_display['ds'].dt.date
#     table_to_display['Time'] = table_to_display['ds'].dt.time

#     # Round the 'XGBoost Forecast Demand' to two decimal places
#     table_to_display['y_predictions_xgb'] = table_to_display['y_predictions_xgb'].round(2)

#     # Select and rename the columns for the table
#     table_to_display = table_to_display[['Date', 'Time', 'y_predictions_xgb']]
#     table_to_display.rename(columns={'y_predictions_xgb': 'XGBoost Forecast Demand'}, inplace=True)

#     # Use Streamlit to display the table without the index
#     st.table(table_to_display.set_index(pd.Index([i for i in range(len(table_to_display))])))

#     # ... [the previous part of your Streamlit app code] ...

#     # Convert the 'ds' column to datetime if it's not already
#     test_data_predictions['ds'] = pd.to_datetime(test_data_predictions['ds'])

#     # Filter the DataFrame for dates that are today or in the future
#     today = pd.Timestamp(datetime.now().date())  # Get today's date
#     future_data = test_data_predictions[test_data_predictions['ds'] >= today]

#     # Create the table display
#     table_to_display = future_data.copy()
#     table_to_display['Date'] = table_to_display['ds'].dt.date
#     table_to_display['Time'] = table_to_display['ds'].dt.time

#     # Round the 'XGBoost Forecast Demand' to two decimal places
#     table_to_display['XGBoost Forecast Demand'] = table_to_display['y_predictions_xgb'].round(2)

#     # Select and rename the columns for the table
#     table_to_display = table_to_display[['Date', 'Time', 'XGBoost Forecast Demand']]

#     # Use Streamlit to display the table without the index
#     st.table(table_to_display.assign(hack='').set_index('hack'))
    
    
    # ... [the previous part of your Streamlit app code] ...

    # Convert the 'ds' column to datetime if it's not already
    test_data_predictions['ds'] = pd.to_datetime(test_data_predictions['ds'])

    # Filter the DataFrame for dates that are today or in the future
    today = pd.Timestamp(datetime.now().date())  # Get today's date
    future_data = test_data_predictions[test_data_predictions['ds'] >= today]

    # Create the table display
    table_to_display = future_data.copy()
    table_to_display['Date'] = table_to_display['ds'].dt.date
    table_to_display['Time'] = table_to_display['ds'].dt.time

    # Ensure 'y_predictions_xgb' is of float type, then round to two decimal places
    table_to_display['XGBoost Forecast Demand'] = table_to_display['y_predictions_xgb'].astype(float).round(2)

    # Select and rename the columns for the table
    table_to_display = table_to_display[['Date', 'Time', 'XGBoost Forecast Demand']]

    # Use Streamlit to display the table without the original index and the temporary 'hack' column
    st.table(table_to_display.assign(hack='').set_index('hack'))

