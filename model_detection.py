# model_detection.py
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def detect_anomalies(df, column='temperature'):
    if df.empty or len(df) < 10:
        # Return empty anomaly column if not enough data
        df = df.copy()
        df['anomaly'] = 0
        return df
    
    model = IsolationForest(contamination=0.05, random_state=42)
    df = df.copy()
    df['anomaly'] = model.fit_predict(df[[column]])
    return df

def predict_next_value(df, column='temperature', steps=5):
    if len(df) < 10:
        raise ValueError("Not enough data for prediction")
    
    df = df.copy()
    df['hour'] = df['timestamp'].dt.hour
    
    X = df[['hour']]
    y = df[column]
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict next steps
    last_hour = df['hour'].iloc[-1]
    future_hours = np.array([[ (last_hour + i) % 24 ] for i in range(1, steps+1)])
    predictions = model.predict(future_hours)
    
    return predictions