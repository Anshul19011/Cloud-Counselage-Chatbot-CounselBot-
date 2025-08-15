import tkinter as tk
from tkinter import scrolledtext
import json
from fuzzywuzzy import process

# ======= Load FAQs ========
with open("faqs.json", "r") as f:
    FAQS = json.load(f)

# ======= Bot Logic ========
def get_faq_answer(query):
    questions = list(FAQS.keys())
    match, score = process.extractOne(query.lower(), questions)
    if score > 75:
        return FAQS[match]
    return "I'm not sure about that. Please reach out to support@cloudcounselage.com for help."

def chat():
    user_input = entry.get().strip()
    if not user_input:
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "👤 You: " + user_input + "\n")
    entry.delete(0, tk.END)

    reply = get_faq_answer(user_input)
    chat_area.insert(tk.END, "🤖 CounselBot: " + reply + "\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

# ======= GUI Setup ========
root = tk.Tk()
root.title("Cloud Counselage Chatbot")
root.geometry("600x550")
root.configure(bg="#f4f7fb")

FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_TEXT = ("Segoe UI", 11)

# ======= Header ========
title_label = tk.Label(root, text="Cloud Counselage Chatbot (CounselBot)", font=FONT_TITLE, fg="#003366", bg="#f4f7fb")
title_label.pack(pady=(10, 0))

# ======= Chat Area ========
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=FONT_TEXT, bg="#ffffff", fg="#000000", bd=1, relief=tk.GROOVE)
chat_area.pack(padx=20, pady=10)
chat_area.config(state=tk.DISABLED)

# ======= Input Frame ========
input_frame = tk.Frame(root, bg="#f4f7fb")
input_frame.pack(pady=10)

entry = tk.Entry(input_frame, width=50, font=FONT_TEXT, bd=2)
entry.grid(row=0, column=0, padx=(0, 10))
entry.bind("<Return>", lambda event: chat())

def on_enter(e): send_btn.config(bg="#005f9e")
def on_leave(e): send_btn.config(bg="#007acc")

send_btn = tk.Button(input_frame, text="Send", width=10, command=chat, font=("Segoe UI", 10, "bold"), bg="#007acc", fg="white", activebackground="#005f9e", cursor="hand2")
send_btn.grid(row=0, column=1)
send_btn.bind("<Enter>", on_enter)
send_btn.bind("<Leave>", on_leave)

# ======= Suggested FAQs ========
def send_suggestion(text):
    entry.delete(0, tk.END)
    entry.insert(0, text)
    chat()

suggestion_frame = tk.Frame(root, bg="#f4f7fb")
suggestion_frame.pack(pady=(0, 10))

suggestions = [
    "how to join internship",
    "do i get certificate",
    "what is cloud counselage"
]

for q in suggestions:
    b = tk.Button(suggestion_frame, text=q.title(), command=lambda t=q: send_suggestion(t), font=("Segoe UI", 9), bg="#e1ecf4", fg="#003366", relief=tk.RIDGE, cursor="hand2", padx=5, pady=2)
    b.pack(side=tk.LEFT, padx=5)

# ======= Greeting ========
chat_area.config(state=tk.NORMAL)
chat_area.insert(tk.END, "🤖 CounselBot: Hello! I'm CounselBot from Cloud Counselage.\nHow can I assist you today?\n\n")
chat_area.config(state=tk.)

# ======= Start Mainloop ========
root.mainloop()
