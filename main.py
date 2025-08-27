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
