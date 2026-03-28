import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import plot_tree
import warnings

warnings.filterwarnings('ignore')

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("Data.csv")

print("Dataset Preview:")
print(df.head())

print("\nDataset Info:")
df.info()

# -------------------------------
# Remove missing values
# -------------------------------
df = df.dropna()

# -------------------------------
# Features and Target
# -------------------------------
X = df.iloc[:, 1:2].values   # Age
y = df.iloc[:, 2].values     # Salary

# -------------------------------
# Create Random Forest Model
# -------------------------------
regressor = RandomForestRegressor(
    n_estimators=500,
    random_state=42
)

# -------------------------------
# Train Model
# -------------------------------
regressor.fit(X, y)

# -------------------------------
# Predictions
# -------------------------------
y_pred = regressor.predict(X)

# -------------------------------
# Evaluation
# -------------------------------
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# -------------------------------
# Visualization
# -------------------------------
X_grid = np.arange(X.min(), X.max(), 0.01)
X_grid = X_grid.reshape(-1, 1)

plt.figure(figsize=(8,6))
plt.scatter(X, y, color='blue')
plt.plot(X_grid, regressor.predict(X_grid), color='green')
plt.title("Random Forest Regression")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()