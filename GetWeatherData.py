import requests
from dotenv import load_dotenv
import os
from ErrorFunction import display_error
from WeeklyGUI import display_weekly_weather
from UnitConversion import unit_conversion_fer_to_deg
from MainGUI import display_weather

#Method for retrieving weather information
def get_weather_info(self):
    # API information and URL construction
    load_dotenv("Informative/.env")
    key_weatherAPI = os.getenv("API_KEY")
    city_Input = self.search_input.text().strip()

    if city_Input == "":
        display_error(self, "Please enter a city/country first.")
        return

    self.search_input.clear()
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_Input}?key={key_weatherAPI}&include=fcst&elements=datetime,temp,tempmax,tempmin,precip,windspeed,pressure,icon,conditions&unitGroup=metric"

    # Calling this to reset unit button always to degrees
    unit_conversion_fer_to_deg(self)

    try:
        # Requesting API data and converting to JSON format
        response = requests.get(url, timeout=(5, 20))
        response.raise_for_status()
        weather_data_json = response.json()

        display_weather(self, weather_data_json)
        display_weekly_weather(self, weather_data_json)

    # This catches HTTP errors returned by the API
    except requests.exceptions.HTTPError:
        match response.status_code:
            case 400:
                display_error(self, "400 BAD REQUEST: Invalid request format or parameters.")
            case 401:
                display_error(self, "401 UNAUTHORIZED: API key or account problem.")
            case 404:
                display_error(self, "404 NOT FOUND: Endpoint does not exist.")
            case 429:
                display_error(self, "429 TOO MANY REQUESTS: Rate limit exceeded.")
            case 500:
                display_error(self, "500 INTERNAL SERVER ERROR: Server problem.")
            case _:
                display_error(self, f"HTTP error occurred: {response.status_code}")

    except requests.exceptions.ConnectionError:
        display_error(self, "Network or connection error occurred.")
    except requests.exceptions.Timeout:
        display_error(self, "The request timed out.")
    except requests.exceptions.TooManyRedirects:
        display_error(self, "URL error, too many or wrong redirects.")
    except requests.exceptions.RequestException as e:
        display_error(self, f"Other error occurred:{e}")
