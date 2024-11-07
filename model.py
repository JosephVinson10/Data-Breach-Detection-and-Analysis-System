import pandas as pd
from sklearn.ensemble import IsolationForest

def preprocess_data(data):
    # Extract hour from timestamp for off-hour detection
    data['hour'] = data['timestamp'].dt.hour
    
    # Aggregate login data by user and retain user_id as index for reference
    user_stats = data.groupby('user_id').agg(
        total_logins=('login_result', 'count'),
        failed_logins=('login_result', lambda x: (x == 'Failure').sum()),
        avg_login_hour=('hour', 'mean')
    ).reset_index()  # Reset index to make 'user_id' a column

    # Calculate additional features
    user_stats['failure_rate'] = user_stats['failed_logins'] / user_stats['total_logins']
    return user_stats[['user_id', 'total_logins', 'failed_logins', 'avg_login_hour', 'failure_rate']]

def train_model(data):
    # Drop 'user_id' column as it's not used for training
    features = data.drop(columns=['user_id'])
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(features)
    return model

def detect_anomalies(model, data):
    # Drop 'user_id' before predicting
    features = data.drop(columns=['user_id'])
    predictions = model.predict(features)
    # Filter anomalies (-1 = anomaly)
    anomalies = data[predictions == -1].copy()
    return anomalies
