# utils/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(data):
    """Plot a correlation heatmap."""
    plt.figure(figsize=(15, 8))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap of ESG Components and Financial Metrics', fontsize=18)
    plt.show()

def plot_pairwise_correlation(data, esg_columns, financial_columns):
    """Plot pairwise correlations between ESG and financial metrics."""
    for esg in esg_columns:
        plt.figure(figsize=(10, 6))
        correlations = data[financial_columns].corrwith(data[esg])
        sns.barplot(x=correlations.values, y=correlations.index, palette='viridis')
        plt.title(f'Correlation of {esg} with Financial Metrics', fontsize=18)
        plt.xlabel('Correlation Coefficient', fontsize=14)
        plt.ylabel('Financial Metric', fontsize=14)
        plt.show()

def plot_scatterplot_matrix(data, selected_columns):
    """Plot a scatterplot matrix for selected columns."""
    sns.pairplot(data[selected_columns], diag_kind='kde')
    plt.suptitle('Pairplot of Selected ESG Components and Financial Metrics', y=1.02, fontsize=16)
    plt.show()

def plot_boxplots(data, columns):
    """Plot boxplots for each column to check for outliers."""
    plt.figure(figsize=(20, 10))
    for idx, col in enumerate(columns):
        plt.subplot(4, 4, idx + 1)
        sns.boxplot(y=data[col], palette='Set2')
        plt.title(f'Boxplot of {col}', fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_distributions(data, columns):
    """Plot distribution histograms for each column."""
    plt.figure(figsize=(20, 12))
    for idx, col in enumerate(columns):
        plt.subplot(4, 4, idx + 1)
        sns.histplot(data[col], kde=True, bins=20, color='purple')
        plt.title(f'Distribution of {col}', fontsize=12)
    plt.tight_layout()
    plt.show()

# utils/visualization.py

import seaborn as sns
import matplotlib.pyplot as plt

def plot_shock_visualizations(results_df):
    """Visualize the regression coefficients and intercepts across shock levels."""

    # Plot regression coefficients
    plt.figure(figsize=(15, 8))
    sns.barplot(
        data=results_df, x='Shock Level', y='Coefficient', hue='ESG Component',
        ci=None, palette='muted'
    )
    plt.title('Regression Coefficients under Different Shock Levels', fontsize=18)
    plt.xlabel('Shock Level (Percentage Change)', fontsize=14)
    plt.ylabel('Regression Coefficient', fontsize=14)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

    # Plot intercepts
    plt.figure(figsize=(15, 8))
    sns.lineplot(
        data=results_df, x='Shock Level', y='Intercept', hue='ESG Component',
        style='Financial Metric', markers=True
    )
    plt.title('Intercepts for ESG Components and Financial Metrics under Stress', fontsize=18)
    plt.xlabel('Shock Level (Percentage Change)', fontsize=14)
    plt.ylabel('Intercept', fontsize=14)
    plt.grid(True)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

# utils/visualization.py

import seaborn as sns
import matplotlib.pyplot as plt

# Existing plot_shock_visualizations function goes here

def plot_elasticity_results(elasticity_df):
    """Visualize the elasticity of financial metrics with respect to ESG components."""
    plt.figure(figsize=(15, 8))
    sns.barplot(
        data=elasticity_df, x='Elasticity', y='Financial Metric', hue='ESG Component',
        palette='muted', ci=None
    )
    plt.title('Elasticity of Financial Metrics with Respect to ESG Components', fontsize=18)
    plt.xlabel('Elasticity Coefficient', fontsize=14)
    plt.ylabel('Financial Metric', fontsize=14)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

    print("\nSummary of Elasticity Analysis:")
    for index, row in elasticity_df.iterrows():
        esg = row['ESG Component']
        metric = row['Financial Metric']
        elasticity = row['Elasticity']
        print(f"- {metric} is {elasticity:.4f} times sensitive to changes in {esg}.")

# utils/visualization.py

import seaborn as sns
import matplotlib.pyplot as plt

def plot_shock_visualizations(results_df):
    """Visualize the regression coefficients for different shock levels."""
    plt.figure(figsize=(15, 8))
    sns.barplot(
        data=results_df, x='Shock Level', y='Coefficient', hue='ESG Component',
        ci=None, palette='muted'
    )
    plt.title('Regression Coefficients under Different Shock Levels', fontsize=18)
    plt.xlabel('Shock Level (Percentage Change)', fontsize=14)
    plt.ylabel('Regression Coefficient', fontsize=14)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

    plt.figure(figsize=(15, 8))
    sns.lineplot(
        data=results_df, x='Shock Level', y='Intercept', hue='ESG Component',
        style='Financial Metric', markers=True
    )
    plt.title('Intercepts for ESG Components and Financial Metrics under Stress', fontsize=18)
    plt.xlabel('Shock Level (Percentage Change)', fontsize=14)
    plt.ylabel('Intercept', fontsize=14)
    plt.grid(True)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

    print("\nKey Insights and Observations:")
    for index, row in results_df.iterrows():
        esg = row['ESG Component']
        metric = row['Financial Metric']
        shock = row['Shock Level']
        coef = row['Coefficient']
        intercept = row['Intercept']

        print(f"- {esg} vs {metric} under {shock*100}% shock: Coefficient = {coef:.4f}, Intercept = {intercept:.4f}")

def plot_elasticity_results(elasticity_df):
    """Visualize the elasticity of financial metrics with respect to ESG components."""
    plt.figure(figsize=(15, 8))
    sns.barplot(
        data=elasticity_df, x='Elasticity', y='Financial Metric', hue='ESG Component',
        palette='muted', ci=None
    )
    plt.title('Elasticity of Financial Metrics with Respect to ESG Components', fontsize=18)
    plt.xlabel('Elasticity Coefficient', fontsize=14)
    plt.ylabel('Financial Metric', fontsize=14)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

    print("\nSummary of Elasticity Analysis:")
    for index, row in elasticity_df.iterrows():
        esg = row['ESG Component']
        metric = row['Financial Metric']
        elasticity = row['Elasticity']
        print(f"- {metric} is {elasticity:.4f} times sensitive to changes in {esg}.")
