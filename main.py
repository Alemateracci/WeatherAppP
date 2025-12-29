import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt

class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Setting up main window
        self.setWindowTitle("Weather Application")
        self.setGeometry(450, 200, 700, 600)
        self.setStyleSheet("background-color: #242424;")

        #Setting up welcome message
        self.welcome_label = QLabel("Welcome to Weather \nApplication!", self)
        self.welcome_label.setGeometry(0, 5, 700, 90)
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setStyleSheet("font-size: 40px;" 
                                         "font-weight: bold;"
                                         "color: white;")
        
        #Setting search text box
        self.search_input = QLineEdit(self)
        self.search_input.setAlignment(Qt.AlignLeft)
        self.search_input.setPlaceholderText('Enter the city and country (e.g. "London, UK")')
        self.search_input.setGeometry(240, 118, 500, 50)
        self.search_input.setStyleSheet("font-size: 20px;"
                                        "border: none")

        #Setting search button
        self.search_button = QPushButton("Get Weather", self)
        self.search_button.setGeometry(70, 123, 150, 40)
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

        #Setting search result background
        self.search_result_backgroundC_label = QLabel(self)
        self.search_result_backgroundC_label.setGeometry(0, 170, 700, 430)
        self.search_result_backgroundC_label.setStyleSheet("background-color: #303030;")

        #Setting up result label
        self.country_result_label = QLabel("Niggeria", self)
        self.country_result_label.setGeometry(0, 165, 700, 100)
        self.country_result_label.setAlignment(Qt.AlignCenter)
        self.country_result_label.setStyleSheet("background-color: transparent;"
                                                "font-size: 70px;"
                                                "font-weight: bold;")

        #Setting up result icon label
        self.icon_result_label = QLabel(self)
        self.icon_result_label.setGeometry(70, 275, 100, 100)
        self.icon_result_label.setStyleSheet("background-color: transparent;"
                                             "font-size: 95px;")
        
        #Setting up temperature result label
        self.temperature_result_label = QLabel(self)
        self.temperature_result_label.setGeometry(200, 260, 200, 100)
        self.temperature_result_label.setStyleSheet("background-color: transparent;"
                                                  "font-size: 63px;")
        
        #Setting up degree converter button
        self.degree_button = QPushButton("°C/", self)
        self.degree_button.setGeometry(270, 285, 75, 30)
        self.degree_button.setStyleSheet("""QPushButton 
                                            {
                                                font-size: 30px;
                                                background-color: transparent;
                                            }
                                            QPushButton:hover 
                                            {
                                                color: #9e9d9d;
                                            }
                                         """)
        
        #Setting up fahrenheit converter button
        self.fahrenheit_button = QPushButton("°F", self)
        self.fahrenheit_button.setGeometry(307, 285, 75, 30)
        self.fahrenheit_button.setStyleSheet("""QPushButton 
                                                {
                                                    font-size: 30px;
                                                    background-color: transparent;
                                                    color: #9e9d9d
                                                }
                                                QPushButton:hover 
                                                {
                                                    color: #9e9d9d;
                                                }
                                             """)

        #Setting up precipitation, wind speed and pressure result label
        self.precipitation_label = QLabel(f"Precipitation: 100% \nWind Speed: 100 km/h \nPressure: 1000 hPa", self)
        self.precipitation_label.setGeometry(410, 285, 180, 80)
        self.precipitation_label.setStyleSheet("background-color: transparent;"
                                               "font-size: 18px;"
                                               "color: rgba(255, 255, 255, 180);")
        
        #Creating an error message box
        self.error_message = QMessageBox()
        self.error_message.setIcon(QMessageBox.Critical)
        self.error_message.setWindowFlags(Qt.FramelessWindowHint)

        
    #Method for retrieving weather information 
    def get_weather_info(self):
        key_weatherAPI = "JRXUF5NDH62ELPGPETM5R3AEB"
        city_Input = self.search_input.text()
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_Input}?key={key_weatherAPI}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data_json = response.json()
            self.display_weather(weather_data_json)

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


    def unit_conversion(self):
        pass


    def display_weather(self, weather_data_json):
        pass


#Main if statement 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainAppWindow()
    main_window.show()
    sys.exit(app.exec_())