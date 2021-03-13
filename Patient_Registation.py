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

        PID=StringVar()
        Name=StringVar()
        Gender=StringVar()
        Age=StringVar()
        PhoneNo=StringVar()
        Address=StringVar()
        Date=StringVar()
        Disease=StringVar()        
        Building=StringVar()
        RoomNo=StringVar()
        Room_Type=StringVar()
        Status_of_Price=StringVar()
        Price=StringVar()
        #==================All Button=============================
        Prescription=StringVar()
        Submit=StringVar()
        Delete=StringVar()
        Reset=StringVar()
        Exit=StringVar()

        def Prescription():
            self.Prescription.insert(END,'PID: \t\t' + PID.get() + "\n")
            self.Prescription.insert(END,'Name of Patient: \t\t' + Name.get() + "\n")
            self.Prescription.insert(END,'Gender: \t\t' + Gender.get() + "\n")
            self.Prescription.insert(END,'Age of Patient: \t\t' + Age.get() + "\n")
            self.Prescription.insert(END,'Phone No: \t\t' + PhoneNo.get() + "\n")
            self.Prescription.insert(END,'Address: \t\t' + Address.get() + "\n")
            self.Prescription.insert(END,'Date: \t\t' + Date.get() + "\n")
            self.Prescription.insert(END,'Disease: \t\t' + Disease.get() + "\n")
            self.Prescription.insert(END,'Building: \t\t' + Building.get() + "\n")
            self.Prescription.insert(END,'Room No: \t\t' + RoomNo.get() + "\n")
            self.Prescription.insert(END,'Room Type: \t\t' + Room_Type.get() + "\n")
            self.Prescription.insert(END,'Status of Price: \t\t' + Status_of_Price.get() + "\n")
            self.Prescription.insert(END,'Price: \t\t' + Price.get() + "\n")
            return

        def Submit():
            global con
            global cur
            sql = "insert into `Patient_registration`(`PID`,`Name`,`Gender`,`Age`,`PhoneNo`,`Address`,`Date`,`Disease`,`Building`,`RoomNo`,`Room_Type`,`Status_of_Price`,`Price`) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')". format(PID.get(),Name.get(),Gender.get(),Age.get(),PhoneNo.get(),Address.get(),Date.get(),Disease.get(),Building.get(),RoomNo.get(),Room_Type.get(),Status_of_Price.get(),Price.get())
            print(sql)
            cur.execute(sql)
            con.commit()

        def Delete():
            PID.set("")
            self.cboGender.current(0)
            Name.set("")
            Gender.set("")
            Age.set("")
            PhoneNo.set("")
            Address.set("")
            Date.set("")
            Disease.set("")        
            Building.set("")
            RoomNo.set("")
            Room_Type.set("")
            Status_of_Price.set("")
            Price.set("")
            return

        def Reset():
            PID.set("")
            self.cboGender.current(0)
            Name.set("")
            Gender.set("")
            Age.set("")
            PhoneNo.set("")
            Address.set("")
            Date.set("")
            Disease.set("")        
            Building.set("")
            RoomNo.set("")
            Room_Type.set("")
            Status_of_Price.set("")
            Price.set("")
            self.Prescription.delete("1.0",END)
            return

        def Exit():
            iExit=tkinter.messagebox.askyesno("Patient Registration","Confirm if you want to Exit")
            if iExit >0:
                root.destroy()


        MainFrame =Frame(self.root)
        MainFrame.grid()

        TitleFrame =Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame,
                             font=('arial',40,'bold'),
                             text="Patient Registration",padx=2)
        self.lblTitle.grid()

        FrameDetail =Frame(MainFrame, bd=20, width=1350, height=180, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame =Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=20, width=1350, height=300, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE,
                                  font=('arial',12,'bold'), text="Patient Registation")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=450, height=400, padx=20, relief=RIDGE,
                                   font=('arial',12,'bold'), text="Patient Details")
        DataFrameRIGHT.pack(side=RIGHT)

        

#===========================DataFrameLEFT=========================================

        self.lblPID =Label(DataFrameLEFT, font=('arial',12,'bold'), text="PID:",padx=2)
        self.lblPID.grid(row=0, column=0,sticky=W)
        self.txtPID=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PID)
        self.txtPID.grid(row=0, column=1)

        self.lblName =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Name of Patient:",padx=2)
        self.lblName.grid(row=1, column=0,sticky=W)
        self.txtName=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Name)
        self.txtName.grid(row=1, column=1)
        
        self.lblGender =Label(DataFrameLEFT,
                                  font=('arial',12,'bold'),
                                  text="Gender:",padx=2)
        self.lblGender.grid(row=2, column=0,sticky=W)

        self.cboGender=ttk.Combobox(DataFrameLEFT,textvariable=Gender,
                                        state='readonly',font=('arial',11,'bold'), width=20)
        
        self.cboGender['value']=('','Male','Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=2, column=1)
        
        
        
        self.lblAge =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Age of Patient:",padx=2)
        self.lblAge.grid(row=3, column=0,sticky=W)
        self.txtAge=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Age)
        self.txtAge.grid(row=3, column=1)

        self.lblPhoneNo =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Phone No:",padx=2)
        self.lblPhoneNo.grid(row=4, column=0,sticky=W)
        self.txtPhoneNo=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PhoneNo)
        self.txtPhoneNo.grid(row=4,column=1)

        self.lblAddress =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Address of Patient:",padx=2)
        self.lblAddress.grid(row=5, column=0,sticky=W)
        self.txtAddress=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Address)
        self.txtAddress.grid(row=5,column=1)

        self.lblDate =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Date:",padx=2)
        self.lblDate.grid(row=6, column=0,sticky=W)
        self.txtDate=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Date)
        self.txtDate.grid(row=6,column=1)

        self.lblDisease =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Disease:",padx=2)
        self.lblDisease.grid(row=7, column=0,sticky=W)
        self.txtDisease=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Disease)
        self.txtDisease.grid(row=7,column=1)

#=====================Data Frame Left 'second column'=====================================

        self.lblBuilding =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Building:",padx=2)
        self.lblBuilding.grid(row=0, column=2,sticky=W)
        self.cboBuilding=ttk.Combobox(DataFrameLEFT,textvariable=Building,
                                        state='readonly',font=('arial',11,'bold'), width=20)
        
        self.cboBuilding['value']=('','A','B','C','D','E','F')
        self.cboBuilding.current(0)
        self.cboBuilding.grid(row=0, column=3)

        self.lblRoomNo =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Room No:",padx=2)
        self.lblRoomNo.grid(row=1, column=2,sticky=W)
        self.cboRoomNo=ttk.Combobox(DataFrameLEFT,textvariable=RoomNo,
                                        state='readonly',font=('arial',11,'bold'), width=20)
        
        self.cboRoomNo['value']=('','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=1, column=3)

        self.lblRoomType =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Room Type:",padx=2)
        self.lblRoomType.grid(row=2, column=2,sticky=W)
        self.cboRoomType=ttk.Combobox(DataFrameLEFT,textvariable=Room_Type,
                                        state='readonly',font=('arial',11,'bold'), width=20)
        
        self.cboRoomType['value']=('','Normal','Medium','VIP')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=2, column=3)

        self.lblStatus_of_Price =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Status of Price:",padx=2)
        self.lblStatus_of_Price.grid(row=3, column=2,sticky=W)
        self.txtStatus_of_Price=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Status_of_Price)
        self.txtStatus_of_Price.grid(row=3,column=3)

        self.lblPrice =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Price:",padx=2)
        self.lblPrice.grid(row=4, column=2,sticky=W)
        self.txtPrice=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Price)
        self.txtPrice.grid(row=4,column=3)

        #===========================DataFrameRIGHT=========================================

        self.Prescription =Text(DataFrameRIGHT, font=('arial',12,'bold'),width =43,height=14,padx=2,pady=4) 
        self.Prescription.grid(row=0, column=0)
        
#===========================Button Frame============================
        
        self.btnPrescription=Button(ButtonFrame,text='Patient Details',font=('arial',12,'bold'),width =24,bd=4,
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
