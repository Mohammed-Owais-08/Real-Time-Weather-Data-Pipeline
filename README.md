# 🌦️ Real-Time Weather Data Pipeline

## 📌 Overview
This project is a real-time data pipeline that fetches live weather data from an external API, processes it, stores it in a database, and visualizes it through a web dashboard.

The goal is to demonstrate end-to-end data engineering concepts including data extraction, transformation, storage, and visualization.

---

## 🚀 Features
- Fetches real-time weather data using REST API
- Cleans and transforms raw JSON data
- Stores structured data in SQL database
- Displays weather insights on a dynamic web dashboard
- Tracks recent search history
- Deployed for live usage

---

## 🛠️ Tech Stack
- **Programming:** Python  
- **Data Processing:** Pandas  
- **API:** OpenWeatherMap API  
- **Backend:** Flask  
- **Database:** MySQL / SQLite  
- **Deployment:** Render  
- **Other Tools:** REST APIs, JSON handling  

---

## ⚙️ ETL Pipeline Breakdown

### 1. Extract
- Fetches real-time weather data from OpenWeatherMap API  
- Uses HTTP requests to retrieve JSON data  

### 2. Transform
- Cleans and structures raw JSON data  
- Extracts key features:
  - Temperature
  - Humidity
  - Weather condition
  - City name
- Converts data into tabular format using Pandas  

### 3. Load
- Stores processed data into SQL database  
- Maintains historical records for analysis  

---

## 📊 Dashboard Features
- Displays current weather conditions  
- Shows previously searched cities  
- User-friendly interface built using Flask  
- Real-time updates  

---

## 🌐 Deployment
The project is deployed using Render for real-time accessibility.
https://real-time-weather-data-pipeline.onrender.com/
---

## 📈 Future Enhancements
- Add scheduling (Airflow / Cron jobs)
- Implement data warehousing
- Add historical trend analysis
- Integrate alert system for weather conditions
- Use Docker for containerization

---

## 💡 Key Learnings
- Building end-to-end ETL pipelines  
- Working with real-time APIs  
- Data cleaning and transformation  
- Backend development with Flask  
- Deployment of data applications  

---

## 🤝 Contribution
Feel free to fork the repo and contribute!

---

## 📧 Contact
**Mohammed Owais Siddibapa**  
- Email: mdowais0803@gmail.com  
- LinkedIn: (add your link)  
- GitHub: (add your link)
