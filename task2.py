import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.master.configure(bg="#f0f0f0")

        self.entry_frame = tk.Frame(master, bg="#f0f0f0")
        self.entry_frame.pack(pady=10)

        self.num1_label = tk.Label(self.entry_frame, text="Enter first number:", bg="#f0f0f0")
        self.num1_label.grid(row=0, column=0, padx=5, pady=5)

        self.num1_entry = tk.Entry(self.entry_frame, font=('Helvetica', 12))
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        self.num2_label = tk.Label(self.entry_frame, text="Enter second number:", bg="#f0f0f0")
        self.num2_label.grid(row=1, column=0, padx=5, pady=5)

        self.num2_entry = tk.Entry(self.entry_frame, font=('Helvetica', 12))
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        self.operator_frame = tk.Frame(master, bg="#f0f0f0")
        self.operator_frame.pack(pady=10)

        self.add_button = tk.Button(self.operator_frame, text="+", command=lambda: self.set_operation("+"), bg="#4CAF50", fg="white", font=('Helvetica', 12, 'bold'))
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.subtract_button = tk.Button(self.operator_frame, text="-", command=lambda: self.set_operation("-"), bg="#4CAF50", fg="white", font=('Helvetica', 12, 'bold'))
        self.subtract_button.grid(row=0, column=1, padx=5, pady=5)

        self.multiply_button = tk.Button(self.operator_frame, text="*", command=lambda: self.set_operation("*"), bg="#4CAF50", fg="white", font=('Helvetica', 12, 'bold'))
        self.multiply_button.grid(row=0, column=2, padx=5, pady=5)

        self.divide_button = tk.Button(self.operator_frame, text="/", command=lambda: self.set_operation("/"), bg="#4CAF50", fg="white", font=('Helvetica', 12, 'bold'))
        self.divide_button.grid(row=0, column=3, padx=5, pady=5)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate, bg="#4CAF50", fg="white", font=('Helvetica', 14, 'bold'))
        self.calculate_button.pack(pady=10, ipadx=10, ipady=5)

        self.result_frame = tk.Frame(master, bg="#f0f0f0")
        self.result_frame.pack(pady=10)

        self.result_label = tk.Label(self.result_frame, text="Result:", bg="#f0f0f0")
        self.result_label.grid(row=0, column=0, padx=5, pady=5)

        self.result_value = tk.Label(self.result_frame, text="", bg="#f0f0f0", font=('Helvetica', 14, 'bold'))
        self.result_value.grid(row=0, column=1, padx=5, pady=5)

        self.operation = None

    def set_operation(self, operator):
        self.operation = operator

    def calculate(self):
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()

        try:
            num1 = float(num1)
            num2 = float(num2)

            if self.operation == "+":
                result = num1 + num2
            elif self.operation == "-":
                result = num1 - num2
            elif self.operation == "*":
                result = num1 * num2
            elif self.operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = num1 / num2
            else:
                raise ValueError("Please select an operation")

            self.result_value.config(text=str(result))

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = SimpleCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
