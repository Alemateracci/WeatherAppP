import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Setting up main window
        self.setWindowTitle("Weather Application")
        self.setGeometry(450, 200, 700, 600)
        self.setStyleSheet("background-color: #242424;")

        #Setting up welcome message
        self.welcome_label = QLabel("Welcome to Weather Application!", self)
        self.welcome_label.setGeometry(0, 5, 700, 50)
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setStyleSheet("font-size: 40px;" 
                                         "font-weight: bold;"
                                         "color: white;")
        
        #Setting search text box
        self.search_input = QLineEdit(self)
        self.search_input.setAlignment(Qt.AlignLeft)
        self.search_input.setPlaceholderText('Enter the city and country (e.g. "London, UK")')
        self.search_input.setGeometry(240, 73, 500, 50)
        self.search_input.setStyleSheet("font-size: 20px;"
                                        "border: none")

        #Setting search button
        self.search_button = QPushButton("Get Weather", self)
        self.search_button.setGeometry(70, 78, 150, 40)
        self.search_button.setStyleSheet("font-size: 17px;"
                                         "background-color: #575757;"
                                         "border-radius: 20px;")

        #Setting search result background
        self.search_result_backgroundC_label = QLabel(self)
        self.search_result_backgroundC_label.setGeometry(0, 130, 700, 470)
        self.search_result_backgroundC_label.setStyleSheet("background-color: #303030;")

        #Setting up result label
        self.country_result_label = QLabel("Nigeria, Africa", self)
        self.country_result_label.setGeometry(0, 130, 700, 100)
        self.country_result_label.setAlignment(Qt.AlignCenter)
        self.country_result_label.setStyleSheet("background-color: transparent;"
                                                "font-size: 70px;"
                                                "font-family: Segoe UI;"
                                                "font-weight: bold;")

        #Setting up result icon label
        self.icon_result_label = QLabel("🌙", self)
        self.icon_result_label.setGeometry(70, 250, 100, 100)
        self.icon_result_label.setStyleSheet("background-color: transparent;"
                                             "font-size: 95px;")
        
        #Setting up temperature result label
        self.temperature_result_label = QLabel("55", self)
        self.temperature_result_label.setGeometry(190, 240, 200, 100)
        self.temperature_result_label.setStyleSheet("background-color: transparent;"
                                                  "font-size: 63px;")
        
        #Setting up unit converter button
        self.degree_button = QPushButton("°C/°F", self)
        self.degree_button.setGeometry(270, 265, 75, 30)
        self.degree_button.setStyleSheet("font-size: 30px;"
                                          "background-color: transparent;")

        #Setting up precipitation, wind speed and pressure result label
        self.precipitation_label = QLabel(f"Precipitation: 100% \nWind Speed: 100 km/h \nPressure: 1000 hPa", self)
        self.precipitation_label.setGeometry(390, 260, 180, 80)
        self.precipitation_label.setStyleSheet("background-color: transparent;"
                                               "font-size: 18px;"
                                               "color: rgb(255, 255, 255, 180);")


#Main if statement 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainAppWindow()
    main_window.show()
    sys.exit(app.exec_())