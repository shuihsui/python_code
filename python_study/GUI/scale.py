#!/usr/bin/env python

from tkinter import *

def resize(ev=None):
	label.config(font='Helvatica -%d bold' % scale.get())

top = Tk()
top.geometry('250x150')

label = Label(top,text='Hello,GUI',font='Helvatica -12 bold')
label.pack(fill=Y,expand=1)

scale = Scale(top,from_=10,to=40,orient=HORIZONTAL,command=resize)
scale.set(12)
scale.pack(fill=Y,expand=1)

button = Button(top,text='quit',command=top.quit,activeforeground='white',activebackground='red')
button.pack()

mainloop()
