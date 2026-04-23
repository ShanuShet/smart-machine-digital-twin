import numpy as np
from model import predict_failure


class VirtualMachine:

    def __init__(self):
        # Sensor values
        self.air_temp = None
        self.process_temp = None
        self.speed = None
        self.torque = None
        self.wear = None
        self.status = None

    # 🔹 Simulate sensor readings
    def generate_sensors(self):
        self.air_temp = round(np.random.uniform(295, 310), 2)
        self.process_temp = round(np.random.uniform(305, 320), 2)
        self.speed = round(np.random.uniform(1000, 3000), 2)
        self.torque = round(np.random.uniform(10, 70), 2)
        self.wear = round(np.random.uniform(0, 250), 2)

    # 🔹 Run prediction model
    def predict(self):
        self.status = predict_failure(
            self.air_temp,
            self.process_temp,
            self.speed,
            self.torque,
            self.wear
        )

    # 🔹 Return current machine state
    def get_state(self):
        return dict(
            air_temp=self.air_temp,
            process_temp=self.process_temp,
            speed=self.speed,
            torque=self.torque,
            wear=self.wear,
            status=self.status
        )