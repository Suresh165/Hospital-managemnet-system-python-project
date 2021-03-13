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
        self.root.title("Add New Ward")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

        Building=StringVar()
        Floor=StringVar()
        RoomNo=StringVar()
        Room_Type=StringVar()
        Number_of_Bed=StringVar()
        Unit_Price=StringVar()
        #==================All Button=============================
        Prescription=StringVar()
        Submit=StringVar()
        Delete=StringVar()
        Reset=StringVar()
        Exit=StringVar()

        def Prescription():
            self.Prescription.insert(END,'Building: \t\t' + self.cboBuilding.get() + "\n")
            self.Prescription.insert(END,'Floor: \t\t' + self.cboFloor.get() + "\n")
            self.Prescription.insert(END,'Room No: \t\t' + self.cboRoomNo.get() + "\n")
            self.Prescription.insert(END,'Room Type: \t\t' + self.cboRoom_Type.get() + "\n")
            self.Prescription.insert(END,'Number of Bed: \t\t' + self.txtNumber_of_Bed.get() + "\n")
            self.Prescription.insert(END,'Unit Price: \t\t' + self.txtUnit_Price.get() + "\n")
            return

        def Submit():
            global con
            global cur
            sql = "insert into `add_new_ward`(`Building`,`Floor`,`RoomNo`,`Room_Type`,`Number_of_Bed`,`Unit_Price`) values('{}','{}','{}','{}','{}','{}')". format(Building.get(),Floor.get(),RoomNo.get(),Room_Type.get(),Number_of_Bed.get(),Unit_Price.get())
            print(sql)
            cur.execute(sql)
            con.commit()

        def Delete():
            Building.set("")
            self.cboBuilding.current(0)
            Floor.set("")
            self.cboFloor.current(0)
            RoomNo.set("")
            self.cboRoomNo.current(0)
            Room_Type.set("")
            self.cboRoom_Type.current(0)
            Number_of_Bed.set("")
            self.txtNumber_of_Bed
            Unit_Price.set("")
            self.delete("1.0",END)
            return

        def Reset():
            Building.set("")
            self.cboBuilding.current(0)
            Floor.set("")
            RoomNo.set("")
            Room_Type.set("")
            Number_of_Bed.set("")
            Unit_Price.set("")
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
                             text="Add New Ward",padx=2)
        self.lblTitle.grid()

        FrameDetail =Frame(MainFrame, bd=20, width=1350, height=180, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame =Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=20, width=1350, height=300, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE,
                                  font=('arial',12,'bold'), text="Add New Ward")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=450, height=400, padx=20, relief=RIDGE,
                                   font=('arial',12,'bold'), text="Patient Details")
        DataFrameRIGHT.pack(side=RIGHT)

#===========================DataFrameLEFT=========================================

        self.lblBuilding =Label(DataFrameLEFT,
                                  font=('arial',12,'bold'),
                                  text="Building:",padx=2)
        self.lblBuilding.grid(row=0, column=0,sticky=W)

        self.cboBuilding=ttk.Combobox(DataFrameLEFT,textvariable=Building,
                                        state='readonly',font=('arial',11,'bold'), width=20)
        
        self.cboBuilding['value']=('','A','B','C','D','E','F')
        self.cboBuilding.current(0)
        self.cboBuilding.grid(row=0, column=1)

        

        self.lblFloor =Label(DataFrameLEFT,
                                  font=('arial',12,'bold'),
                                  text="Floor:",padx=2)
        self.lblFloor.grid(row=1, column=0,sticky=W)

        self.cboFloor=ttk.Combobox(DataFrameLEFT,textvariable=Floor,
                                        state='readonly',font=('arial',11,'bold'), width=20)
        
        self.cboFloor['value']=('','First','Second','Thired','Fourth','Five','Six')
        self.cboFloor.current(0)
        self.cboFloor.grid(row=1, column=1)
        
        
        self.lblRoomNo =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Room No:",padx=2)
        self.lblRoomNo.grid(row=2, column=0,sticky=W)
        self.cboRoomNo=ttk.Combobox(DataFrameLEFT,textvariable=RoomNo,
                                        state='readonly',font=('arial',11,'bold'), width=20)
        
        self.cboRoomNo['value']=('','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=2, column=1)

        self.lblRoom_Type =Label(DataFrameLEFT,
                                  font=('arial',12,'bold'),
                                  text="Room_Type:",padx=2)
        self.lblRoom_Type.grid(row=3, column=0,sticky=W)

        self.cboRoom_Type=ttk.Combobox(DataFrameLEFT,textvariable=Room_Type,
                                        state='readonly',font=('arial',11,'bold'), width=20)
        
        self.cboRoom_Type['value']=('','Normal','Medium','VIP')
        self.cboRoom_Type.current(0)
        self.cboRoom_Type.grid(row=3, column=1)
        
        self.lblNumber_of_Bed =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Number of Bed:",padx=2)
        self.lblNumber_of_Bed.grid(row=4, column=0,sticky=W)
        self.txtNumber_of_Bed=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Number_of_Bed)
        self.txtNumber_of_Bed.grid(row=4,column=1)

        self.lblUnit_Price =Label(DataFrameLEFT, font=('arial',12,'bold'), text="Unit Price:",padx=2)
        self.lblUnit_Price.grid(row=5, column=0,sticky=W)
        self.txtUnit_Price=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Unit_Price)
        self.txtUnit_Price.grid(row=5,column=1)

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
