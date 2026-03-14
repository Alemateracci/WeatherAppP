from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

#Method for displaying error messages
def display_error(self, error_message):
    # Prevent additional input while the error dialog is displayed
    self.search_input.setDisabled(True)

    error_message_label = QMessageBox(self)
    error_message_label.setIcon(QMessageBox.Critical)
    error_message_label.setWindowFlags(Qt.FramelessWindowHint)
    error_message_label.setStandardButtons(QMessageBox.Ok)
    error_message_label.setWindowModality(Qt.ApplicationModal)
    error_message_label.setText(error_message)
    error_message_label.exec_()

    # Restore input focus after user dismisses the dialog
    self.search_input.setDisabled(False)
    self.search_input.setFocus()
    self.weather_description_label.clear()
    self.icon_result_label.clear()
    self.country_result_label.setText("City Weather")
    self.temperature_result_label.clear()
    self.precipitation_label.setText(f"Precipitation: 0% \nWind Speed: 0 km/h \nPressure: 0 hPa")
    self.degree_button.setEnabled(False)
    self.fahrenheit_button.setEnabled(False)
    self.seven_day_weather_widget.setVisible(False)
    self.seven_day_weather_widget.deleteLater()
    self.seven_day_weather_widget = None
    self.seven_day_weather_layout = None
