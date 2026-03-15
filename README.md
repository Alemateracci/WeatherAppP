# 🌦️ Weather Application (Python)

A modern, extensible **Python weather application** built on top of the **Visual Crossing Weather API**.  
The app provides real-time and forecast weather data for any location, with support for **temperature unit switching**, and planned features such as **user accounts**, **saved locations**, **local per-device storage**, and **cloud persistence using AWS**.

This project is designed to start simple while scaling into a cloud-backed, multi-device application.

---

## ✨ Features

### ✅ Current Functionality
- 🌍 Retrieve weather data for a specific location
- ⏱️ Real-time and forecast weather information
- 🌡️ **Temperature unit switching (Celsius ↔ Fahrenheit)**
- 🔌 Powered by the **Visual Crossing Weather API**
- 🐍 Built entirely in **Python**
- Deployed for MacOS in .dmg file

---

## 🏗️ Architecture Overview

The application is designed with flexibility and scalability in mind:

- **Weather Data Layer**
  - Visual Crossing Weather API
- **Application Logic**
  - Python services for fetching, parsing, and processing data
- **Persistence Options**
  - Local database (per device)
  - Cloud database (AWS)
- **User Layer**
  - Accounts
  - Saved locations
  - Device-specific preferences

---

## ☁️ AWS Integration (Planned)

The cloud layer will be implemented using AWS services, such as:

- **Amazon RDS or DynamoDB** – user accounts and saved locations
- **AWS IAM / Cognito** – authentication and access control
- **AWS EC2 / Lambda** – backend services if required

This allows secure data storage, scalability, and synchronization across multiple devices.

---

## 🧰 Tech Stack

- **Language:** Python 🐍
- **Weather API:** Visual Crossing Weather API
- **Cloud Provider:** AWS (planned)
- **Databases:**
  - Local: SQLite (or equivalent)
  - Cloud: AWS RDS or DynamoDB

---

## 🛣️ Roadmap

- [x] Basic weather data retrieval
- [x] Temperature unit switching (°C / °F)
- [x] Deployment
- [x] UI and UX improvements
