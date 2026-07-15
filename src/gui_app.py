# =========================================
# ENGINEERING GUI SYSTEM (ALL-IN-ONE)
# =========================================

import tkinter as tk
from tkinter import messagebox
import json

# -------------------------------
# DATA STORAGE
# -------------------------------
data = []

FILE_NAME = "data.json"


# -------------------------------
# SAVE DATA
# -------------------------------
def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)


# -------------------------------
# LOAD DATA
# -------------------------------
def load_data():
    global data
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
    except:
        data = []


# -------------------------------
# ADD ITEM
# -------------------------------
def add_item():
    name = name_entry.get()
    value = value_entry.get()

    if name == "" or value == "":
        messagebox.showwarning("Input Error", "Fill all fields!")
        return

    data.append({"name": name, "value": value})
    save_data()
    update_list()

    name_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)


# -------------------------------
# DELETE ITEM
# -------------------------------
def delete_item():
    try:
        selected = listbox.curselection()[0]
        data.pop(selected)
        save_data()
        update_list()
    except:
        messagebox.showwarning("Error", "Select an item!")


# -------------------------------
# UPDATE DISPLAY
# -------------------------------
def update_list():
    listbox.delete(0, tk.END)
    for item in data:
        listbox.insert(tk.END, f"{item['name']} = {item['value']}")


# -------------------------------
# REYNOLDS CALCULATOR
# -------------------------------
def calculate_reynolds():
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

        result_label.config(text=f"Re = {Re:.2f} ({flow})")

    except:
        messagebox.showerror("Error", "Invalid input!")


# -------------------------------
# GUI SETUP
# -------------------------------
root = tk.Tk()
root.title("Engineering System 👑")
root.geometry("500x600")


# -------------------------------
# INPUT SECTION
# -------------------------------
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Value").pack()
value_entry = tk.Entry(root)
value_entry.pack()

tk.Button(root, text="Add", command=add_item).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_item).pack(pady=5)


# -------------------------------
# LIST DISPLAY
# -------------------------------
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)


# -------------------------------
# REYNOLDS SECTION
# -------------------------------
tk.Label(root, text="--- Reynolds Calculator ---").pack()

entry_density = tk.Entry(root)
entry_density.insert(0, "Density")
entry_density.pack()

entry_velocity = tk.Entry(root)
entry_velocity.insert(0, "Velocity")
entry_velocity.pack()

entry_diameter = tk.Entry(root)
entry_diameter.insert(0, "Diameter")
entry_diameter.pack()

entry_viscosity = tk.Entry(root)
entry_viscosity.insert(0, "Viscosity")
entry_viscosity.pack()

tk.Button(root, text="Calculate", command=calculate_reynolds).pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()


# -------------------------------
# LOAD DATA ON START
# -------------------------------
load_data()
update_list()


# -------------------------------
# RUN APP
# -------------------------------
root.mainloop()