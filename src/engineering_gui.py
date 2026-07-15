import tkinter as tk
from tkinter import messagebox

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
        messagebox.showerror("Error", "Please enter valid numbers")


def calculate_flow_rate():
    try:
        diameter = float(flow_diameter_entry.get())
        velocity = float(flow_velocity_entry.get())

        area = 3.14 * (diameter ** 2) / 4
        flow_rate = area * velocity

        flow_result_label.config(text=f"Flow Rate: {flow_rate:.4f} m³/s")

    except:
        messagebox.showerror("Error", "Please enter valid numbers")


# -------------------------------
# MAIN WINDOW
# -------------------------------

root = tk.Tk()
root.title("Engineering Calculator")
root.geometry("420x500")

# -------------------------------
# TITLE
# -------------------------------

tk.Label(root, text="ENGINEERING CALCULATOR", font=("Arial", 14, "bold")).pack(pady=10)

# ===============================
# REYNOLDS SECTION
# ===============================

tk.Label(root, text="--- Reynolds Number ---", font=("Arial", 12)).pack()

tk.Label(root, text="Density (kg/m³)").pack()
density_entry = tk.Entry(root)
density_entry.pack()

tk.Label(root, text="Velocity (m/s)").pack()
velocity_entry = tk.Entry(root)
velocity_entry.pack()

tk.Label(root, text="Diameter (m)").pack()
diameter_entry = tk.Entry(root)
diameter_entry.pack()

tk.Label(root, text="Viscosity (Pa.s)").pack()
viscosity_entry = tk.Entry(root)
viscosity_entry.pack()

tk.Button(root, text="Calculate Reynolds", command=calculate_reynolds).pack(pady=5)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=5)

# ===============================
# FLOW RATE SECTION
# ===============================

tk.Label(root, text="--- Flow Rate ---", font=("Arial", 12)).pack(pady=10)

tk.Label(root, text="Diameter (m)").pack()
flow_diameter_entry = tk.Entry(root)
flow_diameter_entry.pack()

tk.Label(root, text="Velocity (m/s)").pack()
flow_velocity_entry = tk.Entry(root)
flow_velocity_entry.pack()

tk.Button(root, text="Calculate Flow Rate", command=calculate_flow_rate).pack(pady=5)

flow_result_label = tk.Label(root, text="", fg="green")
flow_result_label.pack(pady=5)

# -------------------------------
# RUN APP
# -------------------------------

root.mainloop()