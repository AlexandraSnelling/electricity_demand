# import dependencies
import pandas as pd
import holidays
import requests
from sklearn.preprocessing import StandardScaler
from datetime import datetime, timedelta

####################################################################################
# Functions Required for Data Requests, Parsing, Joins, Engineering and Preparation:
####################################################################################
def get_date_range(year_month, today_date):
    """
    Given a year and month in 'yyyymm' format, returns the start and end dates for that month.
    Adjusts the end date to yesterday's date if it is greater than today's date.
    
    Parameters:
    - year_month (str): Year and month in 'yyyymm' format.
    - today_date (datetime): Today's date for comparison.
    
    Returns:
    - tuple: (start_date, end_date) in 'yyyy-mm-dd' format.
    - bool: Whether the end date was adjusted or not.
    """
    year = int(year_month[:4])
    month = int(year_month[4:])
    
    start_date = datetime(year, month, 1)
    next_month = start_date.replace(day=28) + timedelta(days=4)
    end_date = next_month - timedelta(days=next_month.day)
    
    # Check if end date is in the future
    if end_date > today_date:
        end_date = today_date - timedelta(days=1)  # Adjust to yesterday
        return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), True
    
    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), False
####################################################################################
def parse_weather_data(json_data, parsed_data):
    """
    Parses weather data from the JSON response and appends it to the parsed_data list.
    
    Parameters:
    - json_data (dict): The JSON response from the weather API.
    - parsed_data (list): The list to append the parsed data to.
    """
    weather_data = json_data['data']['weather']
    
    for entry in weather_data:
        date = entry['date']
        astronomy = entry['astronomy'][0]
        hourly_data = entry['hourly']

        for hourly_entry in hourly_data:
            parsed_data.append({
                'date': date,
                'time': hourly_entry['time'],
                'sunrise': astronomy['sunrise'],
                'sunset': astronomy['sunset'],
                'moon_illumination': astronomy['moon_illumination'],
                'DewPointC': hourly_entry['DewPointC'],
                'FeelsLikeC': hourly_entry['FeelsLikeC'],
                'HeatIndexC': hourly_entry['HeatIndexC'],
                'WindChillC': hourly_entry['WindChillC'],
                'WindGustKmph': hourly_entry['WindGustKmph'],
                'cloudcover': hourly_entry['cloudcover'],
                'humidity': hourly_entry['humidity'],
                'precipMM': hourly_entry['precipMM'],
                'pressure': hourly_entry['pressure'],
                'tempC': hourly_entry['tempC'],
                'uvIndex': hourly_entry['uvIndex'],
                'visibility': hourly_entry['visibility'],
                'weatherCode': hourly_entry['weatherCode'],
                'winddirDegree': hourly_entry['winddirDegree'],
                'windspeedKmph': hourly_entry['windspeedKmph']
            })
####################################################################################
def convert_time(time_code):
    """
    Convert time codes from '0', '100', '200', ... to '1', '2', '3', ...
    
    Parameters:
    - time_code (str or int): The time code to convert.
    
    Returns:
    - int: The converted time code.
    """
    time_code = int(time_code)
    return time_code // 100 + 1
####################################################################################
def join_dataframes(demand_df, weather_df):
    # Join the DataFrames on 'date' and 'time' columns
    df = pd.merge(demand_df, weather_df, on=['date', 'time'], how='outer')

    # Ensure 'date' column is in datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Subtract 1 to adjust the 'time' column to 0-23 hour format, ensuring no negative values
    df['time'] = df['time'].astype(int) - 1
    # df['time'] = df['time'].clip(lower=0)

    # add Timedelta to 'date'
    df['ds'] = df['date'] + pd.to_timedelta(df['time'], unit='h')

    # Rename the 'Toronto' column to 'y'
    df.rename(columns={'Toronto': 'y'}, inplace=True)

    # Drop the original 'date' and 'time' columns
    df.drop(['date', 'time'], axis=1, inplace=True)
    
    return df
####################################################################################
def create_time_feature(df):
    # Ensure the 'datetime' column is in datetime format
    df['ds'] = pd.to_datetime(df['ds'])
    
    # Extract features from the datetime column
    df['hourofday'] = df['ds'].dt.hour
    df['dayofweek'] = df['ds'].dt.dayofweek
    df['month'] = df['ds'].dt.month
    df['year'] = df['ds'].dt.year
    df['dayofyear'] = df['ds'].dt.dayofyear
    # df['weekofyear'] = df['ds'].dt.isocalendar().week   
    return df
####################################################################################
def add_holiday_column(df):
    # Create a holiday calendar for Canada
    ca_holidays = holidays.CountryHoliday('CA', prov='ON')
    
    # Ensure the 'datetime' column is in datetime format
    df['ds'] = pd.to_datetime(df['ds'])
    
    # Check if each date is a holiday
    df['is_holiday'] = df['ds'].apply(lambda x: 1 if x.date() in ca_holidays else 0)
    
    return df
####################################################################################
def reorder_dataframe(df):
# Reorder the DataFrame so 'ds' is first, followed by 'y' and any other columns
    columns_order = ['ds'] + [col for col in df.columns if col not in ['ds', 'y']] + ['y']
    df = df[columns_order].drop(columns = ['sunrise', 'sunset'])
    
    return df


####################################################################################
# Data Requests, Parsing, Joins, Engineering and Preparation:
####################################################################################
# Fetch and parse historical data for 2024

# create empty list to hold parsed data
parsed_data = []
today_date = datetime.now()  # Today's date
year_month_list = ['202401', '202402', '202403', '202404', '202405', '202406', '202407', '202408', 
                   '202409', '202410', '202411', '202412']

for year_month in year_month_list:
    start_date, end_date, adjusted = get_date_range(year_month, today_date)
    
    # Skip future months entirely
    if datetime.strptime(start_date, '%Y-%m-%d') > today_date:
        continue
    
    url = 'http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key='+API_KEY+'&q=Toronto&format=json&date='+start_date+'&enddate='+end_date+'&tp=1'
    response = requests.get(url)
    json_data = response.json()
    
    # parse forecast json data to list
    parse_weather_data(json_data, parsed_data)

df_historic = pd.DataFrame(parsed_data)

####################################################################################
# Fetch and parse 14-day forecast data

# create empty list to hold parsed data
parsed_data = []
url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key='+API_KEY+'&q=Toronto&format=json&num_of_days=14&tp=1'
response = requests.get(url)
json_data = response.json()

# parse forecast json data to list
parse_weather_data(json_data, parsed_data)

df_forecast = pd.DataFrame(parsed_data)

####################################################################################
# Combine historical and forecast data
df_weather_2024 = pd.concat([df_historic, df_forecast], ignore_index=True)

# Apply the conversion and formatting
df_weather_2024['time'] = df_weather_2024['time'].apply(convert_time)
df_weather_2024['date'] = pd.to_datetime(df_weather_2024['date'])

####################################################################################
# Fetch and parse electricity demand data

# Direct link to the CSV file
csv_url = 'http://reports.ieso.ca/public/DemandZonal/PUB_DemandZonal.csv'

# Load specific columns of the CSV file into a DataFrame, skipping the first 2 rows
# and specifying the column indices instead of names
TO_demand_2024_df = pd.read_csv(csv_url, usecols=[0, 1, 7], skiprows=3)

# Rename the columns
TO_demand_2024_df.columns = ['date', 'time', 'Toronto']

# Convert 'Date' column to datetime format
TO_demand_2024_df['date'] = pd.to_datetime(TO_demand_2024_df['date'])

# Sort DataFrame by 'Date' and then by 'Hour' in descending order
TO_demand_2024_df = TO_demand_2024_df.sort_values(by=['date', 'time'], ascending=[False, False])

# Reset index after sorting
TO_demand_2024_df = TO_demand_2024_df.reset_index(drop=True)

####################################################################################
# Join demand/weather data and engineer/prepare data for forecasting

# defne prediction data (2024 weather and electricity demand data)
weather_df = df_weather_2024
demand_df = TO_demand_2024_df

# apply data join, engineering and preparation functions
df = join_dataframes(demand_df, weather_df)
df = create_time_feature(df)
df = add_holiday_column(df)
df = reorder_dataframe(df)

# write dataframe to .csv
df.to_csv('test_data_2024.csv', index=False)

####################################################################################