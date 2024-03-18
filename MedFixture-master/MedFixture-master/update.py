# update the appointments
# import modules
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
    import tkinter as tk
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect('database.db')
c = conn.cursor()

class App:
    def __init__(self, master):
        self.master = master
        # heading label
        self.heading = Label(master, text="Update Appointments",  fg='black', font=('arial 18'))
        self.heading.place(x=180, y=40)

        # search criteria -->name 
        self.name = Label(master, text="Enter Patient's Name", font=('arial 12'))
        self.name.place(x=70, y=100)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=300, y=100)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=230, y=150)
    
    
    # function to search
    def search_db(self):
        self.input = self.namenet.get()

        # execute sql 
        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]
        
        # creating the update form
        self.uname = Label(self.master, text="Patient's Name", font=('arial 12'))
        self.uname.place(x=70, y=220)

        self.uage = Label(self.master, text="Age", font=('arial 12'))
        self.uage.place(x=70, y=260)

        self.ugender = Label(self.master, text="Gender", font=('arial 12'))
        self.ugender.place(x=70, y=300)

        self.ulocation = Label(self.master, text="Location", font=('arial 12'))
        self.ulocation.place(x=70, y=340)

        self.utime = Label(self.master, text="Appointment Time (HH:MM)", font=('arial 12'))
        self.utime.place(x=70, y=380)

        self.uphone = Label(self.master, text="Phone Number", font=('arial 12'))
        self.uphone.place(x=70, y=420)

        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=220)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=260)
        self.ent2.insert(END, str(self.age))

        # gender list
        GenderList = ["Male",
        "Female",
        "Transgender"]

        # Option menu
        self.var = tk.StringVar()
        self.var.set(GenderList[0])

        self.opt = tk.OptionMenu(self.master, self.var, *GenderList)
        self.opt.config(width=10, font=('arial', 11))
        self.opt.place(x=300, y=300)

        # callback method
        def callback(*args):
            for i in range(len(GenderList)):
                if GenderList[i] == self.var.get():
                    # print(GenderList[i])
                    self.gender = GenderList[i]
                    break
        
        self.var.trace("w", callback)

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=340)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=380)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=420)
        self.ent6.insert(END, str(self.phone))

        # button to execute update
        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=200, y=480)
    
    
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated age
        self.var3 = self.gender #updated gender
        self.var4 = self.ent4.get() #updated location
        self.var5 = self.ent5.get() #updated phone
        self.var6 = self.ent6.get() #updated time

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")


#creating the object
root = tk.Tk()
b = App(root)
root.geometry("640x620+100+50")
root.resizable(False, False)
root.title("Update Appointment")
root.iconphoto(False, tk.PhotoImage(file='resources/icon.png'))

# end the loop
root.mainloop()