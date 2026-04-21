import joblib
import numpy as np

model = joblib.load("model.pkl")

def predict_failure(air, process, speed, torque, wear):
    data = np.array([[air, process, speed, torque, wear]])
    return model.predict(data)[0]