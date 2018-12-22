from tkinter import *
import backend as bn

def getselectedrow(event):
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple=lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
def view_comm():
    lb.delete(0,END)
    for r in bn.view():
        lb.insert(END,r)
def v_search():
    lb.delete(0,END)
    for r in bn.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        lb.insert(END,r)
def insert_f():
    bn.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    lb.delete(0,END)
    lb.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
def delete_f():
    bn.delete(selected_tuple[0])
def update_f():
    bn.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())



window=Tk()
window.wm_title("BookStore")


l1=Label(window,text="Title")
l1.grid(row=0,column=0)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

l2=Label(window,text="Author")
l2.grid(row=0,column=3)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=4)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=4)

view_all=Button(window,text="View",width=12,command=view_comm)
search=Button(window,text="Search",width=12,command=v_search)
add=Button(window,text="Add",width=12,command=insert_f)
update=Button(window,text="Update",width=12,command=update_f)
delete=Button(window,text="Delete",width=12,command=delete_f)
close=Button(window,text="Close",width=12,command=window.destroy)
view_all.grid(row=2,column=4)
search.grid(row=3,column=4)
add.grid(row=4,column=4)
update.grid(row=5,column=4)
delete.grid(row=6,column=4)
close.grid(row=7,column=4)

lb=Listbox(window,height=6,width=35)
lb.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

lb.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',getselectedrow)

window.mainloop()
