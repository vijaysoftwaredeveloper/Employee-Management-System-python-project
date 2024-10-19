from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
db=Database("Employees.db")
root=Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()



#Entry Frame

entries_frame=Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee Management System",font=("Arial",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)


lblName=Label(entries_frame,text="NAME",font=("Arial",16),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="W")
txtName=Entry(entries_frame,textvariable=name,font=("Arial",14),width=30)
txtName.grid(row=1,column=1)

lblAge=Label(entries_frame,text="AGE",font=("Arial",16),bg="#535c68",fg="white")
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky="W")
txtAge=Entry(entries_frame,textvariable=age,font=("Arial",14),width=30)
txtAge.grid(row=1,column=3)


lbldoj=Label(entries_frame,text="D.O.J",font=("Arial",16),bg="#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=10,pady=10,sticky="W")
txtdoj=Entry(entries_frame,textvariable=doj,font=("Arial",14),width=30)
txtdoj.grid(row=2,column=1)




lblemail=Label(entries_frame,text="EMAIL",font=("Arial",16),bg="#535c68",fg="white")
lblemail.grid(row=2,column=2,padx=10,pady=10,sticky="W")
txtemail=Entry(entries_frame,textvariable=email,font=("Arial",14),width=30)
txtemail.grid(row=2,column=3)

lblgender=Label(entries_frame,text="GENDER",font=("Arial",16),bg="#535c68",fg="white")
lblgender.grid(row=3,column=0,padx=10,pady=10,sticky="W")
combogender=ttk.Combobox(entries_frame,font=("Arial",16),width=26,textvariable=gender,state="readonly")
combogender["values"]=("MALE","FEMALE")
combogender.grid(row=3,column=1,padx=10,sticky="W")

lblcontact=Label(entries_frame,text="CONTACT",font=("Arial",16),bg="#535c68",fg="white")
lblcontact.grid(row=3,column=2,padx=10,pady=10,sticky="W")
txtcontact=Entry(entries_frame,textvariable=contact,font=("Arial",14),width=30)
txtcontact.grid(row=3,column=3)

lbladdress=Label(entries_frame,text="ADDRESS",font=("Arial",16),bg="#535c68",fg="white")
lbladdress.grid(row=4,column=0,padx=10,pady=10,sticky="W")

txtaddress=Text(entries_frame,width=85,height=5,font=("Arial",16))
txtaddress.grid(row=5,column=0,columnspan=4,padx=10,pady=10,sticky="w")

def getData(event):
    select_row=tv.focus()
    data=tv.item(select_row)
    global row
    row=data["values"]
    # print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0, END)
    txtaddress.insert(END,row[7])


def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)



def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtdoj.get() == "" or txtemail.get() == "" or combogender.get() == "" or txtcontact.get() == "" or txtaddress.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input ", "Please Fill all the Details")
        return
    db.insert(txtName.get(), txtAge.get(), txtdoj.get(), txtemail.get(), combogender.get(), txtcontact.get(),
              txtaddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearall()
    displayall()

def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtdoj.get() == "" or txtemail.get() == "" or combogender.get() == "" or txtcontact.get() == "" or txtaddress.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input ", "Please Fill all the Details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtdoj.get(), txtemail.get(), combogender.get(), txtcontact.get(),
              txtaddress.get(1.0, END))
    messagebox.showinfo("Success", "Record update")
    clearall()
    displayall()

def delete_employee():
    db.remove(row[0])
    clearall()
    displayall()
def clearall():
    name .set("")
    age.set("")
    doj .set("")
    gender .set("")
    email .set("")
    contact.set("")
    txtaddress.delete(1.0,END)


btn_frame=Frame(entries_frame,bg="#535c68")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")

lbladd=Button(btn_frame,command=add_employee,text="Add Details",width=15,font=("Arial",16,"bold"),bg="green",fg="white",bd=0)
lbladd.grid(row=7,column=0,padx=10,pady=10)

lbledit=Button(btn_frame,command=update_employee,text="Update Details",width=15,font=("Arial",16,"bold"),bg="blue",fg="white",bd=0)
lbledit.grid(row=7,column=1,padx=10,pady=10)

lbldelete=Button(btn_frame,command=delete_employee,text="Delete Details",width=15,font=("Arial",16,"bold"),bg="red",fg="white",bd=0)
lbldelete.grid(row=7,column=2,padx=10,pady=10)

lblclear=Button(btn_frame,command=clearall,text="Clear Details",width=15,font=("Arial",16,"bold"),bg="yellow",fg="white",bd=0)
lblclear.grid(row=7,column=3,padx=10,pady=10)

#Table Frame

tree_frame=Frame(root,bg="#ecf0f1")
tree_frame.place(x=0,y=500,width=1500,height=500)
style=ttk.Style()
style.configure("mystyle.Treeview",font=("Arial",16),rowheigh=50), #Modify the font of the body
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8))
tv.heading("1", text="ID")
tv.column("1",width=5)
tv.heading("2", text="NAME")
tv.column("2",width=15)

tv.heading("3", text="AGE")
tv.column("3",width=5)
tv.heading("4", text="D.O.J")
tv.column("4",width=10)
tv.heading("5", text="EMAIL")
tv.heading("6", text="GENDER")
tv.column("6",width=5)
tv.heading("7", text="CONTACT")
tv.column("7",width=12)
tv.heading("8", text="ADDRESS")
tv["show"]='headings'
tv.bind("<ButtonRelease-1>",getData)
displayall()

tv.pack(fill=X)









root.mainloop()