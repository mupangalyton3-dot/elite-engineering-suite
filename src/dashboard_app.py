import streamlit as st
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

st.title("🌱 AI-Optimized Algae Carbon Capture System")

# ==============================
# USER INPUTS
# ==============================

I0 = st.slider("Light Intensity", 50, 400, 200)
kLa = st.slider("Mass Transfer (kLa)", 0.1, 1.0, 0.5)
H = st.slider("Reactor Depth (m)", 0.1, 1.0, 0.5)

# Constants
mu_max = 0.09
Ks = 0.03
Ki = 50
Yx_co2 = 1.8
k_light = 0.15

X0, C0 = 0.1, 0.02
y0 = [X0, C0]
t = np.linspace(0, 100, 300)

# ==============================
# MODEL
# ==============================

def avg_light(X):
    if X < 1e-6:
        return I0
    return (I0 / (k_light * X * H)) * (1 - np.exp(-k_light * X * H))

def model(y, t):
    X, C = y
    I_avg = avg_light(X)

    mu = mu_max * (C / (Ks + C)) * (I_avg / (Ki + I_avg))
    dXdt = mu * X

    CO2_consumption = (1 / Yx_co2) * dXdt
    CO2_transfer = kLa * (0.04 - C)

    dCdt = CO2_transfer - CO2_consumption

    return [dXdt, dCdt]

sol = odeint(model, y0, t)
X = sol[:, 0]
C = sol[:, 1]

# ==============================
# METRICS
# ==============================

CO2_captured = (C0 - C[-1]) * 1000  # scaled
profit = CO2_captured * 0.05 - (I0 * 0.01)

# ==============================
# OUTPUT
# ==============================

st.subheader("📊 Results")

st.write(f"Final Biomass: {X[-1]:.2f} g/L")
st.write(f"CO₂ Captured: {CO2_captured:.2f}")
st.write(f"Estimated Profit: ${profit:.2f}")

# Plot
fig, ax = plt.subplots()
ax.plot(t, X, label="Biomass")
ax.plot(t, C, label="CO₂")
ax.legend()
ax.set_xlabel("Time")
ax.set_ylabel("Concentration")

st.pyplot(fig)