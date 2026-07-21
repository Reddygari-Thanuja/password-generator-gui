import tkinter as tk
import random
import string

def generate_password():
    password_list = (
        random.sample(string.ascii_uppercase, 1) +
        random.sample(string.ascii_lowercase, 4) +
        random.sample(string.digits, 2) +
        random.sample("$@!_", 1)
    )
    random.shuffle(password_list)
    password = "".join(password_list)
    result.config(text=password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x180")

tk.Label(root, text="Password Generator", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Generate Password", command=generate_password).pack()

result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=20)

root.mainloop()