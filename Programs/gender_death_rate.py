import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('../Data/combined.csv')

data = data[data.groupby('Country name')['year'].transform(max) == data['year']]
data = data[data['Sex'] != 'All']
age_groups_data_new = data[data['Age Group'] != '[All]'].dropna(subset=['Death rate per 100 000 population'])

plt.figure()
sns.barplot(data=age_groups_data_new, x='Age Group', y='Death rate per 100 000 population', hue='Sex', estimator=np.mean, errorbar=None)
plt.title('Average Death Rate by Age Groups')
plt.ylabel('Death rate per 100,000 population')
plt.xlabel('Age Group')
plt.legend(title='Sex', loc='upper right', fontsize='small')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../Data/average_death_rate_by_gender.png')
plt.show()