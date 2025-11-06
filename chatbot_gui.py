import tkinter as tk
from tkinter import scrolledtext
import datetime, random

memory = {"name": None}

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break… and it said 'No problem, I’ll go to sleep.' 😴",
    "Why did the developer go broke? Because he used up all his cache 💸"
]

facts = [
    "Honey never spoils. Archaeologists have found pots of honey thousands of years old!",
    "Octopuses have three hearts 🐙",
    "Bananas are berries, but strawberries aren’t 🍓"
]

fallback = [
    "Hmm, interesting... tell me more!",
    "I’m not sure about that 🤔",
    "Could you explain it differently?",
    "Sorry, I didn’t get that fully."
]

def solve_math(expr):
    try:
        return eval(expr)
    except:
        return None

def chatbot_reply(user_input):
    user_input = user_input.lower()

    if "bye" in user_input:
        return "Goodbye 👋 Have a great day!"

    elif "hello" in user_input or "hi" in user_input:
        if memory["name"]:
            return f"Hey {memory['name']}! How are you today?"
        else:
            return "Hello! What’s your name?"

    elif "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip().title()
        memory["name"] = name
        return f"Nice to meet you, {name}! I’ll remember your name 😊"

    elif "what is my name" in user_input:
        if memory["name"]:
            return f"Your name is {memory['name']}!"
        else:
            return "I don’t know your name yet. Tell me by saying 'My name is ...'"

    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}"

    elif "date" in user_input:
        today = datetime.date.today()
        return f"Today’s date is {today}"

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "fact" in user_input:
        return random.choice(facts)

    elif any(op in user_input for op in ["+", "-", "*", "/", "%"]):
        result = solve_math(user_input)
        if result is not None:
            return f"The answer is {result}"
        else:
            return "Hmm, I couldn’t calculate that."

    else:
        return random.choice(fallback)


# 🪄 GUI Setup
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {user_input}\n", "user")
    entry.delete(0, tk.END)

    bot_response = chatbot_reply(user_input)
    chat_box.insert(tk.END, f"Bot: {bot_response}\n\n", "bot")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)


root = tk.Tk()
root.title("PyBot - Your Mini AI Assistant")
root.geometry("500x550")
root.resizable(False, False)
root.config(bg="#f4f4f4")

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, bg="#ffffff", font=("Segoe UI", 10))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_box.tag_config("user", foreground="#2b2b2b")
chat_box.tag_config("bot", foreground="#1c6dd0")

frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(pady=10)

entry = tk.Entry(frame, width=40, font=("Segoe UI", 10))
entry.grid(row=0, column=0, padx=5)

send_btn = tk.Button(frame, text="Send", command=send_message, bg="#1c6dd0", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", padx=10, pady=5)
send_btn.grid(row=0, column=1)

root.mainloop()
