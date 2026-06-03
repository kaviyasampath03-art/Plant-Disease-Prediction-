import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample Data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Train Model
model = LinearRegression()
model.fit(X, y)

# Save Model
pickle.dump(model, open('model.pkl', 'wb'))

print("Model saved successfully!")


