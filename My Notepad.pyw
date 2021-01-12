from tkinter import *
from tkinter.ttk import Button
import tkinter.scrolledtext as scrolledtext

top=Tk()
top.title('My Notepad')
top.geometry('720x650')

def switch_mode():
    st=btxt.get()
    if st=='OFF':
        btxt.set('ON')
        top.attributes('-topmost',False)

    elif st=='ON':
        btxt.set('OFF')
        top.attributes('-topmost',True)
        

l=Label(top,text='Set on Top')
l.place(x=20,y=3)

btxt=StringVar()
b=Button(top,textvariable=btxt,command=switch_mode)
btxt.set('OFF')
b.place(x=100,y=1)

txt = scrolledtext.ScrolledText(top,height=30,width=69, undo=True)
txt['font'] = ('Courier New',13,'bold')
txt.place(x=1,y=30)

top.attributes('-topmost',True)
top.mainloop()
