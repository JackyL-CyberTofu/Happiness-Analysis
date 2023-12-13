import pandas as pd
import matplotlib.pyplot as plt

# To execute: python3 Programs/mortality_analysis.py
data = pd.read_csv('../Data/Clean/WHOMortalityData-UpdatedNames.csv')

age_death_rate = data.groupby(['Year', 'Age Group'])['Death rate per 100 000 population'].mean()
region_death_rate = data.groupby(['Year', 'Region Name'])['Death rate per 100 000 population'].mean()

# Analyze the death rates per 100,000 people of all age groups
age_groups_dr = age_death_rate.groupby('Age Group').mean()
print('Average deaths per 100,000 people for each group')
print(age_groups_dr.sort_values(ascending=False))
print()

top_five_age_groups_dr = age_groups_dr.nlargest(5).index.to_list()

# Plot the top five age groups with the highest death rates
plt.figure(figsize=(10, 6))
for age_group in top_five_age_groups_dr:
    age_group_data = age_death_rate.xs(age_group, level='Age Group')
    plt.plot(age_group_data.index.get_level_values('Year'), age_group_data.values, marker='o',
             label=f'Age Group: {age_group}')
plt.xlabel('Year')
plt.ylabel('Deaths per 100,000 people')
plt.title('Top 5 Age Groups with the Highest Death Rate')
plt.grid(True)
plt.legend()

plt.savefig('../Data/Analyze/Age Stat/Death_rate_over_time_age.png')

# Analyze the death rates per 100,000 people of all regions
region_dr = region_death_rate.groupby('Region Name').mean()
print('Average deaths per 100,000 people for each region')
print(region_dr.sort_values(ascending=False))
print()

plt.figure(figsize=(10, 6))
for region in region_dr.index.to_list():
    region_data = region_death_rate.xs(region, level='Region Name')
    plt.plot(region_data.index.get_level_values('Year'), region_data.values, marker='o', label=region)
plt.xlabel('Year')
plt.ylabel('Deaths per 100,000 people')
plt.title('Regions and Their Death Rate')
plt.grid(True)
plt.legend()

plt.savefig('../Data/Analyze/Region Stat/Death_rate_over_time.png')
