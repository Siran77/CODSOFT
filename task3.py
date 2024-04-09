import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string

def generate_password(length=12, include_text=True, include_numbers=True, include_special=True):
    characters = ''
    if include_text:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one type of characters (text, numbers, special) must be included.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        password = generate_password(length, include_text_var.get(), include_numbers_var.get(), include_special_var.get())
        generated_password_label.config(text="Generated Password: " + password)
    except ValueError as ve:
        messagebox.showerror("Error", ve)

root = tk.Tk()
root.title("Password Generator")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

length_label = ttk.Label(main_frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky=tk.W)

length_entry = ttk.Entry(main_frame)
length_entry.grid(row=0, column=1, sticky=tk.W)

include_text_var = tk.BooleanVar()
include_numbers_var = tk.BooleanVar()
include_special_var = tk.BooleanVar()

include_text_var.set(True)
include_numbers_var.set(True)
include_special_var.set(True)

include_text_checkbox = ttk.Checkbutton(main_frame, text="Include Text", variable=include_text_var)
include_text_checkbox.grid(row=1, column=0, sticky=tk.W)

include_numbers_checkbox = ttk.Checkbutton(main_frame, text="Include Numbers", variable=include_numbers_var)
include_numbers_checkbox.grid(row=2, column=0, sticky=tk.W)

include_special_checkbox = ttk.Checkbutton(main_frame, text="Include Special Characters", variable=include_special_var)
include_special_checkbox.grid(row=3, column=0, sticky=tk.W)

generate_button = ttk.Button(main_frame, text="Generate Password", command=generate)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

generated_password_label = ttk.Label(main_frame, text="")
generated_password_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
