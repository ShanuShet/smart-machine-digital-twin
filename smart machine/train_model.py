import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("predictive_maintenance.csv")
df.columns = df.columns.str.strip()

# Features
X = df[[
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]]

# Target
y = df["Target"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestClassifier(n_estimators=150)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# Save everything
joblib.dump(model, "model.pkl")
joblib.dump(X.columns.tolist(), "features.pkl")
joblib.dump((X_test, y_test, y_pred), "test_data.pkl")
joblib.dump(acc, "accuracy.pkl")