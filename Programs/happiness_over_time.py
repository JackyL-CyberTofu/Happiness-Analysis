import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

WHR = pd.read_csv('../Data/Clean/WHR2023-UpdatedNames.csv', parse_dates=['year'])
WHO = pd.read_csv('../Data/Clean/WHOMortalityData-UpdatedNames.csv')

grouped = WHO[['Country Name', 'Region Name']].drop_duplicates()
out = pd.merge(WHR, grouped, how='left', left_on='Country name', right_on='Country Name')

# List of columns to plot
columns_to_plot = ['Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth',
                   'Freedom to make life choices', 'Generosity', 'Perceptions of corruption',
                   'Positive affect', 'Negative affect']


def plot_column(column_name):
    data = out.dropna(subset=[column_name])
    long_data = data[['Region Name', 'year', column_name]]

    plt.figure()

    sns.lineplot(data=long_data, x='year', y=column_name, hue='Region Name', marker='o', errorbar=None,estimator='median', lw=2)

    plt.title(f'{column_name} Over Time')
    plt.xlabel('Year')
    plt.ylabel(column_name)
    plt.legend(fontsize='small')
    plt.tight_layout()
    plt.savefig(f"../Data/Analyze/Region Stat/{column_name.replace(' ', '_')}_over_time.png")
    plt.close()


for column in columns_to_plot:
    plot_column(column)
