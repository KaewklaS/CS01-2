from tkinter import *
root = Tk()
root.title("First GUI")
myText = Label(text="My name is ",fg="blue",font=20).grid(row=0,column=0)
myText = Label(text="Kaewkla ",fg="green",font=20).grid(row=1,column=1)
myText = Label(text="Sroykabkaew ",fg="red",font=20).grid(row=2,column=2)
root.mainloop()