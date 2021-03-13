from tkinter import *
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox

class hospital:
    def __init__(self,Root):
        self.root = Root
        self.root.title("Patient CheckOut")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

        
        Gender=StringVar()
        Name=StringVar()       
        Age=StringVar()
        PhoneNo=StringVar()
        Address=StringVar()
        Disease=StringVar()
        DateIn=StringVar()
        DateOut=StringVar()
        RoomNo=StringVar()
        RoomType=StringVar()
        UnitPrice=StringVar()
        Building=StringVar()
        Status=StringVar()
        MedicineandServicesPrice=StringVar()
        Price=StringVar()

        #==================All Button=============================
        Prescription=StringVar()
        Submit=StringVar()
        Delete=StringVar()
        Reset=StringVar()
        Exit=StringVar()

        def Prescription():
            self.Prescription.insert(END,'Patient Name: \t\t' + Name.get() + "\n")
            self.Prescription.insert(END,'Gender: \t\t' + Gender.get() + "\n")
            self.Prescription.insert(END,'Age: \t\t' + Age.get() + "\n")
            self.Prescription.insert(END,'Phone No: \t\t' + PhoneNo.get() + "\n")
            self.Prescription.insert(END,'Address: \t\t' + Address.get() + "\n")
            self.Prescription.insert(END,'Disease: \t\t' + Disease.get() + "\n")
            self.Prescription.insert(END,'Price: \t\t' + Price.get() + "\n")
            self.Prescription.insert(END,'Date In: \t\t' + DateIn.get() + "\n")
            self.Prescription.insert(END,'Date Out: \t\t' + DateOut.get() + "\n")
            self.Prescription.insert(END,'Room No: \t\t' + RoomNo.get() + "\n")
            self.Prescription.insert(END,'Room Type: \t\t' + RoomType.get() + "\n")
            self.Prescription.insert(END,'Unit Price: \t\t' + UnitPrice.get() + "\n")
            self.Prescription.insert(END,'Building: \t\t' + Building.get() + "\n")
            self.Prescription.insert(END,'Status: \t\t' + Status.get() + "\n")
            self.Prescription.insert(END,'Medicine and Services Price: \t\t' + MedicineandServicesPrice.get() + "\n")
            
            return

        def submit():
            return

        def Delete():
            self.cboGender.current(0)
            Gender.set("")
            Name.set("")       
            Age.set("")
            PhoneNo.set("")
            Address.set("")
            Disease.set("")
            DateIn.set("")
            DateOut.set("")
            RoomNo.set("")
            RoomType.set("")
            UnitPrice.set("")
            Building.set("")
            Status.set("")
            MedicineandServicesPrice.set("")
            Price.set("")
            return

        def Reset():
            Gender.set("")
            Name.set("")       
            Age.set("")
            PhoneNo.set("")
            Address.set("")
            Disease.set("")
            DateIn.set("")
            DateOut.set("")
            RoomNo.set("")
            RoomType.set("")
            UnitPrice.set("")
            Building.set("")
            Status.set("")
            MedicineandServicesPrice.set("")
            Price.set("")
            self.Prescription.delete("1.0",END)
            return

        def Exit():
            Exit=tkinter.messagebox.askyesno("Patient Cheak Out","Confirm if you want to Exit")
            if Exit >0:
                root.destroy()
            


        MainFrame =Frame(self.root)
        MainFrame.grid()

        TitleFrame =Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame,
                             font=('arial',40,'bold'),
                             text="Patient CheckOut",padx=2)
        self.lblTitle.grid()

        FrameDetail =Frame(MainFrame, bd=20, width=1350, height=180, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame =Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=20, width=1350, height=300, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE,
                                  font=('arial',12,'bold'), text="Patient ChekOut")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=450, height=400, padx=20, relief=RIDGE,
                                   font=('arial',12,'bold'), text="Patient Details")
        DataFrameRIGHT.pack(side=RIGHT)

#===========================DataFrameLEFT=========================================
        self.lblGender =Label(DataFrameLEFT,
                                  font=('arial',12,'bold'),
                                  text="Gender:",padx=2)
        self.lblGender.grid(row=1, column=0,sticky=W)

        self.cboGender=ttk.Combobox(DataFrameLEFT,textvariable=Gender,
                                        state='readonly',font=('arial',11,'bold'), width=20)
        
        self.cboGender['value']=('','Male','Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=1, column=1)
        
        self.lblName =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Name of Patient:",padx=2)
        self.lblName.grid(row=0, column=0,sticky=W)
        self.txtName=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Name)
        self.txtName.grid(row=0, column=1)
        
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

        self.lblDisease =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Disease:",padx=2)
        self.lblDisease.grid(row=6, column=0,sticky=W)
        self.txtDisease=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Disease)
        self.txtDisease.grid(row=6,column=1)

        self.lblPrice =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Price:",padx=2)
        self.lblPrice.grid(row=7, column=0,sticky=W)
        self.txtPrice=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Price)
        self.txtPrice.grid(row=7,column=1)

#=====================Data Frame Left 'second column'======================================================

        self.lblDateIn =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Date In:",padx=2)
        self.lblDateIn.grid(row=0, column=2,sticky=W)
        self.txtDateIn=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DateIn)
        self.txtDateIn.grid(row=0,column=3)

        self.lblDateOut =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Date Out:",padx=2)
        self.lblDateOut.grid(row=1, column=2,sticky=W)
        self.txtDateOut=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DateOut)
        self.txtDateOut.grid(row=1,column=3)

        self.lblRoomNo =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Room No:",padx=2)
        self.lblRoomNo.grid(row=2, column=2,sticky=W)
        self.txtRoomNo=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=RoomNo)
        self.txtRoomNo.grid(row=2,column=3)

        self.lblRoomType =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Room Type:",padx=2)
        self.lblRoomType.grid(row=3, column=2,sticky=W)
        self.txtRoomType=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=RoomType)
        self.txtRoomType.grid(row=3,column=3)

        self.lblUnitPrice =Label(DataFrameLEFT, font=('arial',12,'bold'), text="UnitPrice:",padx=2)
        self.lblUnitPrice.grid(row=4, column=2,sticky=W)
        self.txtUnitPrice=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=UnitPrice)
        self.txtUnitPrice.grid(row=4,column=3)

        self.lblBuilding =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Building:",padx=2)
        self.lblBuilding.grid(row=5, column=2,sticky=W)
        self.txtBuilding=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Building)
        self.txtBuilding.grid(row=5,column=3)

        self.lblStatus =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Status:",padx=2)
        self.lblStatus.grid(row=6, column=2,sticky=W)
        self.txtStatus=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Status)
        self.txtStatus.grid(row=6,column=3)

        self.lblMedicineandServicesPrice =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Medicine and Services Price:",padx=2)
        self.lblMedicineandServicesPrice.grid(row=7, column=2,sticky=W)
        self.txtMedicineandServicesPrice=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=MedicineandServicesPrice)
        self.txtMedicineandServicesPrice.grid(row=7,column=3)

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
