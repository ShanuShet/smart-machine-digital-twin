import streamlit as st
import time
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from virtual_machine import VirtualMachine

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Digital Twin", layout="wide")

# ---------------- TITLE ----------------
st.title("🏭 AI Smart Machine Digital Twin")

# ---------------- LOAD MODEL DATA ----------------
accuracy = joblib.load("accuracy.pkl")
X_test, y_test, y_pred = joblib.load("test_data.pkl")
model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

# ---------------- SIDEBAR ----------------
st.sidebar.header("Controls")
run = st.sidebar.button("▶ Start Simulation")
stop = st.sidebar.button("⏹ Stop")
speed = st.sidebar.slider("⏱ Simulation Speed", 0.1, 2.0, 0.5)

# ---------------- SESSION STATE ----------------
if "data" not in st.session_state:
    st.session_state.data = []

if "running" not in st.session_state:
    st.session_state.running = False

if run:
    st.session_state.running = True

if stop:
    st.session_state.running = False

# ---------------- MODEL PERFORMANCE ----------------
st.subheader("📊 Model Performance")

col1, col2 = st.columns(2)

col1.metric("🎯 Accuracy", f"{accuracy*100:.2f}%")

with col2:
    fig, ax = plt.subplots()
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(cm)
    disp.plot(ax=ax)
    st.pyplot(fig)

# ---------------- FEATURE IMPORTANCE ----------------
st.subheader("📈 Feature Importance")

importances = model.feature_importances_

feat_df = pd.DataFrame({
    "Feature": features,
    "Importance": importances
}).sort_values(by="Importance", ascending=False)

st.bar_chart(feat_df.set_index("Feature"))

# ---------------- DIGITAL TWIN PANEL ----------------
st.subheader("🏭 Digital Twin Machine Model")

machine_box = st.empty()

# ---------------- LIVE GRAPH ----------------
st.subheader("📈 Live Monitoring")

graph_box = st.empty()

vm = VirtualMachine()

# -------- INITIAL VIEW --------
with machine_box.container():
    st.markdown("## 🏭 Machine Digital Twin")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("machine.png", width=300)

    with col2:
        st.info("Click ▶ Start Simulation to begin")

# ---------------- MAIN UPDATE ----------------
if st.session_state.running:

    vm.generate_sensors()
    vm.predict()

    data = vm.get_state()
    st.session_state.data.append(data)

    with machine_box.container():
        st.markdown("## 🏭 Machine Digital Twin")

        col1, col2 = st.columns([1, 2])

        # MACHINE IMAGE
        with col1:
            st.image("machine.png", width=300)

        # STATUS PANEL
        with col2:

            if data["status"] == 1:
                st.markdown(
                    "<h1 style='color:red;'>🔴 MACHINE FAILURE</h1>",
                    unsafe_allow_html=True
                )

                st.image(
                    "https://cdn-icons-png.flaticon.com/512/564/564619.png",
                    width=120
                )

                st.error("⚠️ Fault detected in system")

            else:
                st.markdown(
                    "<h1 style='color:limegreen;'>🟢 MACHINE HEALTHY</h1>",
                    unsafe_allow_html=True
                )

                st.image(
                    "https://cdn-icons-png.flaticon.com/512/190/190411.png",
                    width=120
                )

                st.success("Running Normally")

            st.markdown("---")

            # PARAMETERS
            st.markdown("### ⚙️ Machine Parameters")

            c1, c2, c3 = st.columns(3)
            c1.metric("🌡 Air Temp", data["air_temp"])
            c2.metric("🔥 Process Temp", data["process_temp"])
            c3.metric("⚡ Speed", data["speed"])

            c4, c5 = st.columns(2)
            c4.metric("🔩 Torque", data["torque"])
            c5.metric("🛠 Wear", data["wear"])

    # -------- GRAPH --------
    with graph_box.container():
        df = pd.DataFrame(st.session_state.data)

        st.line_chart(df[[
            "air_temp", "process_temp", "speed", "torque", "wear"
        ]])

    time.sleep(speed)
    st.rerun()

# ---------------- DATA HISTORY ----------------
if st.session_state.data:
    st.subheader("📁 Data History")
    st.dataframe(pd.DataFrame(st.session_state.data).tail(100))