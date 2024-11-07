
# Data Breach Detection and Analysis System

This project is a data breach detection system that uses machine learning to identify potential security breaches by analyzing login attempt data. The tool detects anomalies in login behaviors, including excessive failed logins, access from unusual IPs, and logins outside business hours.

## Project Structure

- `main.py` - Entry point to run data generation, model training, and report generation.
- `data_generator.py` - Module to generate sample data.
- `model.py` - Contains functions for feature engineering, training the Isolation Forest model, and detecting anomalies.
- `report_generator.py` - Generates a summary report of detected anomalies and saves it as an HTML file.
- `visualizations.py` - Contains visualization functions for creating the heatmap of failed login attempts and a bar plot of detected anomalies.
- `dashboard.py` - Streamlit dashboard to display visualizations and the anomaly report.
- `requirements.txt` - List of required packages (pandas, matplotlib, seaborn, scikit-learn, streamlit).
- `README.md` - Project documentation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data_breach_detection.git
   cd data_breach_detection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the data generation and anomaly detection:
   ```bash
   python main.py
   ```
   This will generate an anomaly report and save it as `anomaly_report.html` in the project directory.

2. Launch the Streamlit dashboard to view visualizations:
   ```bash
   streamlit run dashboard.py
   ```

## Visualizations

- **Failed Login Attempts Heatmap**: A heatmap that shows the density of failed login attempts for each user and IP address. Darker cells indicate higher frequencies of failed logins, helping to spot accounts with suspicious activity.
- **Anomalies Detected by Isolation Forest**: A bar plot displaying the distribution of anomaly scores detected by the Isolation Forest model. Higher bars indicate more frequent anomalies for particular score ranges, helping to identify the severity and commonality of anomalies in the dataset.

The Streamlit dashboard provides these visualizations and a detailed summary of anomalies for easy monitoring of potential security risks.
