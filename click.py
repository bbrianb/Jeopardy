import tkinter as tk

root = tk.Tk()


def left_click(event):
    print("left")


frame = tk.Frame(root, width=300, height=250)

frame.bind("<Button-1>", left_click)

frame.pack()

root.mainloop()
