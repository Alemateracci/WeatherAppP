import sys
import requests
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox, QWidget, QHBoxLayout, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from dotenv import load_dotenv
import os

class MainAppWindow(QMainWindow):
    #Constructor method
    def __init__(self):
        super().__init__()

        #Constructing and Setting up main window
        self.setWindowTitle("Weather Application")
        self.setGeometry(450, 200, 800, 600)
        self.setStyleSheet("background-color: #242424;")

        #Constructing welcome message label
        self.welcome_label = QLabel("Welcome to Weather \nApplication!", self)
        
        #Constructing search text box
        self.search_input = QLineEdit(self)

        #Constructing search button
        self.search_button = QPushButton("Get Weather", self)

        #Constructing search result background label
        self.search_result_backgroundC_label = QLabel(self)

        #Constructing city/country result label
        self.country_result_label = QLabel("City Weather", self)

        #Constructing weather icon result label
        self.icon_result_label = QLabel(self)
        
        #Constructing temperature result label
        self.temperature_result_label = QLabel(self)
        
        #Constructing degree converter button
        self.degree_button = QPushButton("°C/", self)
        
        #Constructing fahrenheit converter button
        self.fahrenheit_button = QPushButton("°F", self)

        #Constructing precipitation, wind speed and pressure result label
        self.precipitation_label = QLabel(f"Precipitation: 0% \nWind Speed: 0 km/h \nPressure: 0 hPa", self)
        
        #Constructing weather condition description label 
        self.weather_description_label = QLabel(self)
        
        #Constructing an error message box
        self.error_message = QMessageBox()

        #Calling method to set up GUI parameters
        self.GUI_main_parameters()
        self.GUI_weather_parameters()


    #Method for setting up main GUI parameters
    def GUI_main_parameters(self):
        #Setting up welcome message label
        self.welcome_label.setGeometry(0, 5, 800, 90)
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setStyleSheet("font-size: 40px;" 
                                         "font-weight: bold;"
                                         "color: white;")
        
        #Setting search text box
        self.search_input.setAlignment(Qt.AlignLeft)
        self.search_input.setPlaceholderText('Enter the city and/or country (e.g. "London, UK")')
        self.search_input.setGeometry(270, 118, 550, 50)
        self.search_input.setStyleSheet("font-size: 20px;"
                                        "border: none")
        
        #Setting search button
        self.search_button.setGeometry(90, 123, 150, 40)
        self.search_button.setStyleSheet("""QPushButton 
                                            {
                                                font-size: 17px;
                                                background-color: #575757;
                                                border-radius: 20px;
                                            }
                                            QPushButton:hover 
                                            {
                                                background-color: #474747;
                                            }
                                            QPushButton:pressed
                                            {
                                                background-color: #2e2e2e;  
                                            }
                                         """)
        self.search_button.clicked.connect(self.get_weather_info)

        #Setting search result background label
        self.search_result_backgroundC_label.setGeometry(0, 170, 800, 450)
        self.search_result_backgroundC_label.setStyleSheet("background-color: #303030;"
                                                           "border-radius: 25px;")
        
        #Setting an error message box
        self.error_message.setIcon(QMessageBox.Critical)
        self.error_message.setWindowFlags(Qt.FramelessWindowHint)


    #Method for setting up weather GUI parameters
    def GUI_weather_parameters(self):
        #Setting up country/city result label
        self.country_result_label.setGeometry(0, 165, 800, 100)
        self.country_result_label.setAlignment(Qt.AlignCenter)
        self.country_result_label.setStyleSheet("background-color: transparent;"
                                                "font-size: 70px;"
                                                "font-weight: bold;")

        #Setting up weather icon result label
        self.icon_result_label.setGeometry(115, 250, 150, 150)
        self.icon_result_label.setStyleSheet("background-color: transparent;"
                                             "font-size: 150px;")
        
        #Setting up temperature result label
        self.temperature_result_label.setGeometry(250, 260, 115, 100)
        self.temperature_result_label.setAlignment(Qt.AlignCenter)
        self.temperature_result_label.setStyleSheet("background-color: transparent;"
                                                    "font-size: 67px;")
        
        #Setting up degree converter button
        self.degree_button.setGeometry(350, 285, 75, 30)
        self.degree_button.setStyleSheet("""QPushButton 
                                            {
                                                font-size: 30px;
                                                background-color: transparent;
                                            }
                                            QPushButton:hover 
                                            {
                                                color: #ffffff;
                                            }
                                         """)
        self.degree_button.clicked.connect(self.unit_conversion_fer_to_deg)
        
        #Setting up fahrenheit converter button
        self.fahrenheit_button.setGeometry(387, 285, 75, 30)
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
        self.fahrenheit_button.clicked.connect(self.unit_conversion_deg_to_fer)

        #Setting up precipitation, wind speed and pressure result label
        self.precipitation_label.setGeometry(480, 285, 180, 80)
        self.precipitation_label.setStyleSheet("background-color: transparent;"
                                               "font-size: 18px;"
                                               "color: rgba(255, 255, 255, 180);")
        self.precipitation_label.setToolTip("The values for precipitation in %, \nwind speed in kilometers per hour \nand pressure in hecto-pascals")
        
        #Setting weather condition description label 
        self.weather_description_label.setGeometry(50, 390, 280, 45)
        self.weather_description_label.setAlignment(Qt.AlignCenter)
        self.weather_description_label.setStyleSheet("background-color: transparent;"
                                                     "font-size: 18px;"
                                                     "font-weight: bold;")
        

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
            self.display_weekly_weather(weather_data_json)

        #This catches HTTP errors returned by the API
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("400 BAD REQUEST: Invalid request format or parameters.")
                case 401:
                    self.display_error("401 UNAUTHORIZED: API key or account problem.")
                case 404:
                    self.display_error("404 NOT FOUND: Endpoint does not exist.")
                case 429:
                    self.display_error("429 TOO MANY REQUESTS: Rate limit exceeded.")
                case 500:
                    self.display_error("500 INTERNAL SERVER ERROR: Server problem.")
                case _:
                    self.display_error(f"HTTP error occurred: {response.status_code}")

        #This catches network errors
        except requests.exceptions.ConnectionError:
            self.display_error("Network or connection error occurred.")
        #This catches timeout errors
        except requests.exceptions.Timeout:
            self.display_error("The request timed out.")
        #This catches URL errors
        except requests.exceptions.TooManyRedirects:
            self.display_error("URL error, too many or wrong redirects.")
        #This catches any other errors
        except requests.exceptions.RequestException as e:
            self.display_error(f"Other error occurred:{e}")


    #Method for displaying error messages
    def display_error(self, error_message):
        self.error_message.setText(error_message)
        self.error_message.exec_()
        self.weather_description_label.clear()
        self.icon_result_label.clear()
        self.country_result_label.setText("City Weather")
        self.temperature_result_label.clear()
        self.precipitation_label.setText(f"Precipitation: 0% \nWind Speed: 0 km/h \nPressure: 0 hPa")


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
        self.country_result_label.setText(weather_data_json['resolvedAddress'].split(",")[0])

        self.temperature_result_label.setText(f"{weather_data_json['days'][0]['temp']:.0f}")

        self.precipitation_label.setText(f"Precipitation: {weather_data_json['days'][0]['precip']:.0f} % \nWind Speed: {weather_data_json['days'][0]['windspeed']:.0f} km/h \nPressure: {weather_data_json['days'][0]['pressure']:.0f} hPa")

        self.weather_description_label.setText(weather_data_json['days'][0]['conditions'])

        Pixmap_icon_address = QPixmap(self.weather_icon(weather_data_json['days'][0]['icon']))
        self.icon_result_label.setScaledContents(True) 
        self.icon_result_label.setPixmap(Pixmap_icon_address)

    
    #Method for returning weather icon path based on weather ID from API
    def weather_icon(self, weather_ID):
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


    #Method for returning the weekday based on date
    def weather_weekday(self, day_date):
        match datetime.strptime(day_date, "%Y-%m-%d").weekday():
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


    #Method for providing weekly weather information
    def display_weekly_weather(self, weather_data_json):                
        #Way to remove and clear old weekly widget data before adding new data
        old_Widget = self.findChild(QWidget, "seven_day_weather_widget")
        if old_Widget is not None:
            old_Widget.deleteLater()


        seven_day_weather_layout = QHBoxLayout()
        seven_day_weather_layout.setAlignment(Qt.AlignCenter)
        seven_day_weather_layout.setSpacing(10)

        seven_day_weather_widget = QWidget(self)
        seven_day_weather_widget.setGeometry(0, 445, 800, 140)
        seven_day_weather_widget.setStyleSheet("background-color: transparent;")

        #Adding each day's weather data to the weekly weather layout
        for i in range(7):
            weekday = "Today" if i == 0 else self.weather_weekday(weather_data_json['days'][i]['datetime'])

            self.welcome_label.setText("7-Day Weather Forecast")
            min_temp = f"{weather_data_json['days'][i]['tempmin']:.0f}"
            max_temp = f"{weather_data_json['days'][i]['tempmax']:.0f}"
            weather_icon = QPixmap(self.weather_icon(weather_data_json['days'][i]['icon']))
            weather_icon_address = weather_icon.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            each_day_frame = self.parameters_of_GUI_weekly_weather(weekday, min_temp, max_temp, weather_icon_address, i)
            seven_day_weather_layout.addWidget(each_day_frame)

        seven_day_weather_widget.setLayout(seven_day_weather_layout)
        seven_day_weather_widget.show()
        seven_day_weather_widget.setObjectName("seven_day_weather_widget")


    #Method for setting up GUI parameters for weekly weather display
    def parameters_of_GUI_weekly_weather(self, weekday, min_temp, max_temp, weather_icon_address, index):
        frame = QFrame()
        frame.setStyleSheet("background-color: #4f4f4f;;"
                            "border-radius: 15px;")
        frame.setFixedSize(105, 125)

        each_day_layout = QVBoxLayout()
        each_day_layout.setAlignment(Qt.AlignCenter)

        #Constructing and Setting weekday label
        weekday_label = QLabel(weekday)
        weekday_label.setAlignment(Qt.AlignCenter)
        weekday_label.setStyleSheet("font-size: 16px;" 
                                    "color: white;" 
                                    "background-color: transparent;")
        each_day_layout.addWidget(weekday_label)

        #Constructing and Setting weather icon label
        weather_icon_label = QLabel()
        weather_icon_label.setPixmap(weather_icon_address)
        weather_icon_label.setAlignment(Qt.AlignCenter)
        weather_icon_label.setStyleSheet("background-color: transparent;")
        weather_icon_label.setScaledContents(True)
        each_day_layout.addWidget(weather_icon_label)

        #Constructing and Setting min and max temperature label
        temp_label = QLabel(f"{min_temp}°C | {max_temp}°C")
        temp_label.setObjectName(f"temp_label_{index}")
        temp_label.setProperty("min_temp", int(min_temp))
        temp_label.setProperty("max_temp", int(max_temp))
        temp_label.setAlignment(Qt.AlignCenter)
        temp_label.setStyleSheet("font-size: 14px;" 
                                 "color: white;"
                                 "background-color: transparent;")
        each_day_layout.addWidget(temp_label)

        frame.setLayout(each_day_layout)
        return frame

    
#Main if statement 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainAppWindow()
    main_window.show()
    sys.exit(app.exec_())