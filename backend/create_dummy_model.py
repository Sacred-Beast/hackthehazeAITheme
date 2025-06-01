import joblib
from sklearn.linear_model import LogisticRegression
import numpy as np
import os

# Create some fake training data (e.g., scores in 3 subjects)
X = np.array([
    [90, 85, 80],
    [60, 65, 70],
    [30, 40, 35],
    [95, 92, 88],
    [55, 58, 60],
    [20, 25, 30],
])
y = ["Engineering", "Commerce", "Arts", "Engineering", "Commerce", "Arts"]

model = LogisticRegression()
model.fit(X, y)

# Save the model to backend/ml_models/aptitude_model.pkl
save_path = os.path.join("backend", "ml_models", "aptitude_model.pkl")
joblib.dump(model, save_path)

print(f"✅ Model saved to {save_path}")
