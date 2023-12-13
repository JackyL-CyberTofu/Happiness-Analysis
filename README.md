# CMPT353-Project

**Required libraries:** pandas, scipy, sys, matplotlib, seaborn, numpy, sklearn

**Order of execution:**
1. first_look_data.py
2. match_country_name.ipynb
3. combine_data.py
4. clean_data.py
5. Rest of the programs can be executed in any order as they are only reliant on the first 4 programs

**How to run code:**

*first_look_data.py:*
In the CMPT353-Project/Programs folder, run ```python3 first_look_data.py``` on the terminal. No files will be produced.

*match_country_name.ipynb*
Matches similar country names for joining. Run this file in Jupyter Notebook. The original ```WHR2023.csv``` and ```WHO2023.csv``` will be required.

*combine_data.py:*
In the CMPT353-Project/Programs folder, run ```python3 combine_data.py``` on the terminal. This will produce the ```combined.csv``` file in the Data folder.

*clean_data.py:*
In the CMPT353-Project/Programs folder, run ```python3 clean_data.py``` on the terminal. This will produce the ```cleaned_data.csv``` file in the Data folder.

*analyze-combined.py:*
In the CMPT353-Project/Programs folder, run ```python3 analyze-combined.py``` on the terminal. There will be a print output of linear regression p-value and correlation coefficients. This will also produce ```Residuals_Histogram.png``` and ```regression_plots.png``` in the Data/Analyze/Correlation file.

*corr_heatmap_region:*
In the CMPT353-Project/Programs folder, run ```python3 corr_heatmap_region.py``` on the terminal. Running combine_data.py first is required.

*gender_death_rate.py:*
In the CMPT353-Project/Programs folder, run ```python3 gender_death_rate.py``` on the terminal. Running combine_data.py first is required.

*happiness_over_time.py:*
In the CMPT353-Project/Programs folder, run ```python3 happiness_over_time.py``` on the terminal. The tables must be joined together using the output from match_country_name.ipynb.

*mortality_analysis.py:*
In the CMPT353-Project/Programs folder, run ```python3 mortality_analysis.py``` on the terminal. The output will print the average death rates grouped by age group and region sorted in descending order. This will also produce ```Death_rate_over_time.png``` and ```Death_rate_over_time_age.png``` located in Data/Analyze/Region Stat and Data/Analyze/Age Stat. 

*scatter_plot.py:*
In the CMPT353-Project/Programs folder, run ```python3 scatter_plot.py``` on the terminal. Running combine_data.py first is required.

