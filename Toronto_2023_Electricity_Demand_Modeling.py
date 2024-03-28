import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.metrics import max_error as max_error_metric

# function called from app.py homepage when Modeling button selected
def show_Toronto_2023_Electricity_Demand_Modeling():
    # st.title("Forecast Page")

    # Page title
    st.title('Model Evaluation:')
    st.title('Actual vs Forecast Demand 2023 Toronto Electricity')

    # Custom CSS with <style> tag
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

    def calculate_metrics(y_true, y_pred):
        # Define calculation of each metric and format to strings with two decimal places
        r2 = "{:.2f}".format(r2_score(y_true, y_pred))
        mape = "{:.2f}".format(np.mean(np.abs((y_true - y_pred) / y_true)) * 100)
        mean_abs_error = "{:.2f}".format(mean_absolute_error(y_true, y_pred))
        max_abs_error = "{:.2f}".format(max_error_metric(y_true, y_pred))
        return r2, mape, mean_abs_error, max_abs_error

    def show_evaluation_table(forecast_data):
        # Calculate metrics for each model and create a DataFrame
        model_metrics = {
            'Model': ['LSTM', 'Prophet', 'XGB'],
            'R2': [],
            'Mean Absolute % Error': [],
            'Mean Absolute Error (MW)': [],
            'Maximum Absolute Error (MW)': []
        }

        for model in model_metrics['Model']:
            y_true = forecast_data['y']
            y_pred = forecast_data[f'y_pred_{model.lower()}']
            r2, mape, mean_abs_error, max_abs_error = calculate_metrics(y_true, y_pred)

            # Convert metrics directly to strings
            model_metrics['R2'].append(r2)
            model_metrics['Mean Absolute % Error'].append(mape)
            model_metrics['Mean Absolute Error (MW)'].append(mean_abs_error)
            model_metrics['Maximum Absolute Error (MW)'].append(max_abs_error)

        # Convert the dictionary to a DataFrame
        metrics_df = pd.DataFrame(model_metrics)

        # Apply custom CSS to style the table with a white background, black border, and black text
        st.markdown("""
            <style>
                .st-emotion-css-1 { border: 1px solid black; }
                .css-1cpxqw2 { border-collapse: collapse; }
                .st-eg { border-collapse: collapse; }
                .st-cj { border-collapse: collapse; }
                table { color: black !important; background-color: white !important; }
                th { color: black !important; background-color: white !important; border: 1px solid black !important; }
                td { color: black !important; background-color: white !important; border: 1px solid black !important; }
                .st-df { border: none !important; }
                .st-bw { border: none !important; }
            </style>
            """, unsafe_allow_html=True)

        # Display the DataFrame as a table
        st.table(metrics_df.assign(hack='').set_index('hack').iloc[:, :])
        # st.table(metrics_df.iloc[:, :])
        # st.table(metrics_df.reset_index(drop=True))

    # Call the function to display the evaluation table
    show_evaluation_table(forecast_data_2023)
    
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

#     # Widget for selecting which predictions to display
#     prediction_options = st.multiselect(
#         'Select prediction lines to display:',
#         options=['y_pred_lstm', 'y_pred_prophet', 'y_pred_xgb'],
#         default=['y_pred_lstm', 'y_pred_prophet', 'y_pred_xgb']
#     )

#     # Filter data based on selected date range
#     filtered_data = forecast_data_2023[(forecast_data_2023['ds'] >= start_date) & (forecast_data_2023['ds'] <= end_date)]

#     # Plotting
#     fig, ax = plt.subplots(figsize=(34, 12))
#     ax.plot(filtered_data['ds'], filtered_data['y'], label='Actual Demand')
   
#     # Dynamically add selected prediction lines
#     if 'y_pred_lstm' in prediction_options:
#         ax.plot(filtered_data['ds'], filtered_data['y_pred_lstm'], label='LSTM Predictions')
#     if 'y_pred_prophet' in prediction_options:
#         ax.plot(filtered_data['ds'], filtered_data['y_pred_prophet'], label='Prophet Predictions')
#     if 'y_pred_xgb' in prediction_options:
#         ax.plot(filtered_data['ds'], filtered_data['y_pred_xgb'], label='XGBoost Predictions')

#     ax.set_xlabel('Date/Time')
#     ax.set_ylabel('Demand')
#     plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotate labels and set font size
#     plt.tight_layout()  # This will make sure the labels and title fit into the figure area
#     ax.legend()
#     st.pyplot(fig)

#     # MAPE and Max Absolute Percentage Error Calculation & Display
    
#     for option in prediction_options:
#         y_true = filtered_data['y']
#         y_pred = filtered_data[option]

#         # Calculate MAPE
#         mape_floating = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
        
#         # Calculate Max Absolute Percentage Error
#         # max_error_floating = np.max(np.abs((y_true - y_pred) / y_true)) * 100

#         st.write(f"MAPE for {option}: {mape_floating:.2f}%")
#         # st.write(f"Max Absolute Percentage Error for {option}: {max_error_floating:.2f}%")   
        
    # Define a mapping from column names to display names
    name_mapping = {
        'y_pred_lstm': 'LSTM',
        'y_pred_prophet': 'Prophet',
        'y_pred_xgb': 'XGB'
    }

    # Widget for selecting which predictions to display
    prediction_options = st.multiselect(
        'Select Models to display:',
        options=list(name_mapping.values()),  # Display names instead of column names
        default=list(name_mapping.values())
    )

    # Filter data based on selected date range
    filtered_data = forecast_data_2023[(forecast_data_2023['ds'] >= start_date) & (forecast_data_2023['ds'] <= end_date)]

    # Plotting
    fig, ax = plt.subplots(figsize=(34, 12))
    ax.plot(filtered_data['ds'], filtered_data['y'], label='Actual Demand')

    # Dynamically add selected prediction lines using the mapping to get the correct column names
    for display_name in prediction_options:
        # Find the column name that corresponds to the selected display name
        column_name = [key for key, value in name_mapping.items() if value == display_name][0]
        ax.plot(filtered_data['ds'], filtered_data[column_name], label=f'{display_name} Predictions')

    ax.set_xlabel('Date/Time', fontsize=18)
    ax.set_ylabel('Demand (MW)', fontsize=18)
    plt.xticks(rotation=45, ha='right', fontsize=16)  # Rotate labels and set font size
    ax.set_title('2023 Hourly Toronto Electricity Forecast vs. Actual Demand', fontsize=22)
    plt.tight_layout()  # This will make sure the labels and title fit into the figure area
    ax.legend(fontsize=22)
    st.pyplot(fig)
    
    # fig, ax = plt.subplots(figsize=(34, 12))  
    # # plot_data.plot(ax=ax)
    # plot_data_filtered.plot(ax=ax)
    # ax.set_xlabel('Date/Time', fontsize=18)
    # ax.set_ylabel('Demand', fontsize=18)
    # ax.tick_params(axis='x', labelsize=16)
    # ax.tick_params(axis='y', labelsize=16)  
    # ax.set_title('Hourly Toronto Electricity Demand vs. Predicted Demand', fontsize=22)
    # ax.legend(fontsize=22)
    # st.pyplot(fig)

    # MAPE and Max Absolute Percentage Error Calculation & Display
    for display_name in prediction_options:
        # Find the column name that corresponds to the selected display name
        column_name = [key for key, value in name_mapping.items() if value == display_name][0]
        y_true = filtered_data['y']
        y_pred = filtered_data[column_name]

        # Calculate MAPE
        mape_floating = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
        # Calculate Max Absolute Percentage Error
        # max_error_floating = np.max(np.abs((y_true - y_pred) / y_true)) * 100

        # Display using the display names
        start = start_date.strftime('%m/%d/%Y')
        end = end_date.strftime('%m/%d/%Y')
        st.write(f"{display_name} Mean Absolute % Error ({start} - {end}) : {mape_floating:.2f}%")
        # st.write(f"Max Absolute Percentage Error for {display_name}: {max_error_floating:.2f}%")