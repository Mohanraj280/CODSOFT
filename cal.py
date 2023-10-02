import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        # Entry for displaying input and result
        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 18), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Clear button
        self.clear_button = tk.Button(root, text="Clear", padx=20, pady=20, font=("Arial", 16), command=self.clear_entry)
        self.clear_button.grid(row=0, column=4)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button_text in button_texts:
            if button_text == "=":
                tk.Button(self.root, text=button_text, padx=20, pady=20, font=("Arial", 16),
                          command=self.evaluate_expression).grid(row=row_val, column=col_val)
            else:
                tk.Button(self.root, text=button_text, padx=20, pady=20, font=("Arial", 16),
                          command=lambda text=button_text: self.on_button_click(text)).grid(row=row_val, column=col_val)
            col_val += 1

            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button_text):
        current_text = self.result_var.get()
        new_text = current_text + button_text
        self.result_var.set(new_text)

    def evaluate_expression(self):
        try:
            expression = self.result_var.get()
            result = str(eval(expression))
            self.result_var.set(result)
        except Exception:
            self.result_var.set("Error")

    def clear_entry(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
