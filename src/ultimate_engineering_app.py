# =========================================
# ULTIMATE ENGINEERING APP (INSANE MODE)
# =========================================

import tkinter as tk
from tkinter import ttk, messagebox
import json

FILE_NAME = "data.json"
data = []


# -------------------------------
# SAVE / LOAD
# -------------------------------
def save_data():
    with open(FILE_NAME, "w") as f:
        json.dump(data, f)

def load_data():
    global data
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
    except:
        data = []


# -------------------------------
# DATA FUNCTIONS
# -------------------------------
def add_item():
    name = name_entry.get()
    value = value_entry.get()

    if name == "" or value == "":
        messagebox.showwarning("Error", "Fill all fields!")
        return

    data.append({"name": name, "value": value})
    save_data()
    update_list()

    name_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)


def delete_item():
    try:
        index = listbox.curselection()[0]
        data.pop(index)
        save_data()
        update_list()
    except:
        messagebox.showwarning("Error", "Select item!")


def update_list():
    listbox.delete(0, tk.END)
    for item in data:
        listbox.insert(tk.END, f"{item['name']} = {item['value']}")


# -------------------------------
# REYNOLDS CALCULATOR
# -------------------------------
def calculate_re():
    try:
        d = float(entry_density.get())
        v = float(entry_velocity.get())
        dia = float(entry_diameter.get())
        mu = float(entry_viscosity.get())

        Re = (d * v * dia) / mu

        if Re < 2000:
            flow = "Laminar"
        elif Re <= 4000:
            flow = "Transitional"
        else:
            flow = "Turbulent"

        result_re.config(text=f"Re = {Re:.2f} ({flow})")

    except:
        messagebox.showerror("Error", "Invalid input!")


# -------------------------------
# FUTURE CALCULATOR (EXAMPLE)
# -------------------------------
def simple_pressure():
    try:
        force = float(entry_force.get())
        area = float(entry_area.get())

        pressure = force / area
        result_pressure.config(text=f"Pressure = {pressure:.2f} Pa")

    except:
        messagebox.showerror("Error", "Invalid input!")


# -------------------------------
# GUI SETUP
# -------------------------------
root = tk.Tk()
root.title("Lyton Engineering Suite 👑")
root.geometry("600x600")
root.configure(bg="#121212")


# -------------------------------
# NOTEBOOK (TABS)
# -------------------------------
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")


# ===============================
# TAB 1: DATA MANAGER
# ===============================
tab1 = tk.Frame(notebook, bg="#121212")
notebook.add(tab1, text="Data Manager")

tk.Label(tab1, text="Name", bg="#121212", fg="white").pack()
name_entry = tk.Entry(tab1)
name_entry.pack()

tk.Label(tab1, text="Value", bg="#121212", fg="white").pack()
value_entry = tk.Entry(tab1)
value_entry.pack()

tk.Button(tab1, text="Add", command=add_item).pack(pady=5)
tk.Button(tab1, text="Delete Selected", command=delete_item).pack(pady=5)

listbox = tk.Listbox(tab1, width=50)
listbox.pack(pady=10)


# ===============================
# TAB 2: REYNOLDS
# ===============================
tab2 = tk.Frame(notebook, bg="#121212")
notebook.add(tab2, text="Reynolds")

tk.Label(tab2, text="Density", bg="#121212", fg="white").pack()
entry_density = tk.Entry(tab2)
entry_density.pack()

tk.Label(tab2, text="Velocity", bg="#121212", fg="white").pack()
entry_velocity = tk.Entry(tab2)
entry_velocity.pack()

tk.Label(tab2, text="Diameter", bg="#121212", fg="white").pack()
entry_diameter = tk.Entry(tab2)
entry_diameter.pack()

tk.Label(tab2, text="Viscosity", bg="#121212", fg="white").pack()
entry_viscosity = tk.Entry(tab2)
entry_viscosity.pack()

tk.Button(tab2, text="Calculate", command=calculate_re).pack(pady=5)

result_re = tk.Label(tab2, text="", bg="#121212", fg="cyan")
result_re.pack()


# ===============================
# TAB 3: PRESSURE CALCULATOR
# ===============================
tab3 = tk.Frame(notebook, bg="#121212")
notebook.add(tab3, text="Pressure")

tk.Label(tab3, text="Force (N)", bg="#121212", fg="white").pack()
entry_force = tk.Entry(tab3)
entry_force.pack()

tk.Label(tab3, text="Area (m²)", bg="#121212", fg="white").pack()
entry_area = tk.Entry(tab3)
entry_area.pack()

tk.Button(tab3, text="Calculate", command=simple_pressure).pack(pady=5)

result_pressure = tk.Label(tab3, text="", bg="#121212", fg="cyan")
result_pressure.pack()


# -------------------------------
# LOAD DATA
# -------------------------------
load_data()
update_list()


# -------------------------------
# RUN APP
# -------------------------------
root.mainloop()