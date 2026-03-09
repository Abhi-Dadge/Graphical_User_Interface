from tkinter import *

# function
def add():
    a = int(box1.get())
    b = int(box2.get())
    result = a + b
    result_label.config(text="Result: " + str(result))

# window
root = Tk()
root.title("Calculator")
root.geometry("300x200")

# labels
Label(root, text="Enter Number 1").pack()
box1 = Entry(root)
box1.pack()

Label(root, text="Enter Number 2").pack()
box2 = Entry(root)
box2.pack()

# button
Button(root, text="Add", command=add).pack()

# result label
result_label = Label(root, text="Result:")
result_label.pack()

root.mainloop()