# Version: 1.0
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
# Version: 1.1
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
'''
# Version: 1.2
'''
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify

# Define symbol
x = symbols('x')

# App theme
ctk.set_appearance_mode("dark")   # "dark" or "light"
ctk.set_default_color_theme("blue")  # themes: "blue", "green", "dark-blue"

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
        plt.plot(X, Y, label=f"y = {expr}", color="cyan", linewidth=2)
        plt.title(f"Graph of y = {expr}", fontsize=14, fontweight="bold")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Invalid Equation!\n{e}")


# ------------------ UI ------------------
root = ctk.CTk()
root.title("GraphyGen 📊")
root.geometry("500x300")

title_label = ctk.CTkLabel(root, text="GraphyGen 📊", font=("Arial", 22, "bold"))
title_label.pack(pady=10)

entry_eq = ctk.CTkEntry(root, width=320, height=35, placeholder_text="Enter equation (e.g. y = sin(x))")
entry_eq.pack(pady=10)

frame_range = ctk.CTkFrame(root)
frame_range.pack(pady=10)

entry_min = ctk.CTkEntry(frame_range, width=80, placeholder_text="X min")
entry_min.grid(row=0, column=0, padx=10)
entry_min.insert(0, "-10")

entry_max = ctk.CTkEntry(frame_range, width=80, placeholder_text="X max")
entry_max.grid(row=0, column=1, padx=10)
entry_max.insert(0, "10")

plot_btn = ctk.CTkButton(root, text="📈 Plot Graph", command=plot_equation, width=150, height=40, corner_radius=15)
plot_btn.pack(pady=20)

root.mainloop()
'''
# Version: 1.3
'''
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify

# Define symbol
x = symbols('x')

ctk.set_appearance_mode("dark")   # "light" or "dark"
ctk.set_default_color_theme("blue")

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
        plt.plot(X, Y, label=f"y = {expr}", color="cyan", linewidth=2)
        plt.title(f"Graph of y = {expr}", fontsize=14, fontweight="bold")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Invalid Equation!\n{e}")


# ------------------ UI ------------------
root = ctk.CTk()
root.title("GraphyGen 📊")
root.geometry("520x320")

# Title
title_label = ctk.CTkLabel(root, text="GraphyGen 📊", font=("Arial", 22, "bold"))
title_label.pack(pady=10)

# Equation entry
entry_eq = ctk.CTkEntry(root, width=350, height=40, placeholder_text="Enter equation (e.g. y = sin(x))")
entry_eq.pack(pady=10)

# Frame for range
frame_range = ctk.CTkFrame(root)
frame_range.pack(pady=10)

# Dropdown options
preset_ranges = ["-10,10", "-90,90", "0,100"]

entry_min = ctk.CTkComboBox(frame_range, values=["-10", "-90", "0"], width=100)
entry_min.grid(row=0, column=0, padx=10)
entry_min.set("-10")

entry_max = ctk.CTkComboBox(frame_range, values=["10", "90", "100"], width=100)
entry_max.grid(row=0, column=1, padx=10)
entry_max.set("10")

# Plot button
plot_btn = ctk.CTkButton(root, text="📈 Plot Graph", command=plot_equation, width=170, height=45, corner_radius=15)
plot_btn.pack(pady=20)

root.mainloop()
'''
# Version: 1.4
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, lambdify

# Define symbol
x = symbols('x')

ctk.set_appearance_mode("dark")   # "light" or "dark"
ctk.set_default_color_theme("blue")

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

        # Get style and color
        style_choice = style_box.get()
        color_choice = color_box.get()

        # Map style to matplotlib syntax
        styles = {
            "Line": "-",
            "Dashed": "--",
            "Dotted": ":",
            "Scatter": "o"
        }
        line_style = styles.get(style_choice, "-")

        # Plot
        plt.figure(figsize=(6,4))
        plt.plot(X, Y, line_style, label=f"y = {expr}", color=color_choice.lower(), linewidth=2)
        plt.title(f"Graph of y = {expr}", fontsize=14, fontweight="bold")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"Invalid Equation!\n{e}")


# ------------------ UI ------------------
root = ctk.CTk()
root.title("GraphyGen 📊")
root.geometry("550x380")

# Title
title_label = ctk.CTkLabel(root, text="GraphyGen 📊", font=("Arial", 22, "bold"))
title_label.pack(pady=10)

# Equation entry
entry_eq = ctk.CTkEntry(root, width=350, height=40, placeholder_text="Enter equation (e.g. y = sin(x))")
entry_eq.pack(pady=10)

# Frame for range
frame_range = ctk.CTkFrame(root)
frame_range.pack(pady=10)

entry_min = ctk.CTkComboBox(frame_range, values=["-10", "-90", "0"], width=100)
entry_min.grid(row=0, column=0, padx=10)
entry_min.set("-10")

entry_max = ctk.CTkComboBox(frame_range, values=["10", "90", "100"], width=100)
entry_max.grid(row=0, column=1, padx=10)
entry_max.set("10")

# Style + Color options
frame_options = ctk.CTkFrame(root)
frame_options.pack(pady=10)

style_box = ctk.CTkComboBox(frame_options, values=["Line", "Dashed", "Dotted", "Scatter"], width=120)
style_box.grid(row=0, column=0, padx=10)
style_box.set("Line")

color_box = ctk.CTkComboBox(frame_options, values=["Blue", "Red", "Green", "Cyan", "Magenta", "Yellow", "Black"], width=120)
color_box.grid(row=0, column=1, padx=10)
color_box.set("Blue")

# Plot button
plot_btn = ctk.CTkButton(root, text="📈 Plot Graph", command=plot_equation, width=170, height=45, corner_radius=15)
plot_btn.pack(pady=20)

root.mainloop()
