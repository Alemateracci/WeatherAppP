import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from dotenv import load_dotenv
import os
from MainGUI import GUI_main_parameters, GUI_weather_parameters, display_weather
from WeeklyGUI import display_weekly_weather
from ErrorFunction import display_error
from UnitConversion import unit_conversion_deg_to_fer, unit_conversion_fer_to_deg

class MainAppWindow(QMainWindow):
    #Constructor method
    def __init__(self):
        super().__init__()

        #Constructing and Setting up main window
        self.setWindowTitle("Weather Application")
        self.setGeometry(450, 200, 800, 600)
        self.setStyleSheet("background-color: #242424;")

        #Calling method to set up GUI parameters
        GUI_main_parameters(self)
        GUI_weather_parameters(self)


    #Method for retrieving weather information 
    def get_weather_info(self):    
        #API information and URL construction
        load_dotenv()
        key_weatherAPI = os.getenv("API_KEY")
        city_Input = self.search_input.text()
        self.search_input.clear()
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_Input}?key={key_weatherAPI}&include=fcst&elements=datetime,temp,tempmax,tempmin,precip,windspeed,pressure,icon,conditions&unitGroup=metric"
        
        #Calling this to reset unit button always to degrees 
        unit_conversion_fer_to_deg(self)

        try:
            #Requesting API data and converting to JSON format
            response = requests.get(url)
            response.raise_for_status()
            weather_data_json = response.json()
            display_weather(self, weather_data_json)
            display_weekly_weather(self, weather_data_json)

        #This catches HTTP errors returned by the API
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

        #This catches network errors
        except requests.exceptions.ConnectionError:
            display_error(self, "Network or connection error occurred.")
        #This catches timeout errors
        except requests.exceptions.Timeout:
            display_error(self, "The request timed out.")
        #This catches URL errors
        except requests.exceptions.TooManyRedirects:
            display_error(self, "URL error, too many or wrong redirects.")
        #This catches any other errors
        except requests.exceptions.RequestException as e:
            display_error(self, f"Other error occurred:{e}")




#Main if statement 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainAppWindow()
    main_window.show()
    sys.exit(app.exec_())