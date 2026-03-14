from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from utilities import weather_icon, weather_weekday


#Method for displaying weekly weather information in the GUI
def display_weekly_weather(self, weather_data_json):
    # Way to remove and clear old weekly widget data before adding new data
    old_Widget = self.findChild(QWidget, "seven_day_weather_widget")
    if old_Widget is not None:
        old_Widget.deleteLater()

    self.seven_day_weather_layout = QHBoxLayout()
    self.seven_day_weather_layout.setAlignment(Qt.AlignCenter)
    self.seven_day_weather_layout.setSpacing(10)

    self.seven_day_weather_widget = QWidget(self)
    self.seven_day_weather_widget.setGeometry(0, 445, 800, 140)
    self.seven_day_weather_widget.setStyleSheet("background-color: transparent;")

    for i in range(7):
        weekday = "Today" if i == 0 else weather_weekday(weather_data_json['days'][i]['datetime'])

        self.welcome_label.setText("7-Day Weather Forecast")
        min_temp = f"{weather_data_json['days'][i]['tempmin']:.0f}"
        max_temp = f"{weather_data_json['days'][i]['tempmax']:.0f}"
        icon_pixmap = QPixmap(weather_icon(weather_data_json['days'][i]['icon']))
        weather_icon_address = icon_pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        each_day_frame = parameters_of_GUI_weekly_weather(self, weekday, min_temp, max_temp, weather_icon_address, i)
        self.seven_day_weather_layout.addWidget(each_day_frame)

    self.seven_day_weather_widget.setLayout(self.seven_day_weather_layout)
    self.seven_day_weather_widget.show()
    self.seven_day_weather_widget.setObjectName("seven_day_weather_widget")


#Method for setting up weekly weather GUI parameters
def parameters_of_GUI_weekly_weather(self, weekday, min_temp, max_temp, weather_icon_address, index):
    frame = QFrame()
    frame.setStyleSheet("background-color: #4f4f4f;;"
                        "border-radius: 15px;")
    frame.setFixedSize(105, 125)

    self.each_day_layout = QVBoxLayout()
    self.each_day_layout.setAlignment(Qt.AlignCenter)

    self.weekday_label = QLabel(weekday)
    self.weekday_label.setAlignment(Qt.AlignCenter)
    self.weekday_label.setStyleSheet("font-size: 16px;"
                                    "color: white;"
                                    "background-color: transparent;")
    self.each_day_layout.addWidget(self.weekday_label)

    self.weather_icon_label = QLabel()
    self.weather_icon_label.setPixmap(weather_icon_address)
    self.weather_icon_label.setAlignment(Qt.AlignCenter)
    self.weather_icon_label.setStyleSheet("background-color: transparent;")
    self.weather_icon_label.setScaledContents(True)
    self.each_day_layout.addWidget(self.weather_icon_label)

    self.temp_label = QLabel(f"{min_temp}°C | {max_temp}°C")
    self.temp_label.setObjectName(f"temp_label_{index}")
    self.temp_label.setProperty("min_temp", int(min_temp))
    self.temp_label.setProperty("max_temp", int(max_temp))
    self.temp_label.setAlignment(Qt.AlignCenter)
    self.temp_label.setStyleSheet("font-size: 14px;"
                                 "color: white;"
                                 "background-color: transparent;")
    self.each_day_layout.addWidget(self.temp_label)

    frame.setLayout(self.each_day_layout)
    return frame
