import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

read = pd.read_csv("obesity_data.csv")

bmi = read[["BMI"]]
height = read["Height"]


linr = LinearRegression()
linr.fit(bmi, height)

predict1 = linr.predict(bmi)
plt.scatter(bmi, height, label="Data")
plt.plot(bmi, predict1, color="red", label="Regression Line")


plt.xlabel('BMI')
plt.ylabel('Height')
plt.title('Linear Regression: BMI vs Height')

plt.legend()
plt.show()
