import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

metrics = [
    "Log GDP per capita",
    "Social support",
    "Healthy life expectancy at birth",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of corruption"
]

data = pd.read_csv("../Data/combined.csv")

sns.set_theme(style="whitegrid")

# Happiness Scores vs. Metrics
for metric in metrics:
    # Calculate the correlation for Happiness Score
    correlation_happiness = data["Happiness Score"].corr(data[metric])

    plt.figure()
    sns.regplot(data=data, x=metric, y="Happiness Score")
    sns.scatterplot(data=data, x=metric, y="Happiness Score", hue="Region Name")
    plt.title(f'Happiness Score vs {metric} (Correlation: {correlation_happiness:.2f})')
    plt.legend(fontsize='small')
    plt.tight_layout()
    plt.savefig(f"Happiness_Score_vs_{metric.replace(' ', '_')}.png")
    plt.close()

    # Calculate the correlation for Death Rate
    correlation_death = data["Death rate per 100 000 population"].corr(data[metric])

    plt.figure()
    sns.regplot(data=data, x=metric, y="Death rate per 100 000 population")
    sns.scatterplot(data=data, x=metric, y="Death rate per 100 000 population", hue="Region Name")
    plt.title(f'Death Rate vs {metric} (Correlation: {correlation_death:.2f})')
    plt.legend(fontsize='small')
    plt.tight_layout()
    plt.savefig(f"Death_Rate_vs_{metric.replace(' ', '_')}.png")
    plt.close()