import tkinter
from tkinter import *

window = tkinter.Tk()
window.title('Prima noastra aplicatie!')
label = tkinter.Label(window, text="Text").pack()
button = tkinter.Button(window, text="Click").pack()

checkbox_1 = IntVar()
checkbox_2 = IntVar()
tkinter.Checkbutton(window, text="Text1", variable=checkbox_1, onvalue=1, offvalue=0).grid(row=0, sticky=W)
tkinter.Checkbutton(window, text="Text2", variable=checkbox_1, onvalue=0, offvalue=1).grid(row=1, sticky=W)
window.mainloop()