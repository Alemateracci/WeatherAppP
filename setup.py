from setuptools import setup

APP = ['main.py']  # Your main Python script
DATA_FILES = ['WeeklyGUI.py', 'GetWeatherData.py', 'MainGUI.py', 'ErrorFunction.py', 'WeatherUtils.py', 'UnitConversion.py', 'WeatherIcons', 'Informative']  # Folders with extra files
OPTIONS = {
    'argv_emulation': True,      # Makes command-line arguments work
    'iconfile': 'Informative/applogo.jpg', # Optional: your app icon
    'packages': [],              # Add extra packages if needed
    'plist': {
        'CFBundleName': 'PythonWeatherApp',   # App name
        'CFBundleVersion': '1.0',
        'CFBundleShortVersionString': '1.0',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)