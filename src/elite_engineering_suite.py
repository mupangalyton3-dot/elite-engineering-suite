# =========================================
# ELITE ENGINEERING SUITE 👑 (ALL-IN-ONE)
# =========================================

import tkinter as tk
from tkinter import ttk, messagebox
import json
import matplotlib.pyplot as plt
from openpyxl import Workbook

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
# EXPORT TO EXCEL
# -------------------------------
def export_excel():
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"

    ws.append(["Name", "Value"])

    for item in data:
        ws.append([item["name"], item["value"]])

    wb.save("engineering_data.xlsx")
    messagebox.showinfo("Success", "Exported to Excel!")

# -------------------------------
# GRAPH
# -------------------------------
def plot_graph():
    try:
        names = [item["name"] for item in data]
        values = [float(item["value"]) for item in data]

        plt.figure()
        plt.plot(names, values, marker='o')
        plt.title("Engineering Data Graph")
        plt.xlabel("Items")
        plt.ylabel("Values")
        plt.show()

    except:
        messagebox.showerror("Error", "Ensure values are numbers!")

# -------------------------------
# REYNOLDS
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
# PRESSURE
# -------------------------------
def calculate_pressure():
    try:
        force = float(entry_force.get())
        area = float(entry_area.get())

        pressure = force / area
        result_pressure.config(text=f"Pressure = {pressure:.2f} Pa")

    except:
        messagebox.showerror("Error", "Invalid input!")

# -------------------------------
# AI ASSISTANT (BASIC)
# -------------------------------
def ai_response():
    question = ai_entry.get().lower()

    if "reynolds" in question:
        answer = "Re = density × velocity × diameter / viscosity"
    elif "pressure" in question:
        answer = "Pressure = Force / Area"
    elif "flow" in question:
        answer = "Laminar <2000, Transitional 2000-4000, Turbulent >4000"
    else:
        answer = "I am your engineering assistant. Ask about Reynolds or Pressure."

    ai_output.config(text=answer)

# -------------------------------
# GUI SETUP
# -------------------------------
root = tk.Tk()
root.title("Lyton Elite Engineering Suite 👑")
root.geometry("700x650")
root.configure(bg="#121212")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# ===============================
# TAB 1: DATA
# ===============================
tab1 = tk.Frame(notebook, bg="#121212")
notebook.add(tab1, text="Data")

tk.Label(tab1, text="Name", bg="#121212", fg="white").pack()
name_entry = tk.Entry(tab1)
name_entry.pack()

tk.Label(tab1, text="Value", bg="#121212", fg="white").pack()
value_entry = tk.Entry(tab1)
value_entry.pack()

tk.Button(tab1, text="Add", command=add_item).pack(pady=5)
tk.Button(tab1, text="Delete", command=delete_item).pack(pady=5)

tk.Button(tab1, text="Export Excel", command=export_excel).pack(pady=5)
tk.Button(tab1, text="Plot Graph", command=plot_graph).pack(pady=5)

listbox = tk.Listbox(tab1, width=50)
listbox.pack(pady=10)

# ===============================
# TAB 2: REYNOLDS
# ===============================
tab2 = tk.Frame(notebook, bg="#121212")
notebook.add(tab2, text="Reynolds")

entry_density = tk.Entry(tab2)
entry_density.insert(0, "Density")
entry_density.pack()

entry_velocity = tk.Entry(tab2)
entry_velocity.insert(0, "Velocity")
entry_velocity.pack()

entry_diameter = tk.Entry(tab2)
entry_diameter.insert(0, "Diameter")
entry_diameter.pack()

entry_viscosity = tk.Entry(tab2)
entry_viscosity.insert(0, "Viscosity")
entry_viscosity.pack()

tk.Button(tab2, text="Calculate", command=calculate_re).pack()

result_re = tk.Label(tab2, text="", fg="cyan", bg="#121212")
result_re.pack()

# ===============================
# TAB 3: PRESSURE
# ===============================
tab3 = tk.Frame(notebook, bg="#121212")
notebook.add(tab3, text="Pressure")

entry_force = tk.Entry(tab3)
entry_force.insert(0, "Force")
entry_force.pack()

entry_area = tk.Entry(tab3)
entry_area.insert(0, "Area")
entry_area.pack()

tk.Button(tab3, text="Calculate", command=calculate_pressure).pack()

result_pressure = tk.Label(tab3, text="", fg="cyan", bg="#121212")
result_pressure.pack()

# ===============================
# TAB 4: AI ASSISTANT
# ===============================
tab4 = tk.Frame(notebook, bg="#121212")
notebook.add(tab4, text="AI Assistant")

ai_entry = tk.Entry(tab4, width=40)
ai_entry.pack(pady=10)

tk.Button(tab4, text="Ask", command=ai_response).pack()

ai_output = tk.Label(tab4, text="", fg="cyan", bg="#121212", wraplength=400)
ai_output.pack(pady=10)

# -------------------------------
# LOAD DATA
# -------------------------------
load_data()
update_list()

# -------------------------------
# RUN
# -------------------------------
root.mainloop()