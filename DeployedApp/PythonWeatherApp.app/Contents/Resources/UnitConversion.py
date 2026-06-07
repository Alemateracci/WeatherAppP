from PyQt5.QtWidgets import QLabel

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
        return

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
        return

    self.temperature_result_label.setText(f"{(int(self.temperature_result_label.text()) - 32) * 5/9:.0f}")
    for i in range(7):
        temp_label = self.findChild(QLabel, f"temp_label_{i}")
        min_temp = temp_label.property('min_temp')
        max_temp = temp_label.property('max_temp')
        temp_label.setText(f"{int(min_temp)}°C | {int(max_temp)}°C")
    self.degree_button.setDisabled(True)
