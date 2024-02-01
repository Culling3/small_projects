import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

read = pd.read_csv("height.csv")

female_data = read[read["male"] == 0]


fheight = female_data[["height"]]
fwage = female_data["wage"]
linr = LinearRegression()
linr.fit(fheight, fwage)

predict1 = linr.predict(fheight)

plt.scatter(fheight, fwage, label="Data")
plt.plot(fheight, predict1, label="Regression Line", color="red")

fheight_array = np.array(fheight.values.flatten())
fwage_array = np.array(fwage.values.flatten())

correlation_matrix = np.corrcoef(fheight_array, fwage_array)
correlation_coefficient = correlation_matrix[0, 1]
ave_height = female_data["height"].mean()


plt.title(f"Female Height vs Wage\nCorrelation coefficient: {correlation_coefficient:.3f}")
plt.xlabel(f"Height\nAverage female height: {ave_height:.1f} cm")
plt.ylabel("Yearly Wage($)")
plt.tight_layout()
plt.legend()
plt.show()