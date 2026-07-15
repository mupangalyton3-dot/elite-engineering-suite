import tkinter as tk
import json
import os
import random

# =========================
# FILE
# =========================
SAVE_FILE = "chats.json"

def load_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return {"chats": {}, "current": None}

def save_data():
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

# =========================
# AI RESPONSE
# =========================
def ai_response(prompt):
    return random.choice([
        "That’s interesting…",
        "Tell me more.",
        "Let’s break that down.",
        "You're onto something.",
        "Think deeper."
    ])

# =========================
# CHAT MANAGEMENT
# =========================
def new_chat():
    name = f"Chat {len(data['chats']) + 1}"
    data["chats"][name] = []
    data["current"] = name
    update_sidebar()
    render_chat()
    save_data()

def switch_chat(name):
    data["current"] = name
    render_chat()
    save_data()

def update_sidebar():
    for widget in sidebar_frame.winfo_children():
        widget.destroy()

    for chat in data["chats"]:
        btn = tk.Button(
            sidebar_frame,
            text=chat,
            bg="#2a2a2a",
            fg="white",
            relief=tk.FLAT,
            command=lambda c=chat: switch_chat(c)
        )
        btn.pack(fill=tk.X, pady=2, padx=5)

# =========================
# CHAT RENDER (BUBBLES)
# =========================
def render_chat():
    for widget in chat_area.winfo_children():
        widget.destroy()

    current = data["current"]
    if not current:
        return

    for msg in data["chats"][current]:
        add_bubble(msg["text"], msg["sender"])

# =========================
# ADD CHAT BUBBLE
# =========================
def add_bubble(text, sender):
    frame = tk.Frame(chat_area, bg="#121212")

    if sender == "user":
        bubble = tk.Label(
            frame,
            text=text,
            bg="#00ffcc",
            fg="black",
            wraplength=300,
            justify="left",
            padx=10,
            pady=5
        )
        bubble.pack(anchor="e", padx=10, pady=5)

    else:
        bubble = tk.Label(
            frame,
            text=text,
            bg="#2a2a2a",
            fg="white",
            wraplength=300,
            justify="left",
            padx=10,
            pady=5
        )
        bubble.pack(anchor="w", padx=10, pady=5)

    frame.pack(fill=tk.X)

# =========================
# SEND MESSAGE
# =========================
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return

    if not data["current"]:
        new_chat()

    current = data["current"]

    # SAVE USER
    data["chats"][current].append({
        "sender": "user",
        "text": user_input
    })

    # AI RESPONSE
    response = ai_response(user_input)

    data["chats"][current].append({
        "sender": "ai",
        "text": response
    })

    save_data()
    render_chat()

    entry.delete(0, tk.END)

# =========================
# GUI
# =========================
root = tk.Tk()
root.title("Elite AI Interface")
root.geometry("1000x650")
root.configure(bg="#121212")

# SIDEBAR
sidebar_frame = tk.Frame(root, bg="#1e1e1e", width=220)
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

new_btn = tk.Button(
    sidebar_frame,
    text="+ New Chat",
    bg="#00ffcc",
    fg="black",
    command=new_chat
)
new_btn.pack(fill=tk.X, pady=10, padx=5)

# CHAT CONTAINER
chat_container = tk.Frame(root, bg="#121212")
chat_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# SCROLLABLE CANVAS
canvas = tk.Canvas(chat_container, bg="#121212", highlightthickness=0)
scrollbar = tk.Scrollbar(chat_container, command=canvas.yview)
chat_area = tk.Frame(canvas, bg="#121212")

chat_area.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=chat_area, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# INPUT AREA
input_frame = tk.Frame(root, bg="#121212")
input_frame.pack(fill=tk.X, side=tk.BOTTOM)

entry = tk.Entry(
    input_frame,
    bg="#2a2a2a",
    fg="white",
    insertbackground="white",
    font=("Consolas", 12)
)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

send_btn = tk.Button(
    input_frame,
    text="Send",
    bg="#00ffcc",
    command=send_message
)
send_btn.pack(side=tk.RIGHT, padx=10)

# INIT
update_sidebar()
root.mainloop()