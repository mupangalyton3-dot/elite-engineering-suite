import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sqlite3
from sklearn.linear_model import LinearRegression

# -----------------------------
# 🧠 DATABASE SETUP
# -----------------------------
conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

# -----------------------------
# 🔐 AUTH SYSTEM
# -----------------------------
def login(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()

def signup(username, password):
    c.execute("INSERT INTO users VALUES (?,?)", (username, password))
    conn.commit()

# -----------------------------
# 🎨 UI CONFIG
# -----------------------------
st.set_page_config(page_title="Elite AI SaaS", layout="wide")

st.markdown("""
<style>
body { background-color: #0e1117; color: white; }
h1, h2 { color: #00f5d4; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 🔑 LOGIN UI
# -----------------------------
st.sidebar.title("🔐 Login")

auth_mode = st.sidebar.radio("Choose", ["Login", "Sign Up"])

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if auth_mode == "Sign Up":
    if st.sidebar.button("Create Account"):
        signup(username, password)
        st.sidebar.success("Account created!")

if auth_mode == "Login":
    if st.sidebar.button("Login"):
        if login(username, password):
            st.session_state["user"] = username
            st.success(f"Welcome {username}")
        else:
            st.error("Invalid credentials")

# -----------------------------
# 🚫 BLOCK IF NOT LOGGED IN
# -----------------------------
if "user" not in st.session_state:
    st.warning("Please login to continue")
    st.stop()

# -----------------------------
# 🚀 MAIN DASHBOARD
# -----------------------------
st.title("🚀 Elite Engineering AI SaaS")

# Sidebar Inputs
st.sidebar.header("Controls")

growth_rate = st.sidebar.slider("Growth Rate", 0.1, 2.0, 1.0)
carrying_capacity = st.sidebar.slider("Capacity", 10, 100, 50)
initial_population = st.sidebar.slider("Initial Pop", 1, 10, 2)

cost_per_unit = st.sidebar.slider("Cost", 1, 20, 5)
carbon_per_unit = st.sidebar.slider("Carbon", 0.1, 5.0, 1.0)

# -----------------------------
# 📊 MODEL
# -----------------------------
def model(P, t, r, K):
    return r * P * (1 - P / K)

t = np.linspace(0, 10, 100)
solution = odeint(model, initial_population, t, args=(growth_rate, carrying_capacity))
population = solution.flatten()

# -----------------------------
# 🤖 REAL MACHINE LEARNING
# -----------------------------
X = population.reshape(-1, 1)
y = population * 10 - population * cost_per_unit - population * carbon_per_unit

ml_model = LinearRegression()
ml_model.fit(X, y)

predicted_profit = ml_model.predict(X)

# -----------------------------
# 📈 UI LAYOUT
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Growth")
    fig, ax = plt.subplots()
    ax.plot(t, population)
    st.pyplot(fig)

with col2:
    st.subheader("🤖 ML Profit Prediction")
    fig2, ax2 = plt.subplots()
    ax2.plot(t, predicted_profit)
    st.pyplot(fig2)

# -----------------------------
# 📊 METRICS
# -----------------------------
st.markdown("### Key Metrics")

col3, col4, col5 = st.columns(3)

col3.metric("Final Population", f"{population[-1]:.2f}")
col4.metric("Predicted Profit", f"${predicted_profit[-1]:.2f}")
col5.metric("Carbon Impact", f"{(population[-1]*carbon_per_unit):.2f} kg")

st.markdown("---")
st.markdown("AI SaaS | Built by Elite Engineering Suite 🚀")