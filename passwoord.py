import tkinter as tk
import random
import string


# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())
    complexity = complexity_var.get()

    if complexity == "Low":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace

    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=f"Generated Password: {password}")


# Create the main window
root = tk.Tk()
root.title("Password Generator App")
root.geometry("400x200")

frame = tk.Frame(root)
frame.pack(pady=20)

length_label = tk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=10)

length_entry = tk.Entry(frame, width=5)
length_entry.grid(row=0, column=1)

complexity_label = tk.Label(frame, text="Complexity:")
complexity_label.grid(row=1, column=0, padx=10)

complexity_var = tk.StringVar()
complexity_var.set("Low")
complexity_menu = tk.OptionMenu(frame, complexity_var, "Low", "Medium", "High")
complexity_menu.grid(row=1, column=1)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

password_label = tk.Label(root, text="Generated Password: ")
password_label.pack()

root.mainloop()
