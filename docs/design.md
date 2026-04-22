#  System Design

##  Overview
The system is designed using a modular approach for easy development and maintenance.

---

##  Modules

### 1. Data Generation Module
- File: `virtual_machine.py`
- Generates sensor values

---

### 2. Prediction Module
- File: `model.py`
- Uses trained ML model
- Returns machine status

---

### 3. Training Module
- File: `train_model.py`
- Trains Random Forest model
- Saves model using joblib

---

### 4. User Interface Module
- File: `app.py`
- Built using Streamlit
- Displays all outputs

---

##  Workflow
Generate Data → Predict → Display → Repeat


---

##  Design Goals
- Simplicity  
- Real-time updates  
- Modular structure  
- Easy scalability  

---
