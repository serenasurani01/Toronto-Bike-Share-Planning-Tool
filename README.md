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
* Map Services: OpenStreetMap for displaying map data and location selection.
* Methodologies: Time series analysis for bike availability prediction, H3 Uber’s Hexagonal Hierarchical Spatial Index to determine nearest bike station
