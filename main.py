from data_generator import generate_data
from report_generator import generate_report, print_report
from visualizations import create_failed_login_heatmap, create_anomalies_bar_plot

def main():
    # Generate sample data
    login_data = generate_data()
    
    # Generate and display the breach report
    anomalies = generate_report(login_data)
    print_report(anomalies)
    
    # Visualize failed login attempts and anomalies
    heatmap_fig = create_failed_login_heatmap(login_data)
    anomalies_bar_fig = create_anomalies_bar_plot(anomalies)

if __name__ == "__main__":
    main()
