# 🌦️ Weather Application (Python)

A desktop **weather application** built with **Python** and **PyQt5**, powered by the **Visual Crossing Weather API**.  
Search any city or country to see the current conditions and a 7-day forecast, with the ability to switch between Celsius and Fahrenheit at a click.

---

## ✨ Features

- 🔍 **Search by city and/or country** (e.g. "London, UK") via a text input and "Get Weather" button
- 🌡️ **Current conditions**: location name, temperature, weather condition description and icon
- 💧 **Additional details**: precipitation (%), wind speed (km/h) and pressure (hPa)
- 📅 **7-day forecast**: weekday, min/max temperature and weather icon for each of the next 7 days
- 🔄 **Temperature unit switching (°C ↔ °F)**, applied instantly to both the current and weekly forecasts
- 🖼️ **Custom weather icons** for conditions such as snow, rain, fog, wind, cloudy, partly cloudy (day/night) and clear (day/night)
- ⚠️ **Error handling** with on-screen dialogs for empty input, HTTP errors (400/401/404/429/500), connection issues, timeouts and too-many-redirects
- 🎨 Dark-themed custom GUI built with **PyQt5**
- 🔌 Powered by the **Visual Crossing Weather API**, with the API key loaded securely from a local `.env` file
- 🍎 Packaged as a standalone **macOS app** (`.app`) and **`.dmg` installer** using `py2app`

---

## 🏗️ Architecture Overview

- **`main.py`** — Application entry point; creates the main window and assembles the GUI
- **`MainGUI.py`** — Builds the main window layout (search bar, current weather display, unit toggle buttons) and renders the current weather
- **`WeeklyGUI.py`** — Builds and renders the 7-day forecast widget
- **`GetWeatherData.py`** — Fetches data from the Visual Crossing Weather API and routes errors to the error handler
- **`UnitConversion.py`** — Converts and re-renders displayed temperatures between Celsius and Fahrenheit
- **`WeatherUtils.py`** — Maps API condition codes to icon files and API dates to weekday names
- **`ErrorFunction.py`** — Displays error dialogs and resets the UI to a clean state
- **`WeatherIcons/`** — Weather condition icon assets
- **`Informative/`** — App icon and `.env` file holding the API key (not committed)

---

## 🧰 Tech Stack

- **Language:** Python 🐍
- **GUI:** PyQt5
- **HTTP requests:** `requests`
- **Configuration:** `python-dotenv`
- **Weather API:** Visual Crossing Weather API
- **Packaging:** `py2app` (macOS `.app` / `.dmg`)

---

## 📦 Deployment

The app is packaged for macOS using `py2app` (see [`setup.py`](setup.py)) into a `PythonWeatherApp.app` bundle and a `WeatherAppInstaller.dmg` installer.

> **Note:** The built `.dmg` installer is **not included in this repository** — at over 100 MB, it was too large to be sent/uploaded. It is excluded via [`.gitignore`](.gitignore) along with the `build/` directory.

---

## 🛣️ Roadmap

- [x] Basic weather data retrieval
- [x] 7-day forecast
- [x] Temperature unit switching (°C / °F)
- [x] Error handling
- [x] macOS deployment (`.app` / `.dmg`)
- [x] UI and UX improvements
