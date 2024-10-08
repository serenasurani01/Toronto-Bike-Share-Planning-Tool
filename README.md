# Toronto Bike Share Planning Tool
A web applicaion designed to help users plan their commute by checking bike availability at their nearest station for future dates. Whether you're scheduling your commute for Friday or planning a weekend ride, the app forecasts how many bikes will be available at a specific time and location.  

### Demo Video
Watch the demo video [here](https://youtu.be/yPUQJBBdPPM).
[![Watch the video](https://img.youtube.com/vi/yPUQJBBdPPM/maxresdefault.jpg)](https://youtu.be/yPUQJBBdPPM)

## Features  
* Location Selection: Users can input their location, and the app will automatically identify the nearest bike station.
* Date and Time Input: Users specify a future date and time to check bike availability.
* Bike Availability Forecasting: The app calculates bike availability based on historical data patterns to predict how many bikes will be at the chosen station in the future.

## Technologies Used
* Frontend: HTML, CSS, Leaflet.js for interactive maps.
* Backend: Python, Flask for handling user input and interacting with historical data.
* Data Processing: Pandas for processing and analyzing historical bike data to generate future predictions.
* Map Services: OpenStreetMap is used to display map data and select locations.
* Methodologies: Time series analysis for bike availability prediction, H3 Uber’s Hexagonal Hierarchical Spatial Index to determine nearest bike station

## Procedure for Building the App
1. **Data Collection:** 2023 Historical transaction data from Toronto Bike share was compiled including bike availability at various stations throughout the year.  
2. **Data Preprocessing:** The data was cleaned and structured to ensure that there was a count for bikes available at any given station by minute. This involved filling in gaps where data was missing and aligning data points to ensure accurate availability tracking.  
3. **Data Segmentation:** The data was segmented by time of year, day of the week, and time of day, allowing the app to capture recurring patterns in bike demand.  
4. **Time Series Analysis**: I applied time series analysis to forecast bike availability at specific stations for future dates and times based on historical trends.  
5. **App Integration: **The time series analysis was integrated into a Flask app, where users can input their location, date, and time to receive a forecast of bike availability at the closest station.


