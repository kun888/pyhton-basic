import tkinter
from tkinter import Tk, Button
win1=Tk()
win2=Tk()
Button(win1,text='button1',command=win1.destroy).place()
Button(win2,text='button2').place()
win1.mainloop()
