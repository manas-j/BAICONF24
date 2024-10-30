# experiments/esg_resilience_analysis.py

import pandas as pd
import yaml
import seaborn as sns
import matplotlib.pyplot as plt
from utils.data_processing import load_and_process_data
from utils.model_utils import resilience_regression
from utils.visualization import plot_shock_visualizations

def main():
    # Load configuration
    with open('../configs/esg_resilience_analysis_config.yaml') as config_file:
        config = yaml.safe_load(config_file)

    # Load and process data
    data = pd.read_csv(config['file_path'])
    esg_columns = config['esg_columns']
    financial_columns = config['financial_columns']
    shock_levels = config['shock_levels']

    # Apply resilience regression across all combinations of ESG components, financial metrics, and shocks
    results = []
    for esg in esg_columns:
        for metric in financial_columns:
            for shock in shock_levels:
                coef, intercept = resilience_regression(data, esg, metric, shock)
                
                # Skip if regression couldn't be performed
                if coef is None or intercept is None:
                    print(f"Skipping {esg} vs {metric} under {shock*100}% shock (insufficient data).")
                    continue
                
                results.append({
                    'ESG Component': esg,
                    'Financial Metric': metric,
                    'Shock Level': shock,
                    'Coefficient': coef,
                    'Intercept': intercept
                })

    # Convert results to DataFrame for analysis and visualization
    results_df = pd.DataFrame(results)

    # Visualize regression coefficients and intercepts
    plot_shock_visualizations(results_df)

if __name__ == "__main__":
    main()
