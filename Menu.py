from tkinter import *
from tkinter import ttk
import tkinter.messagebox
tk=Tk()
tk.geometry("1350x750+0+0")

tk.config(bg="white")
tk.title('Hospital Management')
scrollbar = Scrollbar()
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(tk, yscrollcommand = scrollbar.set )

lbl=Label(tk,text="Hospital Management \n System",font=("Courier", 30, "bold"),height=2,bg="green",width=71,fg = "white")
lbl.pack()

frame1=Frame(tk)
def Login():
    global tk
    import Login
btnLogin_1=Button(frame1,text='Login',font=('arial',12,'bold'),width =27,bd=4,command=Login)
btnLogin_1.grid(row=0, column=0)

def Add_New_Patient():
    global tk
    import Add_New_Patient

btnAdd_New_Patient=Button(frame1,text='Add_New_Patient',font=('arial',12,'bold'),width =20,bd=4,command=Add_New_Patient)
btnAdd_New_Patient.grid(row=0, column=1)

def Add_New_ward():
    import Add_New_ward

btnAdd_New_ward=Button(frame1,text='Add_New_ward',font=('arial',12,'bold'),width =20,bd=4,command=Add_New_ward)
btnAdd_New_ward.grid(row=0, column=2)

def Patient_CkeckOut():
    import Patient_CkeckOut

btnPatient_CkeckOut=Button(frame1,text='Patient_CkeckOut',font=('arial',12,'bold'),width =20,bd=4,command=Patient_CkeckOut)
btnPatient_CkeckOut.grid(row=0, column=3)

def Patient_Registation():
    import Patient_Registation

btnPatient_Registation=Button(frame1,text='Patient_Registation',font=('arial',12,'bold'),width =20,bd=4,
                            command=Patient_Registation)
btnPatient_Registation.grid(row=0, column=4)

def Staff_Information():
    import Staff_Information

btnStaff_Information=Button(frame1,text='Staff_Information',font=('arial',12,'bold'),width =20,bd=4,
                            command=Staff_Information)
btnStaff_Information.grid(row=0, column=5)
frame1.pack()

canvas=Canvas(tk,width=1400,height=600)
canvas.pack()
image1 = PhotoImage(file="r096x9_large.png")
canvas.create_image(0,0,anchor=NW,image=image1)

#scrollbar.config( command = mylist.yview )

#root = Tk()
#application = Hospital(root)

tk.mainloop()

