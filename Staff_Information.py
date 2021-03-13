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
        self.root.title("Staff Information")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

        ID=StringVar()
        Name=StringVar()
        Sex=StringVar()
        Age=StringVar()
        Address=StringVar()
        PhoneNo=StringVar()
        Position=StringVar()

        
        #==================All Button=============================
        Prescription=StringVar()
        Submit=StringVar()
        Delete=StringVar()
        Reset=StringVar()
        Exit=StringVar()

        def Prescription():
            self.Prescription.insert(END,'ID: \t\t' + ID.get() + "\n")
            self.Prescription.insert(END,'Name: \t\t' + Name.get() + "\n")
            self.Prescription.insert(END,'Sex: \t\t' + Sex.get() + "\n")
            self.Prescription.insert(END,'Address: \t\t' + Address.get() + "\n")
            self.Prescription.insert(END,'Phone No: \t\t' + PhoneNo.get() + "\n")
            self.Prescription.insert(END,'Position: \t\t' + Position.get() + "\n")
            return


        
        def Submit():
            global con
            global cur
            sql = "insert into `staff_information`(`ID`,`Name`,`Sex`,`Age`,`Address`,`PhoneNo`,`Position`) values('{}','{}','{}','{}','{}','{}','{}')". format(ID.get(),Name.get(),Sex.get(),Age.get(),Address.get(),PhoneNo.get(),Position.get())
            print(sql)
            cur.execute(sql)
            con.commit()

        def Delete():
            ID.set("")
            Name.set("")
            Sex.set("")
            Age.set("")
            Address.set("")
            PhoneNo.set("")
            Position.set("")
            return

        def Reset():
            ID.set("")
            Name.set("")
            Sex.set("")
            Age.set("")
            Address.set("")
            PhoneNo.set("")
            Position.set("")
            self.Prescription.delete("1.0",END)
            return
        
        def Exit():
            iExit=tkinter.messagebox.askyesno("Add New Ward","Confirm if you want to Exit")
            if iExit >0:
                root.destroy()


        MainFrame =Frame(self.root)
        MainFrame.grid()

        TitleFrame =Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame,
                             font=('arial',40,'bold'),
                             text="Staff Information",padx=2)
        self.lblTitle.grid()

        FrameDetail =Frame(MainFrame, bd=20, width=1350, height=180, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame =Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=20, width=1350, height=300, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE,
                                  font=('arial',12,'bold'), text="Staff Information")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=450, height=400, padx=20, relief=RIDGE,
                                   font=('arial',12,'bold'), text="Staff Details")
        DataFrameRIGHT.pack(side=RIGHT)

        

#===========================DataFrameLEFT=========================================

        self.lblID =Label(DataFrameLEFT, font=('arial',12,'bold'), text="ID:",padx=2)
        self.lblID.grid(row=0, column=0,sticky=W)
        self.txtID=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=ID)
        self.txtID.grid(row=0, column=1)

        self.lblName =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Name of Patient:",padx=2)
        self.lblName.grid(row=1, column=0,sticky=W)
        self.txtName=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Name)
        self.txtName.grid(row=1, column=1)
        
        self.lblSex =Label(DataFrameLEFT,
                                  font=('arial',12,'bold'),
                                  text="Sex:",padx=2)
        self.lblSex.grid(row=2, column=0,sticky=W)

        self.cboSex=ttk.Combobox(DataFrameLEFT,textvariable=Sex,
                                        state='readonly',font=('arial',11,'bold'), width=20)
        
        self.cboSex['value']=('','Male','Female')
        self.cboSex.current(0)
        self.cboSex.grid(row=2, column=1)
        
        
        
        self.lblAge =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Age of Patient:",padx=2)
        self.lblAge.grid(row=3, column=0,sticky=W)
        self.txtAge=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Age)
        self.txtAge.grid(row=3, column=1)

        self.lblAddress =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Address of Patient:",padx=2)
        self.lblAddress.grid(row=4, column=0,sticky=W)
        self.txtAddress=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Address)
        self.txtAddress.grid(row=4,column=1)

        self.lblPhoneNo =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Phone No:",padx=2)
        self.lblPhoneNo.grid(row=5, column=0,sticky=W)
        self.txtPhoneNo=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PhoneNo)
        self.txtPhoneNo.grid(row=5,column=1)

        self.lblPosition =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Position:",padx=2)
        self.lblPosition.grid(row=6, column=0,sticky=W)
        self.txtPosition=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Position)
        self.txtPosition.grid(row=6,column=1)

        #===========================DataFrameRIGHT=========================================

        self.Prescription =Text(DataFrameRIGHT, font=('arial',12,'bold'),width =43,height=14,padx=2,pady=4) 
        self.Prescription.grid(row=0, column=0)
        
#===========================Button Frame============================
        
        self.btnPrescription=Button(ButtonFrame,text='Prescription',font=('arial',12,'bold'),width =24,bd=4,
                                    command=Prescription)
        self.btnPrescription.grid(row=0, column=0)

        self.btnSubmit=Button(ButtonFrame,text='Submit Data',font=('arial',12,'bold'),width =24,bd=4,
                                    command=Submit)
        self.btnSubmit.grid(row=0, column=1)

        self.btnDelete=Button(ButtonFrame,text='Delete',font=('arial',12,'bold'),width =24,bd=4,
                                    command=Delete)
        self.btnDelete.grid(row=0, column=2)

        self.btnReset=Button(ButtonFrame,text='Reset',font=('arial',12,'bold'),width =24,bd=4,
                                    command=Reset)
        self.btnReset.grid(row=0, column=3)

        self.btnExit=Button(ButtonFrame,text='Exit',font=('arial',12,'bold'),width =24,bd=4,
                                    command=Exit)
        self.btnExit.grid(row=0, column=4)


        
#if __name__=='__main__':
root = Tk()
application = hospital(root)
root.mainloop()
