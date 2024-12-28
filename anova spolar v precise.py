import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'sentiment_analysis_w_bonus_precise.csv'
df = pd.read_csv(file_path)

# clean msising
df_cleaned = df.dropna(subset=['sentiment_polarity'])

groups_cleaned = [group['sentiment_polarity'].values for name, group in df_cleaned.groupby('con.precise')]

anova_result_cleaned = stats.f_oneway(*groups_cleaned)

print("F-statistic:", anova_result_cleaned.statistic)
print("p-value:", anova_result_cleaned.pvalue)

plt.figure(figsize=(10, 6))
sns.boxplot(data = df_cleaned, x = "con.precise", y = "sentiment_polarity")

plt.title("con.precise vs sentiment polarity")
plt.xlabel("con.precise")
plt.ylabel("sentiment polarity")

plt.show()