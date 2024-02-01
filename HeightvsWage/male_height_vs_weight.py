import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

read = pd.read_csv("height.csv")

male_data = read[read["male"] == 1]

mheight = male_data[["height"]]
mwage = male_data["wage"]
ave_height = male_data["height"].mean()


linr = LinearRegression()
linr.fit(mheight, mwage)

predict1 = linr.predict(mheight)

plt.scatter(mheight, mwage, label="Data")
plt.plot(mheight, predict1, label="Regression Line", color="red")


fheight_array = np.array(mheight.values.flatten())
fwage_array = np.array(mwage.values.flatten())

correlation_matrix = np.corrcoef(fheight_array, fwage_array)
correlation_coefficient = correlation_matrix[0, 1]

plt.title(f"Male Height vs Wage\nCorrelation Coefficient: {correlation_coefficient:.3f}")
plt.xlabel(f"Height\nAverage male height: {ave_height:.1f} cm")
plt.ylabel("Yearly Wage($)")
plt.tight_layout()
plt.legend()
plt.show()
