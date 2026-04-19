import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from data_logger import log_data   # Import the logging function

def generate_sensor_data(num_records=1000):
    timestamps = [datetime.now() - timedelta(minutes=i*5) for i in range(num_records)]  # 5 min interval
    
    data = {
        'timestamp': timestamps,
        'temperature': np.random.normal(28, 3, num_records),
        'humidity': np.random.normal(60, 10, num_records),
        'soil_moisture': np.random.uniform(20, 80, num_records),
        'light_intensity': np.random.uniform(100, 1000, num_records),
        'air_quality': np.random.normal(50, 15, num_records)
    }
    
    # Add a few realistic anomalies
    anomaly_indices = random.sample(range(100, 300), 5)
    for idx in anomaly_indices:
        data['temperature'][idx] += 12
    
    df = pd.DataFrame(data)
    return df

# Main execution
if __name__ == "__main__":
    print("Generating IoT sensor data...")
    df = generate_sensor_data(800)        # Generate 800 records
    df.to_csv('data/sensor_data.csv', index=False)   # Save as CSV too
    log_data(df)                              # Log to SQLite database
    print("✅ Data generated and logged successfully!")
    print(f"Total records: {len(df)}")