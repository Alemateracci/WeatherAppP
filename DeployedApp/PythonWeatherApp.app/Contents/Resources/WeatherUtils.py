from datetime import datetime

#Method for retrieving weather icon based on API weather condition ID
def weather_icon(weather_ID):
    match weather_ID:
        case "snow":
            return "WeatherIcons/snow.png"
        case "rain":
            return "WeatherIcons/rain.png"
        case "fog":
            return "WeatherIcons/fog.png"
        case "wind":
            return "WeatherIcons/wind.png"
        case "cloudy":
            return "WeatherIcons/cloudy.png"
        case "partly-cloudy-day":
            return "WeatherIcons/partly-cloudy-day.png"
        case "partly-cloudy-night":
            return "WeatherIcons/partly-cloudy-night.png"
        case "clear-day":
            return "WeatherIcons/clear-day.png"
        case "clear-night":
            return "WeatherIcons/clear-night.png"
        case _:
            return "WeatherIcons/clear-day.png"


#Method for converting API date to weekday name
def weather_weekday(day_date):
    try:
        w = datetime.strptime(day_date, "%Y-%m-%d").weekday()
    except Exception:
        return "?"

    match w:
        case 0:
            return "Mon"
        case 1:
            return "Tue"
        case 2:
            return "Wed"
        case 3:
            return "Thu"
        case 4:
            return "Fri"
        case 5:
            return "Sat"
        case 6:
            return "Sun"
        case _:
            return "?"
