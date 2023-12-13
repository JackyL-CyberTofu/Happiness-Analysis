import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def subset_data_by_region(data, region):
    columns_of_interest = [
        'Happiness Score',
        'Death rate per 100 000 population',
        'Log GDP per capita',
        'Social support',
        'Healthy life expectancy at birth',
        'Freedom to make life choices',
        'Generosity',
        'Perceptions of corruption',
        'Positive affect',
        'Negative affect'
    ]
    plt.figure(figsize=(12, 10))
    data_clean = data.dropna(subset=columns_of_interest)
    if region == 'All':
        ax = sns.heatmap(data_clean[columns_of_interest].corr(), mask=np.triu(np.ones_like(data_clean[columns_of_interest].corr(), dtype=bool)),annot=True, fmt=".2f", vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(230, 20, as_cmap=True))

    else:
        ax = sns.heatmap(data_clean[data_clean['Region Name'] == region][columns_of_interest].corr(), annot=True, fmt=".2f", vmin=-1, vmax=1, center=0.25)

    labels = ['Happiness', 'Death Rate', 'Log GDP', 'Social Support', 'Life Expectancy', 'Freedom', 'Generosity', 'Corruption', 'Positive Affect', 'Negative Affect']
    ax.set_xticklabels(labels, rotation=45)
    ax.set_yticklabels(labels, rotation=0)
    plt.title('Correlation Heatmap for ' + region)
    plt.savefig(f"Correlation_Heatmap_{region.replace(' ', '_')}.png")
    plt.close()


regions = ['Europe', 'Central and South America', 'Asia', 'Oceania', 'North America and the Caribbean', 'Africa', 'All']

data = pd.read_csv('../Data/combined.csv')

for region in regions:
    subset_data_by_region(data, region)
