#2.Implementation of Simple Linear Regression using Python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("C:/FullStack Devp/ML LAB/weatherHistory.csv")

# Select variables
X = df["Temperature (C)"].values.reshape(-1,1)
y = df["Apparent Temperature (C)"].values

# Remove missing values if any
mask = ~np.isnan(X.flatten()) & ~np.isnan(y)
X = X[mask]
y = y[mask]

# ----- From scratch -----
x = X.flatten()

x_mean = np.mean(x)
y_mean = np.mean(y)

b1 = np.sum((x - x_mean)*(y - y_mean)) / np.sum((x - x_mean)**2)
b0 = y_mean - b1*x_mean

# ----- Using sklearn -----
model = LinearRegression()
model.fit(X, y)

# Predictions for line
x_line = np.linspace(x.min(), x.max(), 100)
y_line = b0 + b1*x_line

# Plot
plt.figure()
plt.scatter(x, y)
plt.plot(x_line, y_line)
plt.xlabel("Temperature (C)")
plt.ylabel("Apparent Temperature (C)")
plt.title("Simple Linear Regression on Weather Dataset")
plt.show()

b0, b1, model.intercept_, model.coef_[0]





