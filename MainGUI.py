from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from UnitConversion import unit_conversion_deg_to_fer, unit_conversion_fer_to_deg
from PyQt5.QtGui import QPixmap
from WeatherUtils import weather_icon
from GetWeatherData import get_weather_info

#Method for setting up main GUI parameters
def GUI_main_parameters(self):
    #Setting up welcome message label
    self.welcome_label = QLabel("Welcome to Weather \nApplication!", self)
    self.welcome_label.setGeometry(0, 5, 800, 90)
    self.welcome_label.setAlignment(Qt.AlignCenter)
    self.welcome_label.setStyleSheet("font-size: 40px;" 
                                       "font-weight: bold;"
                                       "color: white;")
    
    #Setting search text box
    self.search_input = QLineEdit(self)
    self.search_input.setAlignment(Qt.AlignLeft)
    self.search_input.returnPressed.connect(lambda: get_weather_info(self))
    self.search_input.setPlaceholderText('Enter the city and/or country (e.g. "London, UK")')
    self.search_input.setGeometry(270, 118, 550, 50)
    self.search_input.setStyleSheet("font-size: 20px;"
                                      "border: none")
    
    #Setting search button
    self.search_button = QPushButton("Get Weather", self)
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
    self.search_button.clicked.connect((lambda: get_weather_info(self)))

    #Setting search result background label
    self.search_result_backgroundC_label = QLabel(self)
    self.search_result_backgroundC_label.setGeometry(0, 170, 800, 450)
    self.search_result_backgroundC_label.setStyleSheet("background-color: #303030;"
                                                         "border-radius: 25px;")


#Method for setting up weather GUI parameters
def GUI_weather_parameters(self):
    #Setting up country/city result label
    self.country_result_label = QLabel("City Weather", self)
    self.country_result_label.setGeometry(0, 165, 800, 100)
    self.country_result_label.setAlignment(Qt.AlignCenter)
    self.country_result_label.setStyleSheet("background-color: transparent;"
                                            "font-size: 70px;"
                                            "font-weight: bold;")

    #Setting up weather icon result label
    self.icon_result_label = QLabel(self)
    self.icon_result_label.setGeometry(115, 250, 150, 150)
    self.icon_result_label.setStyleSheet("background-color: transparent;"
                                            "font-size: 150px;")
    
    #Setting up temperature result label
    self.temperature_result_label = QLabel(self)
    self.temperature_result_label.setGeometry(250, 260, 115, 100)
    self.temperature_result_label.setAlignment(Qt.AlignCenter)
    self.temperature_result_label.setStyleSheet("background-color: transparent;"
                                                "font-size: 67px;")
    
    #Setting up degree converter button
    self.degree_button = QPushButton("°C/", self)
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
    self.degree_button.clicked.connect(lambda: unit_conversion_fer_to_deg(self))
    
    #Setting up fahrenheit converter button
    self.fahrenheit_button = QPushButton("°F", self)
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
    self.fahrenheit_button.clicked.connect(lambda: unit_conversion_deg_to_fer(self))

    #Setting up precipitation, wind speed and pressure result label
    self.precipitation_label = QLabel(f"Precipitation: 0% \nWind Speed: 0 km/h \nPressure: 0 hPa", self)
    self.precipitation_label.setGeometry(480, 285, 180, 80)
    self.precipitation_label.setStyleSheet("background-color: transparent;"
                                            "font-size: 18px;"
                                            "color: rgba(255, 255, 255, 180);")
    self.precipitation_label.setToolTip("The values for precipitation in %, \nwind speed in kilometers per hour \nand pressure in hecto-pascals")
    
    #Setting weather condition description label 
    self.weather_description_label = QLabel(self)
    self.weather_description_label.setGeometry(50, 390, 280, 45)
    self.weather_description_label.setAlignment(Qt.AlignCenter)
    self.weather_description_label.setStyleSheet("background-color: transparent;"
                                                    "font-size: 18px;"
                                                    "font-weight: bold;")


#Method for displaying weather info from API response
def display_weather(self, weather_data_json):
    self.country_result_label.setText((weather_data_json['resolvedAddress'].split(",")[0]).capitalize())
    self.temperature_result_label.setText(f"{weather_data_json['days'][0]['temp']:.0f}")
    self.precipitation_label.setText(
        f"Precipitation: {weather_data_json['days'][0]['precip']:.0f} % \nWind Speed: {weather_data_json['days'][0]['windspeed']:.0f} km/h \nPressure: {weather_data_json['days'][0]['pressure']:.0f} hPa"
    )
    self.weather_description_label.setText(weather_data_json['days'][0]['conditions'])

    Pixmap_icon_address = QPixmap(weather_icon(weather_data_json['days'][0]['icon']))
    self.icon_result_label.setScaledContents(True)
    self.icon_result_label.setPixmap(Pixmap_icon_address)
