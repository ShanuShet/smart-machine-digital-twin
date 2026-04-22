#  AI Smart Machine Digital Twin

##  Project Overview
This project implements a **Digital Twin system** for monitoring machine health using Artificial Intelligence.  
A virtual machine is created that simulates real industrial machine behavior and predicts failures in real time.

---

##  Objectives
- Simulate a machine using virtual sensor data  
- Predict machine health using Machine Learning  
- Display real-time monitoring dashboard  
- Reduce downtime using predictive maintenance  

---

##  Features
-  Digital Twin Machine Visualization  
-  AI-based Failure Prediction (Random Forest)  
-  Real-time Monitoring Dashboard (Streamlit)  
-  Live Graphs and Data Visualization  
-  Data History Tracking  

---

##  Technologies Used
- Python  
- Streamlit  
- Scikit-learn  
- Pandas, NumPy  
- Matplotlib  

---

##  Project Structure
project/
│── README.md
│── smart machine/
│ ├── app.py
│ ├── model.py
│ ├── virtual_machine.py
│ ├── train_model.py
│ └── predictive_maintenance.csv
│── docs/
│ ├── architecture.md
│ ├── design.md
│ ├── interfaces.md
│── tests/

---

## How to Run the Project

### 1. Install Requirements
pip install -r requirements.txt
### 2. Train Model
python train_model.py
### 3. Run Application
streamlit run app.py
---
## Output
- Machine Health Status (Healthy / Failure)
- Real-time Sensor Data
- Performance Metrics
- Feature Importance
- Live Monitoring Graph
---
## Use Cases
- Industrial Monitoring
- Predictive Maintenance
- Smart Manufacturing
- IoT-based Systems
---
## Conclusion
This project demonstrates how Digital Twin technology combined with AI can improve machine monitoring, reduce failures, and optimize industrial processes
