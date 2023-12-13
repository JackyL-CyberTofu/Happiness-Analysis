import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# GOAL: Analyse happiness metrics and happiness with suicide rates

data = pd.read_csv('../Data/cleaned_data.csv')

# Linear regression to see suicide rate vs happiness score and metrics of happiness
suicide_rate = data['Death rate per 100 000 population']
metrics = ['Happiness Score', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 
		'Positive affect', 'Negative affect']

results = pd.DataFrame(index=metrics, columns=['p-value', 'correlation coef'], dtype='float64')

plt.figure(figsize=(20, 10))

for i in range(len(metrics)):
	x = metrics[i]
	reg = stats.linregress(data[x], suicide_rate)
	# print("Does " + x + " impact suicide rates? P-value: " + str(reg.pvalue))
	# print("Correlation coefficient (r): " + str(reg.rvalue))

	results.loc[metrics[i]] = [reg.pvalue, reg.rvalue]

	# Check normality of residuals
	residuals = suicide_rate - (reg.slope*data[x] + reg.intercept)
	plt.subplot(3,3,i+1)
	plt.hist(residuals)
	plt.title("Suicide rate " + "vs " + x + " residuals")

plt.savefig("../Data/Analyze/Correlation/Residuals_Histogram.png")
print(results)


# Create linear regression plots for suicide rates vs metrics of happiness

plt.figure(figsize=(20,10))
for i in range(len(metrics)):
	x = metrics[i]
	reg = stats.linregress(data[x], suicide_rate)
	
	plt.subplot(3,3,i+1)
	plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
	plt.plot(data[x], suicide_rate, 'bo', markersize=2)
	plt.plot(data[x], reg.slope*data[x] + reg.intercept, 'r-')
	plt.title("Suicide rate " + "vs " + x)
	plt.xlabel(x)
	plt.ylabel("Death rate per 100 000 population")

plt.savefig("../Data/Analyze/Correlation/regression_plots.png")
