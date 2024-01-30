import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

read = pd.read_csv("study_data.csv")

study_hours = read[["Study Hours"]]
score = read["Score"]


a = LinearRegression()
a.fit(study_hours, score)


prediction = a.predict(study_hours)
plt.scatter(study_hours, score, label="Data")
plt.plot(study_hours, prediction, color = "red", label="Regression Line" )

plt.xlabel('Study Hours')
plt.ylabel('Score')
plt.title('Linear Regression: Study Hours vs Score')

plt.legend()
plt.show()
