from model import detect_anomalies, preprocess_data, train_model
import pandas as pd

def generate_report(data):
    # Preprocess data for the model, which now includes 'user_id'
    processed_data = preprocess_data(data)
    
    # Train Isolation Forest model
    model = train_model(processed_data)
    
    # Predict anomalies for processed data
    predictions = model.predict(processed_data.drop(columns=['user_id']))
    
    # Calculate anomaly scores for the entire dataset without modifying processed_data directly
    anomaly_scores = model.decision_function(processed_data.drop(columns=['user_id']))
    
    # Filter anomalies based on predictions
    anomalies = processed_data[predictions == -1].copy()  # Copy to avoid SettingWithCopyWarning
    anomalies['anomaly_score'] = anomaly_scores[predictions == -1]
    
    # Save the report to an HTML file for easier reading
    html_report = anomalies.to_html(index=False)
    with open("anomaly_report.html", "w") as file:
        file.write("<h1>Anomaly Detection Report</h1>")
        file.write(html_report)
    
    return anomalies

def print_report(report):
    print("Anomaly report saved to 'anomaly_report.html'")
