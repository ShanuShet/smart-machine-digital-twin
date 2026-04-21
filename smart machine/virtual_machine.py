import numpy as np
from model import predict_failure

class VirtualMachine:

    def __init__(self):
        self.air_temp = 0
        self.process_temp = 0
        self.speed = 0
        self.torque = 0
        self.wear = 0
        self.status = 0

    # 🔹 Generate sensor data
    def generate_sensors(self):
        self.air_temp = round(np.random.uniform(295, 310), 2)
        self.process_temp = round(np.random.uniform(305, 320), 2)
        self.speed = round(np.random.uniform(1000, 3000), 2)
        self.torque = round(np.random.uniform(10, 70), 2)
        self.wear = round(np.random.uniform(0, 250), 2)

    # 🔹 Predict machine health
    def predict(self):
        self.status = predict_failure(
            self.air_temp,
            self.process_temp,
            self.speed,
            self.torque,
            self.wear
        )

    # 🔹 Get machine state
    def get_state(self):
        return {
            "air_temp": self.air_temp,
            "process_temp": self.process_temp,
            "speed": self.speed,
            "torque": self.torque,
            "wear": self.wear,
            "status": self.status
        }