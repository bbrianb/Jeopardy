import tkinter as tk

root = tk.Tk()
root.geometry("500x300")


def add():
    tk.Entry(frame).grid()


frame = tk.Frame(root, height=100, width=150, bg="black")
frame.grid(row=1, column=0)
frame.grid_propagate(False)

tk.Button(root, text="add widget", command=add).grid(row=0, column=0)

root.mainloop()
