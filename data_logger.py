import pandas as pd
import sqlite3
from datetime import datetime

def log_data(df, db_name='iot_data.db'):
    conn = sqlite3.connect(db_name)
    # Create table if it doesn't exist
    df.to_sql('sensor_readings', conn, if_exists='append', index=False)
    conn.close()
    print(f"Data logged successfully to {db_name}")

def load_data(db_name='iot_data.db'):
    conn = sqlite3.connect(db_name)
    # Create table with proper schema if it doesn't exist (prevents error)
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS sensor_readings (
        timestamp TEXT,
        temperature REAL,
        humidity REAL,
        soil_moisture REAL,
        light_intensity REAL,
        air_quality REAL,
        anomaly INTEGER DEFAULT 0
    )
    '''
    conn.execute(create_table_query)
    
    df = pd.read_sql('SELECT * FROM sensor_readings', conn)
    if not df.empty:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    conn.close()
    return df