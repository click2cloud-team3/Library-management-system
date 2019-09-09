from tkinter import *
import tkinter.messagebox
import backend
root=Tk()
root.title('Library system')

def clear():
  e1.delete(0,END)
  e2.delete(0,END)
  e3.delete(0,END)
  e4.delete(0,END)

def add_entry():
  backend.insert(title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get())
  listing.delete(0,END)
  listing.insert(END,(title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get()))
  clear()

def view_all():
  listing.delete(0,END)
  for row in backend.view():
    listing.insert(END,row)
  clear()

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

b1=Button(root,text='View All',command=view_all)
b1.grid(row=2,column=3,padx=5,pady=5,sticky='nswe')
b2=Button(root,text='Search Entry',command=search)
b2.grid(row=3,column=3,padx=5,pady=5,sticky='nswe')
b3=Button(root,text='Add Entry',command=add_entry)
b3.grid(row=4,column=3,padx=5,pady=5,sticky='nswe')
b4=Button(root,text='Update Selected',command=update)
b4.grid(row=5,column=3,padx=5,pady=5,sticky='nswe')
b5=Button(root,text='Delete Selected',command=delete)
b5.grid(row=6,column=3,padx=5,pady=5,sticky='nswe')
b6=Button(root,text='Close',command=root.destroy)
b6.grid(row=7,column=3,padx=5,pady=5,sticky='nswe')

listing=Listbox(root)
listing.grid(row=2,column=0,rowspan=6,columnspan=3,padx=5,pady=5,sticky='nswe')
listing.bind('<<ListboxSelect>>',get_selected_row)

for i in range(4):
  root.grid_columnconfigure(i,weight=1)
for i in range(8):
  root.grid_rowconfigure(i,weight=1) 

root.mainloop()
