import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("qualitative.csv")

filtered_always = data[data["adviceIncorporate"] == "Always followed the AI advice closely"]
filtered_general = data[data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy"]
filtered_not = data[data["adviceIncorporate"] == "Did not follow the advice at all or only rarely"]

inco_average_dict = {
    "Always followed the AI\n advice closely": filtered_always["total_bonus"].mean(),
    "\n\n Generally followed the advice\n but deviated sometimes\n when I thought I had a better strategy": filtered_general["total_bonus"].mean(), 
    "Did not follow the advice\n at all or only rarely": filtered_not["total_bonus"].mean()
}

incokeys = list(inco_average_dict.keys())
incovalues = list(inco_average_dict.values())

plt.bar(incokeys, incovalues)
plt.title("degree of advice incorporation vs bonus earned")
plt.xlabel("adviceIncorporate")
plt.ylabel("total_bonus")
plt.tight_layout()

plt.show()