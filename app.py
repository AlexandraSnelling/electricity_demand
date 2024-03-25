# Required Dependencies
import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt
from joblib import load
import streamlit as st

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

# define data to be plotted
plot_data = pd.concat([test_data.set_index('ds')['y'], test_data_predictions.set_index('ds')['y_predictions_xgb']], axis=1)
plot_data.columns = ['Demand', 'Predicted Demand']


# Step 3: Plot Data and Calculate MAPE

# # Creating the plot
# ax = plot_data.plot(figsize=(24, 6))

# # Setting the axis labels
# ax.set_xlabel('Date/Time')
# ax.set_ylabel('Demand')

# # Setting the plot title
# ax.set_title('Hourly Toronto Electricity Demand vs. Predicted Demand')

# # Adjusting the legend
# ax.legend()

# # Display the plot
# plt.show()

# print(f"Mean Absolute Percentage Error: {mape}%")


# Plotting with Streamlit

# Custom CSS
st.markdown("""
<style>
body {
    color: #fff;
    background-color: #267;
    background-image: linear-gradient(to right, yellow, green, darkblue);
}
</style>
    """, unsafe_allow_html=True)

# Add your title here
st.title('Hourly Toronto Electricity Demand Prediction')

# Date range selection
start_date, end_date = st.select_slider(
    'Select a range of dates',
    options=pd.to_datetime(plot_data.index).date,
    value=(pd.to_datetime(plot_data.index).min().date(), pd.to_datetime(plot_data.index).max().date())
)

# Filter data based on the selected date range
plot_data_filtered = plot_data[(plot_data.index >= str(start_date)) & (plot_data.index <= str(end_date))]

fig, ax = plt.subplots(figsize=(24, 6))
# plot_data.plot(ax=ax)
plot_data_filtered.plot(ax=ax)
ax.set_xlabel('Date/Time')
ax.set_ylabel('Demand')
ax.set_title('Hourly Toronto Electricity Demand vs. Predicted Demand')
ax.legend()
st.pyplot(fig)

# write with Streamlit
st.write(f"Mean Absolute Percentage Error: {mape}%")