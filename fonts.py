from tkinter import *
from tkinter import font

root = Tk()
root.title('Font Families')
fonts = list(font.families())
fonts.sort()


# noinspection PyUnresolvedReferences,PyShadowingNames,PyUnboundLocalVariable
def populate(f):
    """Put in the fonts"""
    list_number = 1
    for i, item in enumerate(fonts):
        label = Label(f, text=item, font=(item, 16))
        label.grid(row=i)
        label.bind("<Button-1>", lambda e, item=item: copy_to_clipboard(item))
        list_number += 1


def copy_to_clipboard(item):
    root.clipboard_clear()
    root.clipboard_append("font=('" + item.lstrip('@') + "', 12)")


def on_frame_configure(c):
    """Reset the scroll region to encompass the inner frame"""
    c.configure(scrollregion=c.bbox("all"))


canvas = Canvas(root, borderwidth=0, background="#ffffff")
frame = Frame(canvas, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4, 4), window=frame, anchor="nw")

# noinspection PyShadowingNames,PyUnresolvedReferences,PyUnboundLocalVariable
frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))

populate(frame)

root.mainloop()
