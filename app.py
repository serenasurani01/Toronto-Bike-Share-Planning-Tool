from flask import Flask, render_template, request
import h3
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

df_stations = pd.read_csv('df_lng_lat.csv')
location_names = pd.read_csv('location_names.csv')
def get_closest_station(user_lat,user_lng):
    df_stations['lat'] = df_stations['lat'].astype(float)
    df_stations['lng'] = df_stations['lng'].astype(float)
    user_h3_index = h3.geo_to_h3(user_lat, user_lng, 9)
    df_stations['h3_index'] = df_stations.apply(lambda x: h3.geo_to_h3(x['lat'], x['lng'], 9), axis=1)
    df_stations['h3_distance'] = df_stations['h3_index'].apply(lambda x: h3.h3_distance(user_h3_index, x))
    closest_station = df_stations.iloc[df_stations['h3_distance'].idxmin()]['Station_ID']
    return closest_station

def get_season_and_day(date_input):
    date_obj = datetime.strptime(date_input, '%Y-%m-%d')
    day_of_week = date_obj.weekday()
    month = date_obj.month
    day = date_obj.day
    if (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day < 20):
        season = 'winter'
    elif (month == 3 and day >= 20) or (4 <= month <= 5) or (month == 6 and day < 21):
        season = 'spring'
    elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day < 22):
        season = 'summer'
    elif (month == 9 and day >= 22) or (10 <= month <= 11) or (month == 12 and day < 21):
        season = 'fall'
    return season, day_of_week

def get_rounded_hour_of_day(time_input):
    time_obj = datetime.strptime(time_input, '%H:%M')
    hour = time_obj.hour
    minute = time_obj.minute
    if minute >= 30:
        hour = (hour + 1) % 24
    
    return hour
df_grouped = pd.read_csv('final_data_for_app.csv')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lat = float(request.form.get('latitude'))
        lng = float(request.form.get('longitude'))
        time_trip = request.form.get('time')
        date_trip = request.form.get('date')
        closest_station = get_closest_station(lat,lng)
        season, day_of_week = get_season_and_day(date_trip)
        rounded_hour = get_rounded_hour_of_day(time_trip)
        bikes_station = df_grouped[(df_grouped['season']==season)&(df_grouped['day_of_week']==day_of_week)&(df_grouped['hour']==rounded_hour)&(df_grouped['station_id']==int(closest_station))]['moving_average_bike_count']
        bikes_station_value = int(bikes_station.values[0])
        station_name = location_names[location_names['ID']==closest_station]['Title'].values[0]
        return render_template('output.html', bikes_station_value=bikes_station_value, station_name=station_name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
