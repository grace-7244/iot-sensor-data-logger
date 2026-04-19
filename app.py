import streamlit as st
import pandas as pd
import plotly.express as px

# Updated imports (because you renamed the file)
from data_logger import load_data
from model_detection import detect_anomalies, predict_next_value   # ← Changed here

st.title("📊 IoT Sensor Data Logger & Predictive Analytics Dashboard")

# Load data
df = load_data()

if df.empty:
    st.warning("No data available. Please run data_generator.py first to generate sample data.")
    st.stop()

# Sidebar filters
st.sidebar.header("Filters")
sensor_options = ['temperature', 'humidity', 'soil_moisture', 'light_intensity', 'air_quality']
selected_sensor = st.sidebar.selectbox("Select Sensor", sensor_options)

# Main Chart
st.subheader(f"{selected_sensor.replace('_', ' ').title()} Over Time")
fig = px.line(df, x='timestamp', y=selected_sensor, 
              title=f"{selected_sensor.replace('_', ' ').title()} Trend")
st.plotly_chart(fig, use_container_width=True)

# Anomaly Detection
st.subheader("🔍 Anomaly Detection")
df_anom = detect_anomalies(df, selected_sensor)
anomalies = df_anom[df_anom['anomaly'] == -1]

if not anomalies.empty:
    st.write(f"Found **{len(anomalies)}** anomalies in {selected_sensor}")
    st.dataframe(anomalies[['timestamp', selected_sensor, 'anomaly']])
else:
    st.success("No anomalies detected in the current data!")

# Prediction Section
st.subheader("🔮 Next 5 Readings Prediction (Linear Regression)")
try:
    preds = predict_next_value(df, selected_sensor, steps=5)
    st.line_chart(preds, use_container_width=True)
    st.caption("Simple Linear Regression based prediction")
except Exception as e:
    st.warning(f"Prediction not available yet: {e}")

# Summary Statistics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(f"Average {selected_sensor.title()}", f"{df[selected_sensor].mean():.2f}")
with col2:
    st.metric(f"Maximum {selected_sensor.title()}", f"{df[selected_sensor].max():.2f}")
with col3:
    st.metric(f"Minimum {selected_sensor.title()}", f"{df[selected_sensor].min():.2f}")