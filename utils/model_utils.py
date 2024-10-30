# utils/model_utils.py

import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

def statistical_significance_test(data, esg_columns, financial_columns):
    """Prints statistical significance of correlations between ESG and financial metrics."""
    print("\nStatistical Significance of Correlations:")
    for esg in esg_columns:
        for metric in financial_columns:
            corr, p_value = stats.pearsonr(data[esg], data[metric])
            significance = "Significant" if p_value < 0.05 else "Not Significant"
            print(f"{esg} vs {metric}: Correlation = {corr:.2f}, p-value = {p_value:.4f} ({significance})")

def regression_analysis(data, esg, metric):
    """Performs linear regression and displays results and plots."""
    X = data[[esg]]
    y = data[metric]
    X = sm.add_constant(X)  # Add intercept

    model = sm.OLS(y, X).fit()
    predictions = model.predict(X)

    # Plot regression line and data points
    plt.figure(figsize=(8, 5))
    plt.scatter(X[esg], y, alpha=0.7, label='Data Points')
    plt.plot(X[esg], predictions, color='red', linewidth=2, label='Regression Line')
    plt.title(f'Regression: {metric} on {esg}', fontsize=16)
    plt.xlabel(esg, fontsize=14)
    plt.ylabel(metric, fontsize=14)
    plt.legend()
    plt.show()

    # Display regression summary
    print(f"\nRegression Summary for {metric} vs {esg}:")
    print(model.summary())
