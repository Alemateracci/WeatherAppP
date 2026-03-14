import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from dotenv import load_dotenv
import os
from utilities import weather_icon
from MainGUI import GUI_main_parameters, GUI_weather_parameters
from WeeklyGUI import display_weekly_weather
from ErrorFunction import display_error

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
        self.unit_conversion_fer_to_deg()

        try:
            #Requesting API data and converting to JSON format
            response = requests.get(url)
            response.raise_for_status()
            weather_data_json = response.json()
            self.display_weather(weather_data_json)
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


    #Method for converting Celsius to Fahrenheit
    def unit_conversion_deg_to_fer(self):
        self.degree_button.setDisabled(False)
        self.degree_button.setStyleSheet("""QPushButton 
                                            {
                                                font-size: 30px;
                                                background-color: transparent;
                                                color: #9e9d9d
                                            }
                                            QPushButton:hover 
                                            {
                                                color: #ffffff;
                                            }
                                         """)
        
        self.fahrenheit_button.setStyleSheet("""QPushButton 
                                                {
                                                    font-size: 30px;
                                                    background-color: transparent;
                                                    color: #ffffff;
                                                }
                                                QPushButton:hover 
                                                {
                                                    color: #ffffff;
                                                }
                                             """)
        
        if self.temperature_result_label.text() == "":
            pass
        else:
            self.temperature_result_label.setText(f"{(int(self.temperature_result_label.text()) * 9/5) + 32:.0f}")
            for i in range(7):
                temp_label = self.findChild(QLabel, f"temp_label_{i}")
                min_temp = temp_label.property("min_temp")
                max_temp = temp_label.property('max_temp')
                temp_label.setText(f"{(int(min_temp) * 9/5) + 32:.0f}°F | {(int(max_temp) * 9/5) + 32:.0f}°F")
            self.fahrenheit_button.setDisabled(True)


    #Method for converting Fahrenheit to Celsius
    def unit_conversion_fer_to_deg(self):
        self.fahrenheit_button.setDisabled(False)
        self.degree_button.setStyleSheet("""QPushButton 
                                            {
                                                font-size: 30px;
                                                background-color: transparent;
                                                color: #ffffff
                                            }
                                            QPushButton:hover 
                                            {
                                                color: #ffffff;
                                            }
                                         """)
        
        self.fahrenheit_button.setStyleSheet("""QPushButton 
                                                {
                                                    font-size: 30px;
                                                    background-color: transparent;
                                                    color: #9e9d9d
                                                }
                                                QPushButton:hover 
                                                {
                                                    color: #ffffff;
                                                }
                                             """)

        if self.temperature_result_label.text() == "":
            pass
        else:
            self.temperature_result_label.setText(f"{(int(self.temperature_result_label.text()) - 32) * 5/9:.0f}")
            for i in range(7):
                temp_label = self.findChild(QLabel, f"temp_label_{i}")
                min_temp = temp_label.property('min_temp')
                max_temp = temp_label.property('max_temp')
                temp_label.setText(f"{int(min_temp)}°C | {int(max_temp)}°C")
            self.degree_button.setDisabled(True)
        

    #Method for displaying weather information
    def display_weather(self, weather_data_json):
        self.country_result_label.setText((weather_data_json['resolvedAddress'].split(",")[0]).capitalize())

        self.temperature_result_label.setText(f"{weather_data_json['days'][0]['temp']:.0f}")

        self.precipitation_label.setText(f"Precipitation: {weather_data_json['days'][0]['precip']:.0f} % \nWind Speed: {weather_data_json['days'][0]['windspeed']:.0f} km/h \nPressure: {weather_data_json['days'][0]['pressure']:.0f} hPa")

        self.weather_description_label.setText(weather_data_json['days'][0]['conditions'])

        Pixmap_icon_address = QPixmap(weather_icon(weather_data_json['days'][0]['icon']))
        self.icon_result_label.setScaledContents(True) 
        self.icon_result_label.setPixmap(Pixmap_icon_address)


#Main if statement 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainAppWindow()
    main_window.show()
    sys.exit(app.exec_())