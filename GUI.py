import tkinter as tk
from tkinter import ttk


from tkinter import *
def GUI():
    root=tk.Tk()
    root.geometry("500x500")
    root.title 
    label1=Label(root,text="Please Enter Your Login Details")
    label2=Label(root,text="Username")
    label3=Label(root,text="Password")
    label4=Label(root,text="Dont Have A Account? Click Here!")
    nameEntry = tk.Entry(root,font=('calibre',10,'normal'))
    passEntry = tk.Entry(root,font=('calibre',10,'normal'))

    label1.grid(column=3,row=0)
    label2.grid(column=2,row=1)
    label3.grid(column=2,row=2)
    nameEntry.grid(column=3,row=1)
    passEntry.grid(column=3,row=2)
    root.mainloop()