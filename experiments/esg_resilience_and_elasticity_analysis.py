# experiments/esg_resilience_and_elasticity_analysis.py

import pandas as pd
import yaml
import seaborn as sns
import matplotlib.pyplot as plt
from utils.data_processing import load_and_process_data
from utils.model_utils import resilience_regression, calculate_elasticity
from utils.visualization import plot_shock_visualizations, plot_elasticity_results

def main():
    # Load configuration
    with open('../configs/esg_resilience_analysis_config.yaml') as config_file:
        config = yaml.safe_load(config_file)

    # Load and process data
    data = pd.read_csv(config['file_path'])
    esg_columns = config['esg_columns']
    financial_columns = config['financial_columns']
    shock_levels = config['shock_levels']

    # Step 1: Resilience Analysis
    resilience_results = []
    for esg in esg_columns:
        for metric in financial_columns:
            for shock in shock_levels:
                coef, intercept = resilience_regression(data, esg, metric, shock)
                
                # Skip if regression couldn't be performed
                if coef is None or intercept is None:
                    print(f"Skipping {esg} vs {metric} under {shock*100}% shock (insufficient data).")
                    continue
                
                resilience_results.append({
                    'ESG Component': esg,
                    'Financial Metric': metric,
                    'Shock Level': shock,
                    'Coefficient': coef,
                    'Intercept': intercept
                })

    # Convert resilience results to DataFrame for analysis and visualization
    resilience_df = pd.DataFrame(resilience_results)

    # Step 2: Elasticity Analysis
    elasticity_results = []
    for esg in esg_columns:
        for metric in financial_columns:
            elasticity = calculate_elasticity(data, esg, metric)
            if elasticity is not None:
                elasticity_results.append({
                    'ESG Component': esg,
                    'Financial Metric': metric,
                    'Elasticity': elasticity
                })

    # Convert elasticity results to DataFrame for analysis and visualization
    elasticity_df = pd.DataFrame(elasticity_results)

    # Visualize resilience regression and elasticity results
    plot_shock_visualizations(resilience_df)
    plot_elasticity_results(elasticity_df)

if __name__ == "__main__":
    main()
