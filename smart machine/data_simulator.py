import numpy as np

def generate_data():
    return {
        "air_temp": round(np.random.uniform(295, 310), 2),
        "process_temp": round(np.random.uniform(305, 320), 2),
        "speed": round(np.random.uniform(1000, 3000), 2),
        "torque": round(np.random.uniform(10, 70), 2),
        "wear": round(np.random.uniform(0, 250), 2)
    }