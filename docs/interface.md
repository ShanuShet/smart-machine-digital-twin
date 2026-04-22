#  Interfaces

##  Overview
Interfaces define how different components of the system interact with each other.

---

##  1. Data Interface

### Input:
- Air Temperature  
- Process Temperature  
- Speed  
- Torque  
- Wear  

### Output:
- Structured data dictionary  

---

##  2. Model Interface

### Function:
predict_failure(air, process, speed, torque, wear)

### Input:
Sensor values
### Output:
0 → Healthy
1 → Failure

---

## 3. UI Interface (Streamlit)
### Input:
Model prediction
Sensor data
### Output:
Dashboard visualization
Graphs
Machine status

---

## 4. File Interface
### Files Used:
model.pkl
accuracy.pkl
test_data.pkl

---

## Summary
Interfaces ensure smooth communication between modules, making the system efficient and maintainable.
