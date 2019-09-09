from tkinter import *
import tkinter.messagebox
import backend
root=Tk()
root.title('Library system')

title_txt=StringVar()
author_txt=StringVar()
year_txt=StringVar()
isbn_txt=StringVar()
l=Label(root,text='Title',fg='red',relief=RAISED)
l.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')
l=Label(root,text='Year',fg='red',relief=RAISED)
l.grid(row=1,column=0,padx=5,pady=5,sticky='nswe')
e1=Entry(root,textvariable=title_txt)
e1.grid(row=0,column=1,padx=5,pady=5,sticky='nswe')
e2=Entry(root,textvariable=year_txt)
e2.grid(row=1,column=1,padx=5,pady=5,sticky='nswe')

l=Label(root,text='Author',fg='red',relief=RAISED)
l.grid(row=0,column=2,padx=5,pady=5,sticky='nswe')
l=Label(root,text='ISBN',fg='red',relief=RAISED)
l.grid(row=1,column=2,padx=5,pady=5,sticky='nswe')
e3=Entry(root,textvariable=author_txt)
e3.grid(row=0,column=3,padx=5,pady=5,sticky='nswe')
e4=Entry(root,textvariable=isbn_txt)
e4.grid(row=1,column=3,padx=5,pady=5,sticky='nswe')


root.mainloop()
