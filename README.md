# IoT Sensor Data Logger with Predictive Analytics Dashboard

A complete **pure software IoT project** that simulates multiple sensors, logs real-time data, detects anomalies, and provides predictive insights using Machine Learning.

This project demonstrates end-to-end IoT data pipeline skills — from data generation to visualization and intelligent analytics.

## 🚀 Project Features

- Simulation of 5 IoT sensors (Temperature, Humidity, Soil Moisture, Light Intensity, Air Quality)
- Data logging into SQLite database
- Real-time interactive web dashboard built with Streamlit
- Anomaly detection using **Isolation Forest** (Machine Learning)
- Future value prediction using **Linear Regression**
- Beautiful interactive visualizations with Plotly
- Responsive filters and summary statistics

## 🛠️ Technologies Used

- **Python 3**
- **Streamlit** – Interactive Dashboard
- **Pandas & NumPy** – Data Processing
- **Scikit-learn** – Machine Learning (Anomaly Detection & Prediction)
- **Plotly** – Interactive Charts
- **SQLite** – Local Database

## 📁 Project Structure
iot-data-logger/
├── app.py                    # Main Streamlit Dashboard
├── data_generator.py         # Generates simulated sensor data
├── data_logger.py            # Handles data logging to SQLite
├── model_detection.py        # ML functions (Anomaly + Prediction)
├── requirements.txt
├── README.md
└── data/                     # Generated CSV files (optional)


## 🏃 How to Run the Project

1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd iot-data-logger

2. Create and activate virtual environment (Recommended):
   Bash
   python -m venv venv
   venv\Scripts\Activate.ps1     # Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Generate sample sensor data:
   python data_generator.py

5. Run the dashboard:
   streamlit run app.py

  ## 📊 What You Will See

- Live line charts for each sensor
- Anomaly highlights (sudden spikes or drops)
- Next 5 readings prediction
- Summary statistics (Average, Max, Min)
- Easy sensor selection from sidebar

## 🎯 Key Learnings
- Building end-to-end IoT data pipeline in pure software
- Working with time-series sensor data
- Implementing Machine Learning on IoT data (Anomaly Detection + Prediction)
- Creating professional interactive dashboards using Streamlit
- Data logging and database management with SQLite