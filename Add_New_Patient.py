from tkinter import *
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox
import mysql.connector
con = mysql.connector.connect(user="root",password="",host="localhost",database="project")
cur = con.cursor()

class hospital:
    def __init__(self,Root):
        self.root = Root
        self.root.title("Patient Registration")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

        UserId=StringVar()
        User_Name=StringVar()
        Password=StringVar()
        Confirm=StringVar()
        Position=StringVar()

        Patient=StringVar()
        Submit=StringVar()
        Delete=StringVar()
        Reset=StringVar()
        Exit=StringVar()

        


        MainFrame =Frame(self.root)
        MainFrame.grid()

        TitleFrame =Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame,
                             font=('arial',40,'bold'),
                             text="Add New Patient",padx=2)
        self.lblTitle.grid()

        FrameDetail =Frame(MainFrame, bd=20, width=1350, height=180, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame =Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=20, width=1350, height=300, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE,
                                  font=('arial',12,'bold'), text="Add New Patient")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=450, height=400, padx=20, relief=RIDGE,
                                   font=('arial',12,'bold'), text="Patient Details")
        DataFrameRIGHT.pack(side=RIGHT)

        #===========================DataFrameLEFT=========================================


        self.lblUserId =Label(DataFrameLEFT, font=('arial',12,'bold'), text="User Id:",padx=2)
        self.lblUserId.grid(row=0, column=0,sticky=W)
        self.txtUserId=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= UserId)
        self.txtUserId.grid(row=0, column=1)

        self.lblUser_Name =Label(DataFrameLEFT, font=('arial',12,'bold'), text="User Name:",padx=2)
        self.lblUser_Name.grid(row=1, column=0,sticky=W)
        self.txtUser_Name=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=User_Name)
        self.txtUser_Name.grid(row=1, column=1)

        self.lblPassword =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Password:",padx=2)
        self.lblPassword.grid(row=2, column=0,sticky=W)
        self.txtPassword=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Password)
        self.txtPassword.grid(row=2,column=1)

        self.lblConfirm =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Confirm:",padx=2)
        self.lblConfirm.grid(row=3, column=0,sticky=W)
        self.txtConfirm=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Confirm)
        self.txtConfirm.grid(row=3,column=1)

        self.lblPosition =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Position:",padx=2)
        self.lblPosition.grid(row=4, column=0,sticky=W)
        self.txtPosition=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Position)
        self.txtPosition.grid(row=4,column=1)

        #===========================DataFrameRIGHT=========================================

        self.Patient =Text(DataFrameRIGHT, font=('arial',12,'bold'),width =43,height=14,padx=2,pady=4) 
        self.Patient.grid(row=0, column=0)

        #===========================Button Frame============================
        def Patient():
            self.Patient.insert(END,'UserId: \t\t' + self.txtUserId.get() + "\n")
            self.Patient.insert(END,'User Name: \t\t' + self.txtUser_Name.get() + "\n")
            self.Patient.insert(END,'Password: \t\t' + self.txtPassword.get() + "\n")
            self.Patient.insert(END,'Confirm: \t\t' + self.txtConfirm.get() + "\n")
            self.Patient.insert(END,'Position: \t\t' + self.txtPosition.get() + "\n")
            return

        self.btnPatient=Button(ButtonFrame,text='Patient Details',font=('arial',12,'bold'),width =24,bd=4,
                                    command=Patient)
        self.btnPatient.grid(row=0, column=0)
        
        def Submit():
            global con
            global cur
            sql = "insert into `add_new_patient`(`UserId`,`User_Name`,`Password`,`Confirm`,Position) values('{}','{}','{}','{}','{}')". format(UserId.get(),User_Name.get(),Password.get(),Confirm.get(),Position.get())
            print(sql)
            cur.execute(sql)
            con.commit()

        self.btnSubmit=Button(ButtonFrame,text='Submit Data',font=('arial',12,'bold'),width =24,bd=4,
                                    command=Submit)
        self.btnSubmit.grid(row=0, column=1)

        def Delete():
            UserId.set("")
            User_Name.set("")
            Password.set("")
            Confirm.set("")
            Position.set("")
            return

        self.btnDelete=Button(ButtonFrame,text='Delete',font=('arial',12,'bold'),width =24,bd=4,
                                    command=Delete)
        self.btnDelete.grid(row=0, column=2)

        def Reset():
            UserId.set("")
            User_Name.set("")
            Password.set("")
            Confirm.set("")
            Position.set("")
            self.Patient.delete("1.0",END)
            return

        self.btnReset=Button(ButtonFrame,text='Reset',font=('arial',12,'bold'),width =24,bd=4,
                                    command=Reset)
        self.btnReset.grid(row=0, column=3)

        def Exit():
            Exit=tkinter.messagebox.askyesno("Add New Patient","Confirm if you want to Exit")
            if Exit >0:
                root.destroy()

        self.btnExit=Button(ButtonFrame,text='Exit',font=('arial',12,'bold'),width =24,bd=4,
                                    command=Exit)
        self.btnExit.grid(row=0, column=4)

            #==================All Button=============================

        
#if __name__=='__main__':
root = Tk()
application = hospital(root)
root.mainloop()
