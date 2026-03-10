import tkinter as tk

# Function to show numbers on screen
def click(num):
    entry.insert(tk.END, num)

# Function to calculate result
def calculate():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Function to clear screen
def clear():
    entry.delete(0, tk.END)

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")

# Entry box
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Buttons
tk.Button(root, text="1", width=5, height=2, command=lambda: click(1)).grid(row=1,column=0)
tk.Button(root, text="2", width=5, height=2, command=lambda: click(2)).grid(row=1,column=1)
tk.Button(root, text="3", width=5, height=2, command=lambda: click(3)).grid(row=1,column=2)
tk.Button(root, text="+", width=5, height=2, command=lambda: click("+")).grid(row=1,column=3)

tk.Button(root, text="4", width=5, height=2, command=lambda: click(4)).grid(row=2,column=0)
tk.Button(root, text="5", width=5, height=2, command=lambda: click(5)).grid(row=2,column=1)
tk.Button(root, text="6", width=5, height=2, command=lambda: click(6)).grid(row=2,column=2)
tk.Button(root, text="-", width=5, height=2, command=lambda: click("-")).grid(row=2,column=3)

tk.Button(root, text="7", width=5, height=2, command=lambda: click(7)).grid(row=3,column=0)
tk.Button(root, text="8", width=5, height=2, command=lambda: click(8)).grid(row=3,column=1)
tk.Button(root, text="9", width=5, height=2, command=lambda: click(9)).grid(row=3,column=2)
tk.Button(root, text="*", width=5, height=2, command=lambda: click("*")).grid(row=3,column=3)

tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=4,column=0)
tk.Button(root, text="0", width=5, height=2, command=lambda: click(0)).grid(row=4,column=1)
tk.Button(root, text="=", width=5, height=2, command=calculate).grid(row=4,column=2)
tk.Button(root, text="/", width=5, height=2, command=lambda: click("/")).grid(row=4,column=3)

root.mainloop()