import pandas as pd
import matplotlib.pyplot as plt

read = pd.read_csv("obesity_data.csv")

bar_chart = read.groupby("ObesityCategory")["Height"].mean()



order = ["Underweight", "Normal weight", "Overweight", "Obese"]
bar_chart = bar_chart.reindex(order)
bar_chart = bar_chart.plot(kind="bar", color = ["green", "blue", "yellow", "red"])

plt.xlabel("Obesity Category")
plt.ylabel("Height")
plt.title("Obesity Category vs Height")

plt.xticks(rotation=0)
plt.show()