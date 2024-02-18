import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

read = pd.read_csv("obesity_data.csv")

bmi = read[["BMI"]]
height = read["Height"]
bmim = bmi.mean()
bmim1 = bmim.iloc[0]
heightm = height.mean()
print(heightm)

linr = LinearRegression()
linr.fit(bmi, height)

predict1 = linr.predict(bmi)
plt.scatter(bmi, height, label="Data")
plt.plot(bmi, predict1, color="red", label="Regression Line")


plt.xlabel('BMI')
plt.ylabel('Height')
plt.title('Linear Regression: BMI vs Height')

correlation_matrix = np.corrcoef(bmi.values.flatten(), height.values.flatten())
correlation_coefficient = correlation_matrix[0, 1]
print(f"Correlation coeeficient: {correlation_coefficient}")
print(f"R^2 score: {linr.score(bmi, height)}")
print(f"Average bmi: {bmim1:.2f}")
plt.legend()
plt.show()
