import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# -----------------------------
# 🎨 PAGE CONFIG (Silicon UI)
# -----------------------------
st.set_page_config(
    page_title="Elite Engineering AI Suite",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# 💎 CUSTOM STYLING
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.main {
    background: linear-gradient(135deg, #0e1117, #111827);
}
h1, h2, h3 {
    color: #00f5d4;
}
.stButton>button {
    background: linear-gradient(90deg, #00f5d4, #00bbf9);
    color: black;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 🧠 HEADER
# -----------------------------
st.title("🚀 Elite Engineering AI Dashboard")
st.markdown("### AI-Optimized Bio-System Simulation + Cost + Carbon Intelligence")

# -----------------------------
# ⚙️ SIDEBAR INPUTS
# -----------------------------
st.sidebar.header("⚙️ System Controls")

growth_rate = st.sidebar.slider("Growth Rate", 0.1, 2.0, 1.0)
carrying_capacity = st.sidebar.slider("Carrying Capacity", 10, 100, 50)
initial_population = st.sidebar.slider("Initial Population", 1, 10, 2)

cost_per_unit = st.sidebar.slider("Cost per Unit ($)", 1, 20, 5)
carbon_per_unit = st.sidebar.slider("Carbon Emission per Unit (kg)", 0.1, 5.0, 1.0)

# -----------------------------
# 📊 MODEL (Logistic Growth)
# -----------------------------
def model(P, t, r, K):
    return r * P * (1 - P / K)

t = np.linspace(0, 10, 100)
solution = odeint(model, initial_population, t, args=(growth_rate, carrying_capacity))

population = solution.flatten()

# -----------------------------
# 💰 COST + 🌱 CARBON
# -----------------------------
cost = population * cost_per_unit
carbon = population * carbon_per_unit

# -----------------------------
# 🤖 AI OPTIMIZATION ENGINE
# -----------------------------
def optimize():
    best_score = -1e9
    best_r = 0

    for r in np.linspace(0.1, 2.0, 50):
        sol = odeint(model, initial_population, t, args=(r, carrying_capacity))
        pop = sol[-1][0]

        revenue = pop * 10
        cost_val = pop * cost_per_unit
        carbon_penalty = pop * carbon_per_unit * 2

        score = revenue - cost_val - carbon_penalty

        if score > best_score:
            best_score = score
            best_r = r

    return best_r, best_score

opt_r, opt_score = optimize()

# -----------------------------
# 📈 LAYOUT (Silicon style)
# -----------------------------
col1, col2 = st.columns(2)

# 📊 Population Graph
with col1:
    st.subheader("📊 Growth Simulation")
    fig, ax = plt.subplots()
    ax.plot(t, population)
    ax.set_xlabel("Time")
    ax.set_ylabel("Population")
    st.pyplot(fig)

# 💰 Cost + Carbon
with col2:
    st.subheader("💰 Cost & 🌱 Carbon")
    fig2, ax2 = plt.subplots()
    ax2.plot(t, cost, label="Cost")
    ax2.plot(t, carbon, label="Carbon")
    ax2.legend()
    st.pyplot(fig2)

# -----------------------------
# 🤖 AI RESULTS PANEL
# -----------------------------
st.markdown("---")
st.subheader("🤖 AI Optimization Engine")

st.success(f"✅ Optimal Growth Rate: {opt_r:.2f}")
st.info(f"💡 AI Score (Profit - Cost - Carbon): {opt_score:.2f}")

# -----------------------------
# 🎯 KPI CARDS
# -----------------------------
st.markdown("### 📊 Key Metrics")

col3, col4, col5 = st.columns(3)

col3.metric("Final Population", f"{population[-1]:.2f}")
col4.metric("Total Cost", f"${cost[-1]:.2f}")
col5.metric("Carbon Impact", f"{carbon[-1]:.2f} kg")

# -----------------------------
# 🚀 FOOTER
# -----------------------------
st.markdown("---")
st.markdown("Built with ❤️ by Elite Engineering Suite | AI Powered")