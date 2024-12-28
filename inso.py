import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("qualitative.csv")

plt.scatter(data["con.precise"], data["total_bonus"])
plt.xlabel("precision")
plt.ylabel("bonus")
plt.title("precision vs bonus")
plt.show()

# data[["con.precise", "total_bonus"]].hist(bins=2, alpha=0.5)
# plt.show()

correlation = data["con.precise"].corr(data["total_bonus"])
print(correlation)

plt.scatter(data["age"], data["total_bonus"])
plt.xlabel("age")
plt.ylabel("bonus")
plt.title("age vs bonus")
plt.show()

# vs advice incorp