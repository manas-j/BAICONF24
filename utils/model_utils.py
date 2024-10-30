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

# utils/model_utils.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def apply_shock(data, metric, shock):
    """Apply a shock to a financial metric and return the updated data."""
    shocked_data = data.copy()
    shocked_data[metric] = shocked_data[metric] * (1 + shock)
    return shocked_data

def resilience_regression(data, esg, metric, shock):
    """Perform regression to assess resilience for a given ESG component and financial metric."""
    shocked_data = apply_shock(data, metric, shock)
    shocked_data = shocked_data[[esg, metric]].dropna()

    # If no valid data remains, return None to skip this combination
    if shocked_data.empty:
        return None, None

    X = shocked_data[[esg]]
    y = shocked_data[metric]

    model = LinearRegression()
    model.fit(X, y)

    return model.coef_[0], model.intercept_

# utils/model_utils.py

import numpy as np
from sklearn.linear_model import LinearRegression

# Existing resilience_regression and apply_shock functions go here

def calculate_elasticity(data, esg, metric):
    """Calculate the elasticity of financial metric with respect to ESG score."""
    if metric not in data.columns:
        print(f"Warning: {metric} is not in DataFrame columns.")
        return None

    # Filter out rows with NaN and log-transform data
    data_filtered = data[[esg, metric]].dropna()
    if data_filtered.empty:
        print(f"Skipping {esg} vs {metric} due to insufficient data.")
        return None

    # Apply log transformation for elasticity calculation
    data_filtered[esg] = np.log(data_filtered[esg] + 1)  # Avoid log(0)
    data_filtered[metric] = np.log(data_filtered[metric] + 1)  # Avoid log(0)

    X = data_filtered[[esg]]
    y = data_filtered[metric]

    model = LinearRegression()
    model.fit(X, y)

    elasticity = model.coef_[0]  # Elasticity is the coefficient of log-log model
    return elasticity
