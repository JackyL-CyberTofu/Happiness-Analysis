import pandas as pd

happy_data = pd.read_csv('../Data/Clean/WHR2023-UpdatedNames.csv')
mort_data = pd.read_csv('../Data/Clean/WHOMortalityData-UpdatedNames.csv')

# Because the happiness data involves all individuals regardless of age and gender, we'll keep it that way with the mortality data by keeping only rows involving all age and gender
mort_data = mort_data[mort_data['Sex'] == "All"]
mort_data = mort_data[mort_data['Age group code'] == "Age_all"]

# Combines the two datasets
data = happy_data.merge(mort_data, how='inner', left_on=['Country name', 'year'], right_on=['Country Name', 'Year'])
data = data.rename(columns={"Number":"Death Number", "Life Ladder":"Happiness Score"})

data.to_csv('../Data/combined.csv', index=False)
