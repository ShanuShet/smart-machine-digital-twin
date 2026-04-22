
#  System Architecture

##  Overview
The system follows a **Digital Twin Architecture** where a virtual model represents a real machine.

---

##  Architecture Flow
Virtual Sensors → Data Simulator → AI Model → Prediction → Dashboard


---

##  Components

### 1. Virtual Machine
- Simulates machine behavior
- Generates sensor data

### 2. Data Simulator
- Produces random values for:
  - Temperature
  - Speed
  - Torque
  - Wear

### 3. Machine Learning Model
- Algorithm: Random Forest
- Predicts machine condition:
  - 0 → Healthy
  - 1 → Failure

### 4. Dashboard (Streamlit)
- Displays real-time data
- Shows machine status
- Visualizes graphs

---

##  Interaction Between Components

1. Virtual machine generates data  
2. Data is passed to ML model  
3. Model predicts health  
4. Results shown in dashboard  

---

##  Key Advantage
- Real-time monitoring  
- Early failure detection  
- Scalable architecture  

---
