'''
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify

# Define symbol
x = symbols('x')

def plot_equation():
    eq_text = entry.get()
    try:
        # Parse equation
        expr = sympify(eq_text.replace("^", "**"))
        func = lambdify(x, expr, "numpy")
        
        # Generate x values
        X = np.linspace(-10, 10, 500)
        Y = func(X)
        
        # Plot
        plt.figure(figsize=(6,4))
        plt.plot(X, Y, label=f"y = {expr}", color="blue")
        plt.title("Equation Graph Generator")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Equation!\n{e}")

# UI setup
root = tk.Tk()
root.title("Graph Generator")
root.geometry("400x200")

tk.Label(root, text="Enter equation in terms of x:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Plot Graph", command=plot_equation, bg="blue", fg="white", font=("Arial", 12)).pack(pady=20)

root.mainloop()
'''
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify

# Define symbol
x = symbols('x')

def plot_equation():
    eq_text = entry_eq.get().strip()
    
    # Remove "y=" if present
    if "=" in eq_text:
        eq_text = eq_text.split("=")[-1].strip()

    try:
        # Parse equation
        expr = sympify(eq_text.replace("^", "**"))
        func = lambdify(x, expr, "numpy")

        # Get range values
        try:
            x_min = float(entry_min.get())
            x_max = float(entry_max.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for X range!")
            return

        if x_min >= x_max:
            messagebox.showerror("Error", "X min should be less than X max!")
            return

        # Generate x values
        X = np.linspace(x_min, x_max, 500)
        Y = func(X)

        # Plot
        plt.figure(figsize=(6,4))
        plt.plot(X, Y, label=f"y = {expr}", color="blue")
        plt.title(f"Graph of y = {expr}")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Invalid Equation!\n{e}")

# ------------------ UI ------------------
root = tk.Tk()
root.title("GraphyGen 📊")
root.geometry("450x250")

tk.Label(root, text="Enter Equation in terms of x:", font=("Arial", 12)).pack(pady=5)
entry_eq = tk.Entry(root, width=30, font=("Arial", 12))
entry_eq.pack(pady=5)

frame_range = tk.Frame(root)
frame_range.pack(pady=5)

tk.Label(frame_range, text="X min:", font=("Arial", 10)).grid(row=0, column=0, padx=5)
entry_min = tk.Entry(frame_range, width=7)
entry_min.grid(row=0, column=1, padx=5)
entry_min.insert(0, "-10")

tk.Label(frame_range, text="X max:", font=("Arial", 10)).grid(row=0, column=2, padx=5)
entry_max = tk.Entry(frame_range, width=7)
entry_max.grid(row=0, column=3, padx=5)
entry_max.insert(0, "10")

tk.Button(root, text="Plot Graph", command=plot_equation, bg="blue", fg="white", font=("Arial", 12)).pack(pady=15)

root.mainloop()
