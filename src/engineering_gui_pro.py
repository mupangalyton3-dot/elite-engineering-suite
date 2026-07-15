import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------------
# FUNCTIONS
# -------------------------------

def calculate_reynolds():
    try:
        density = float(density_entry.get())
        velocity = float(velocity_entry.get())
        diameter = float(diameter_entry.get())
        viscosity = float(viscosity_entry.get())

        Re = (density * velocity * diameter) / viscosity

        if Re < 2000:
            flow = "Laminar"
        elif Re <= 4000:
            flow = "Transitional"
        else:
            flow = "Turbulent"

        result_label.config(text=f"Re = {Re:.2f} → {flow}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")


def calculate_flow_rate():
    try:
        diameter = float(flow_diameter_entry.get())
        velocity = float(flow_velocity_entry.get())

        area = 3.14 * (diameter ** 2) / 4
        flow_rate = area * velocity

        flow_result_label.config(text=f"Q = {flow_rate:.4f} m³/s")

    except:
        messagebox.showerror("Error", "Enter valid numbers")


def calculate_bernoulli():
    try:
        P = float(pressure_entry.get())
        v = float(velocity_b_entry.get())
        h = float(height_entry.get())
        rho = float(density_b_entry.get())
        g = 9.81

        result = P + 0.5 * rho * v**2 + rho * g * h

        bernoulli_result.config(text=f"Total Energy = {result:.2f}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")


# -------------------------------
# MAIN WINDOW
# -------------------------------

root = tk.Tk()
root.title("Engineering Calculator Pro")
root.geometry("500x450")
root.configure(bg="#f0f4f7")

# -------------------------------
# STYLE
# -------------------------------

style = ttk.Style()
style.configure("TNotebook.Tab", font=("Arial", 10, "bold"))

# -------------------------------
# TABS
# -------------------------------

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

tab1 = tk.Frame(notebook, bg="#f0f4f7")
tab2 = tk.Frame(notebook, bg="#f0f4f7")
tab3 = tk.Frame(notebook, bg="#f0f4f7")

notebook.add(tab1, text="Reynolds")
notebook.add(tab2, text="Flow Rate")
notebook.add(tab3, text="Bernoulli")

# ===============================
# TAB 1: REYNOLDS
# ===============================

tk.Label(tab1, text="Reynolds Number", font=("Arial", 14, "bold"), bg="#f0f4f7").pack(pady=10)

density_entry = tk.Entry(tab1)
velocity_entry = tk.Entry(tab1)
diameter_entry = tk.Entry(tab1)
viscosity_entry = tk.Entry(tab1)

for label, entry in [
    ("Density (kg/m³)", density_entry),
    ("Velocity (m/s)", velocity_entry),
    ("Diameter (m)", diameter_entry),
    ("Viscosity (Pa.s)", viscosity_entry),
]:
    tk.Label(tab1, text=label, bg="#f0f4f7").pack()
    entry.pack(pady=2)

tk.Button(tab1, text="Calculate", bg="#4CAF50", fg="white",
          command=calculate_reynolds).pack(pady=8)

result_label = tk.Label(tab1, text="", fg="blue", bg="#f0f4f7")
result_label.pack()

# ===============================
# TAB 2: FLOW RATE
# ===============================

tk.Label(tab2, text="Flow Rate", font=("Arial", 14, "bold"), bg="#f0f4f7").pack(pady=10)

flow_diameter_entry = tk.Entry(tab2)
flow_velocity_entry = tk.Entry(tab2)

for label, entry in [
    ("Diameter (m)", flow_diameter_entry),
    ("Velocity (m/s)", flow_velocity_entry),
]:
    tk.Label(tab2, text=label, bg="#f0f4f7").pack()
    entry.pack(pady=2)

tk.Button(tab2, text="Calculate", bg="#2196F3", fg="white",
          command=calculate_flow_rate).pack(pady=8)

flow_result_label = tk.Label(tab2, text="", fg="green", bg="#f0f4f7")
flow_result_label.pack()

# ===============================
# TAB 3: BERNOULLI
# ===============================

tk.Label(tab3, text="Bernoulli Equation", font=("Arial", 14, "bold"), bg="#f0f4f7").pack(pady=10)

pressure_entry = tk.Entry(tab3)
velocity_b_entry = tk.Entry(tab3)
height_entry = tk.Entry(tab3)
density_b_entry = tk.Entry(tab3)

for label, entry in [
    ("Pressure (Pa)", pressure_entry),
    ("Velocity (m/s)", velocity_b_entry),
    ("Height (m)", height_entry),
    ("Density (kg/m³)", density_b_entry),
]:
    tk.Label(tab3, text=label, bg="#f0f4f7").pack()
    entry.pack(pady=2)

tk.Button(tab3, text="Calculate", bg="#FF5722", fg="white",
          command=calculate_bernoulli).pack(pady=8)

bernoulli_result = tk.Label(tab3, text="", fg="purple", bg="#f0f4f7")
bernoulli_result.pack()

# -------------------------------
# RUN
# -------------------------------

root.mainloop()