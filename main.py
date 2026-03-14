import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainGUI import GUI_main_parameters, GUI_weather_parameters

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

#Main if statement 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainAppWindow()
    main_window.show()
    sys.exit(app.exec_())