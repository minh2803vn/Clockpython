from tkinter import *
from time import *


def new():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B,%d,%Y")
    date_label.config(text=date_string)

    time_label.after(1000, new)


window = Tk()
time_label = Label(window, font="Arial, 35", fg="#0366fc", bg="#fafbfc")
time_label.pack()
day_label = Label(window, font="Arial, 35")
day_label.pack()
day_label = Label(window, font="Arial, 35")
day_label.pack()
date_label = Label(window, font="Arial, 35")
date_label.pack()
new()
window.mainloop()
