import pandas as pd
from scipy import stats

happiness_data = pd.read_csv("../Data/WHR2023.csv")
print(happiness_data.head())
print("Dimension = ", happiness_data.shape)

missing_data = happiness_data[happiness_data.isna().any(axis=1)]
missing_data.reset_index(drop=True, inplace=True)
print(missing_data)

# Which columns have missing data
print(missing_data.isna().sum())
print()

# Counts for each country
country_count = happiness_data['Country name'].value_counts().sort_index()
print("Number of entries for each country:")
print(country_count)
print(country_count.shape)

print("Countries with 3 or fewer rows")
country_little_data = country_count[country_count <= 3]
print(country_little_data.index)

# Counts for each year
year_count = happiness_data['year'].value_counts().sort_index()
print("Number of entries for each year:")
print(year_count)
print(year_count.shape)
print()

happiness_data = happiness_data.dropna()
happiness_by_country = happiness_data.groupby('Country name').mean()

test_cols = [
    "Life Ladder",
    "Log GDP per capita",
    "Social support",
    "Healthy life expectancy at birth",
    "Freedom to make life choices",
    "Generosity",
    "Perceptions of corruption",
    "Positive affect",
    "Negative affect"
]
# Check normality
print("Normality for each category:\n")
for i in range(len(test_cols)):
    x = test_cols[i]
    print(x, stats.normaltest(happiness_by_country[x]).pvalue)
print("All categories have p-values way less than 0.05, so that limits statistical tests we can perform")





