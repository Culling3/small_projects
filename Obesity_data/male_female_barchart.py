import pandas as pd
import matplotlib.pyplot as plt

read = pd.read_csv("obesity_data.csv")

bar_chart = read.groupby("Gender")["BMI"].mean()
bar_chart = bar_chart.plot(kind="bar", color = ["red", "blue"])

plt.xlabel("Gender")
plt.ylabel("BMI")
plt.title("Gender vs BMI")

plt.xticks(rotation=0)
plt.show()