import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("qualitative.csv")

f1 = data[data["con.precise"] == 1]
f2 = data[data["con.precise"] == 2]
f3 = data[data["con.precise"] == 3]

inco_average_dict = {
    "precision: 1": f1["total_bonus"].mean(),
    "precision: 2": f2["total_bonus"].mean(), 
    "precision: 3": f3["total_bonus"].mean()
}

incokeys = list(inco_average_dict.keys())
incovalues = list(inco_average_dict.values())

plt.bar(incokeys, incovalues)
plt.title("advice precision vs bonus earned")
plt.xlabel("con.precise")
plt.ylabel("total_bonus")
plt.tight_layout()

plt.show()