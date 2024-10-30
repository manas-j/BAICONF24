# experiments/esg_financial_analysis.py

import yaml
from utils.data_processing import load_and_process_data
from utils.visualization import plot_correlation_heatmap, plot_pairwise_correlation, plot_scatterplot_matrix, plot_boxplots, plot_distributions
from utils.model_utils import statistical_significance_test, regression_analysis

def main():
    # Load configuration
    with open('../configs/esg_financial_analysis_config.yaml') as config_file:
        config = yaml.safe_load(config_file)

    # Load and process data
    data = load_and_process_data(config['file_path'], config['esg_columns'], config['financial_columns'])

    # Visualization: Correlation Heatmap
    plot_correlation_heatmap(data)

    # Pairwise Correlation Analysis
    plot_pairwise_correlation(data, config['esg_columns'], config['financial_columns'])

    # Statistical Significance Test
    statistical_significance_test(data, config['esg_columns'], config['financial_columns'])

    # Regression Analysis
    for esg in config['esg_columns']:
        for metric in config['financial_columns']:
            regression_analysis(data, esg, metric)

    # Scatterplot Matrix
    plot_scatterplot_matrix(data, config['selected_columns'])

    # Boxplots
    plot_boxplots(data, config['esg_columns'] + config['financial_columns'])

    # Distribution Analysis
    plot_distributions(data, config['esg_columns'] + config['financial_columns'])

if __name__ == "__main__":
    main()
