import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv("qualitative.csv")

f1a = data[(data["age"] == "18-24") & (data["adviceIncorporate"] == "Always followed the AI advice closely")]
f1b = data[(data["age"] == "25-34") & (data["adviceIncorporate"] == "Always followed the AI advice closely")]
f1c = data[(data["age"] == "35-44") & (data["adviceIncorporate"] == "Always followed the AI advice closely")]
f1d = data[(data["age"] == "45-54") & (data["adviceIncorporate"] == "Always followed the AI advice closely")]
f1e = data[(data["age"] == "55-64") & (data["adviceIncorporate"] == "Always followed the AI advice closely")]

f2a = data[(data["age"] == "18-24") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")]
f2b = data[(data["age"] == "25-34") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")]
f2c = data[(data["age"] == "35-44") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")]
f2d = data[(data["age"] == "45-54") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")]
f2e = data[(data["age"] == "55-64") & (data["adviceIncorporate"] == "Generally followed the advice but deviated sometimes when I thought I had a better strategy")]

f3a = data[(data["age"] == "18-24") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")]
f3b = data[(data["age"] == "25-34") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")]
f3c = data[(data["age"] == "35-44") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")]
f3d = data[(data["age"] == "45-54") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")]
f3e = data[(data["age"] == "55-64") & (data["adviceIncorporate"] == "Did not follow the advice at all or only rarely")]

d1 = {
    "f1a": f1a["total_bonus"].mean(),
    "f1b": f1b["total_bonus"].mean(),
    "f1c": f1c["total_bonus"].mean(),
    "f1d": f1d["total_bonus"].mean(),
    "f1e": f1e["total_bonus"].mean()
}

d2 = {
    "f2a": f2a["total_bonus"].mean(),
    "f2b": f2b["total_bonus"].mean(),
    "f2c": f2c["total_bonus"].mean(),
    "f2d": f2d["total_bonus"].mean(),
    "f2e": f2e["total_bonus"].mean()
}

d3 = {
    "f3a": f3a["total_bonus"].mean(),
    "f3b": f3b["total_bonus"].mean(),
    "f3c": f3c["total_bonus"].mean(),
    "f3d": f3d["total_bonus"].mean(),
    "f3e": f3e["total_bonus"].mean()
}


keys1 = list(d1.keys())
keys2 = list(d2.keys())
keys3 = list(d3.keys())
keys = list(["18-24", "25-34", "35-44", "45-54", "55-64"])

vals1 = np.array(list(d1.values()))
vals2 = np.array(list(d2.values()))
vals3 = np.array(list(d3.values()))

plt.bar(keys, vals1, label = "Always followed the AI advice closely")
plt.bar(keys, vals2, bottom = vals1, label = "Generally followed the advice but deviated sometimes when I thought I had a better strategy")
plt.bar(keys, vals3, bottom = vals2, label = "Did not follow the advice at all or only rarely")
plt.title("age vs compliance")
plt.xlabel("age")
plt.ylabel("adviceIncorporate")
plt.tight_layout()

plt.show()