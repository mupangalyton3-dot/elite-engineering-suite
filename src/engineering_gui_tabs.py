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
            flow = "Laminar Flow"
        elif Re <= 4000:
            flow = "Transitional Flow"
        else:
            flow = "Turbulent Flow"

        result_label.config(text=f"Re: {Re:.2f} | {flow}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")


def calculate_flow_rate():
    try:
        diameter = float(flow_diameter_entry.get())
        velocity = float(flow_velocity_entry.get())

        area = 3.14 * (diameter ** 2) / 4
        flow_rate = area * velocity

        flow_result_label.config(text=f"Flow Rate: {flow_rate:.4f} m³/s")

    except:
        messagebox.showerror("Error", "Enter valid numbers")


# -------------------------------
# MAIN WINDOW
# -------------------------------

root = tk.Tk()
root.title("Engineering Calculator Pro")
root.geometry("450x400")

# -------------------------------
# TABS SETUP
# -------------------------------

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Create tabs
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

notebook.add(tab1, text="Reynolds Number")
notebook.add(tab2, text="Flow Rate")

# ===============================
# TAB 1: REYNOLDS
# ===============================

tk.Label(tab1, text="Reynolds Number Calculator", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(tab1, text="Density (kg/m³)").pack()
density_entry = tk.Entry(tab1)
density_entry.pack()

tk.Label(tab1, text="Velocity (m/s)").pack()
velocity_entry = tk.Entry(tab1)
velocity_entry.pack()

tk.Label(tab1, text="Diameter (m)").pack()
diameter_entry = tk.Entry(tab1)
diameter_entry.pack()

tk.Label(tab1, text="Viscosity (Pa.s)").pack()
viscosity_entry = tk.Entry(tab1)
viscosity_entry.pack()

tk.Button(tab1, text="Calculate", command=calculate_reynolds).pack(pady=5)

result_label = tk.Label(tab1, text="", fg="blue")
result_label.pack(pady=5)

# ===============================
# TAB 2: FLOW RATE
# ===============================

tk.Label(tab2, text="Flow Rate Calculator", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(tab2, text="Diameter (m)").pack()
flow_diameter_entry = tk.Entry(tab2)
flow_diameter_entry.pack()

tk.Label(tab2, text="Velocity (m/s)").pack()
flow_velocity_entry = tk.Entry(tab2)
flow_velocity_entry.pack()

tk.Button(tab2, text="Calculate", command=calculate_flow_rate).pack(pady=5)

flow_result_label = tk.Label(tab2, text="", fg="green")
flow_result_label.pack(pady=5)

# -------------------------------
# RUN APP
# -------------------------------

root.mainloop()