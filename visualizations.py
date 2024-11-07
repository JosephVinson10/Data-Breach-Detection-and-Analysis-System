import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Heatmap of failed login attempts by user
def create_failed_login_heatmap(data):
    failed_logins = data[data['login_result'] == 'Failure']
    heatmap_data = failed_logins.groupby(['user_id', 'ip_address']).size().unstack(fill_value=0)
    
    plt.figure(figsize=(12, 8))
    fig = sns.heatmap(heatmap_data, cmap="Reds", linewidths=0.1)
    plt.title("Heatmap of Failed Login Attempts by User and IP Address")
    plt.xlabel("IP Address")
    plt.ylabel("User ID")
    return fig.get_figure()

# Bar plot of anomalies detected by the model
def create_anomalies_bar_plot(anomalies):
    plt.figure(figsize=(10, 6))
    fig = anomalies['anomaly_score'].value_counts().plot(kind='bar')
    plt.title("Detected Anomalies")
    plt.xlabel("Anomaly Score")
    plt.ylabel("Count")
    return fig.get_figure()
