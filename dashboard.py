import streamlit as st
from data_generator import generate_data
from report_generator import generate_report
from visualizations import create_failed_login_heatmap, create_anomalies_bar_plot

def main():
    st.title("Data Breach Detection Dashboard")

    # Generate and process data
    login_data = generate_data()
    anomalies = generate_report(login_data)

    # Display visuals on the dashboard
    st.header("Anomaly Detection Visualizations")

    # Heatmap of failed login attempts
    st.subheader("Failed Login Attempts Heatmap")
    heatmap_fig = create_failed_login_heatmap(login_data)
    st.pyplot(heatmap_fig)
    st.markdown("""
        **Description**: This heatmap shows the density of failed login attempts by user and IP address.
        Each cell represents the number of failed login attempts from a particular IP for each user. Darker colors indicate a higher
        number of failed attempts, which may indicate suspicious activity or potential brute-force attacks.
    """)

    # Bar plot of detected anomalies
    st.subheader("Anomalies Detected by Isolation Forest")
    anomalies_bar_fig = create_anomalies_bar_plot(anomalies)
    st.pyplot(anomalies_bar_fig)
    st.markdown("""
        **Description**: This bar plot represents the distribution of anomaly scores detected by the Isolation Forest model.
        Higher bars indicate more frequent anomalies in certain score ranges, giving a sense of the severity and volume of
        potential security breaches. Anomalies with higher scores are more significant deviations from normal behavior.
    """)

    # Display a summary of anomalies
    st.subheader("Anomaly Detection Report Summary")
    st.write(anomalies[['user_id', 'anomaly_score']])
    st.markdown("""
        **Summary Description**: This table lists all detected anomalies, including the user ID and the anomaly score.
        The anomaly score reflects how far a login attempt deviates from normal behavior patterns, with higher scores
        representing more suspicious activities.
    """)

if __name__ == "__main__":
    main()
