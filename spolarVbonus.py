import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

file_path = 'sentiment_analysis_with_bonus.csv'
data = pd.read_csv(file_path)

# check missing
missing_values = data[['sentiment_polarity', 'total_bonus']].isna().sum()
non_numeric_values = data[['sentiment_polarity', 'total_bonus']].map(lambda x: not isinstance(x, (int, float))).sum()

# remove missing
cleaned_data = data.dropna(subset=['sentiment_polarity', 'total_bonus'])


x_clean = cleaned_data['sentiment_polarity']
y_clean = cleaned_data['total_bonus']

# linear regression
slope, intercept, rval, pval, std_err = stats.linregress(x_clean, y_clean)

# compute t_stat and 2-tailed p_val
tstat = slope / std_err
pslope = stats.t.sf(abs(tstat), df = len(x_clean) - 2) * 2 

results = {
    'slope': slope,
    'intercept': intercept,
    'r_value': rval,
    'p_value (overall)': pval,
    't_statistic (slope)': tstat,
    'p_value (slope)': pslope,
    'standard_error': std_err
}

print(results)

plt.scatter(x_clean, y_clean, label="Data Points", alpha=0.77)

plt.plot(x_clean, intercept + slope * x_clean, color="red", label="Regression Line")

plt.xlabel("Sentiment Polarity")
plt.ylabel("Total Bonus")
plt.title("Relationship between Sentiment Polarity vs Total Bonus")
plt.legend()

plt.show()