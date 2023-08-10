import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.num1_label = tk.Label(root, text="Enter first number:")
        self.num1_label.pack()

        self.num1_entry = tk.Entry(root)
        self.num1_entry.pack()

        self.num2_label = tk.Label(root, text="Enter second number:")
        self.num2_label.pack()

        self.num2_entry = tk.Entry(root)
        self.num2_entry.pack()

        self.operation_label = tk.Label(root, text="Select operation:")
        self.operation_label.pack()

        self.operation_var = tk.StringVar(root)
        self.operation_var.set("+")  # Default operation is addition

        self.operation_menu = tk.OptionMenu(root, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.pack()

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
