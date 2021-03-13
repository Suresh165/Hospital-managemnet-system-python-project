# import modules
from tkinter import *
import sqlite3
import tkinter.messagebox
# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move around the databse
c = conn.cursor()

# empty list to later append the ids from the database
ids = []

# tkinter window
class Application:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1350x750+0+0")
        self.master.configure(background='powder blue')

        # creating the frames in the master

        TitleFrame =Frame(master, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame,
                             font=('arial',40,'bold'),
                             text="Patient Login",padx=2)
        self.lblTitle.grid()

        FrameDetail =Frame(master, bd=20, width=1350, height=180, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame =Frame(master, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame =Frame(master, bd=20, width=1350, height=300, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE,
                                  font=('arial',12,'bold'), text="")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=450, height=400, padx=20, relief=RIDGE,
                                   font=('arial',12,'bold'), text="Patient Details")
        DataFrameRIGHT.pack(side=RIGHT)
        

        # patients name
        self.name = Label(DataFrameLEFT,font=('arial',12,'bold'), text="Name:",padx=2)
        self.name.grid(row=0,column=0,sticky=W)

        # age
        self.age = Label(DataFrameLEFT, font=('arial',12,'bold'), text="Password:",padx=2)
        self.age.grid(row=2,column=0,sticky=W)

        

        # Entries for all labels============================================================
        self.name_ent = Entry(DataFrameLEFT, font=('arial',12,'bold'))
        self.name_ent.grid(row=1,column=0)

        self.age_ent = Entry(DataFrameLEFT, font=('arial',12,'bold'))
        self.age_ent.grid(row=3,column=0)
    
        

        # button to perform a command
        self.submit = Button(ButtonFrame, text="Submit", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.grid(row=0,column=1)
    
        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
        
        # ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        # displaying the logs in our right frame

        self.box = Text(DataFrameRIGHT, width=50, height=20)
        self.box.grid(row=1,column=0)
        self.box.insert(END, "Total Submit now :  " + str(self.final_id))
    # funtion to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (name, age) VALUES(?, ?)"
            c.execute(sql, (self.val1, self.val2))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for \n" +str(self.val1) + " has been created" )
            

            self.box.insert(END, '\n Name: ' + str(self.val1) + ' Password: ' + str(self.val2))
           

# creating the object
root = Tk()
b = Application(root)

# resolution of the window
#root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()
