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
