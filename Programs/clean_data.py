import pandas as pd

data = pd.read_csv('../Data/combined.csv')

# Drop duplicate country name and year columns from merging
data = data.drop(['Country Name', 'Year'], axis=1)

# Drop following columns as they are unnecessary
data = data.drop(['Region Code', 'Sex', 'Age group code', 'Age Group', 'Country Code'], axis=1)

# Remove rows with missing data (NaN or 0 rows)
# After examining the dataset, all 0 values should be treated as missing values
data = data[data!=0] # From https://stackoverflow.com/questions/27020312/drop-row-in-pandas-dataframe-if-any-value-in-the-row-equals-zero
data = data.dropna(axis=0, how='any')

# Rename number to death number for clarity
data = data.rename(columns={"Number":"Death Number", "Life Ladder":"Happiness Score"})

data.to_csv('../Data/cleaned_data.csv', index=False)
