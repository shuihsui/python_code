#!/usr/bin/env python


import tkinter

top = tkinter.Tk()
label = tkinter.Label(top,text='Hello,GUI')
label.pack()
quit = tkinter.Button(top,text='quit',command=top.quit,bg='red',fg='blue')
quit.pack(fill=tkinter.X,expand=1)
tkinter.mainloop()
