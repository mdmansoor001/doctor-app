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
        self.master.configure(bg='lightblue')  # Set background color for the main window

        # background
        self.canvas = Canvas(master, width=1400, height=600, bg='lightblue')
        self.canvas.pack()

        #  background
        # self.canvas = Canvas(master, width=1400, height=600)
        # self.canvas.pack()

        self.bg_image = PhotoImage(file="resources/images123.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_image)


        # heading label
        self.heading = Label(master, text="Delete Appointments",  fg='black', font=('arial 18'), bg='lightblue')
        self.heading.place(x=400, y=50)

        # search criteria -->name 
        self.name = Label(master, text="Enter Patient's Name", font=('arial 12'), bg='lightblue')
        self.name.place(x=300, y=100)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=490, y=100)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=300, y=180)

        #back button            
        self.search = Button(self.master, text="Back Home", width=12, height=1, bg='steelblue', command=root.destroy)
        self.search.place(x=400, y=180)
    
    
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
        self.uname = Label(self.master, text="Patient's Name", font=('arial 12'), bg='lightblue')
        self.uname.place(x=70, y=220)

        self.uage = Label(self.master, text="Age", font=('arial 12'), bg='lightblue')
        self.uage.place(x=70, y=260)

        self.ugender = Label(self.master, text="Gender", font=('arial 12'), bg='lightblue')
        self.ugender.place(x=70, y=300)

        self.ulocation = Label(self.master, text="Location", font=('arial 12'), bg='lightblue')
        self.ulocation.place(x=70, y=340)

        self.utime = Label(self.master, text="Appointment Time (HH:MM)", font=('arial 12'), bg='lightblue')
        self.utime.place(x=70, y=380)

        self.uphone = Label(self.master, text="Phone Number", font=('arial 12'), bg='lightblue')
        self.uphone.place(x=70, y=420)

        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Label(self.master, text=self.name1, font=('arial 12'), bg='lightblue')
        self.ent1.place(x=300, y=220)

        self.ent2 = Label(self.master, text=self.age, font=('arial 12'), bg='lightblue')
        self.ent2.place(x=300, y=260)

        self.ent3 = Label(self.master, text=self.gender, font=('arial 12'), bg='lightblue')
        self.ent3.place(x=300, y=300)

        self.ent4 = Label(self.master, text=self.location, font=('arial 12'), bg='lightblue')
        self.ent4.place(x=300, y=340)

        self.ent5 = Label(self.master, text=self.time, font=('arial 12'), bg='lightblue')
        self.ent5.place(x=300, y=380)

        self.ent6 = Label(self.master, text=self.phone, font=('arial 12'), bg='lightblue')
        self.ent6.place(x=300, y=420)

        # button to execute delete
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=200, y=480)

      
    
    
    def delete_db(self):
        if tkinter.messagebox.askyesno("Are you sure?", "Delete record of "+self.name1+"?"):
            # delete the appointment
            sql2 = "DELETE FROM appointments WHERE name LIKE ?"
            c.execute(sql2, (self.namenet.get(),))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Deleted Successfully")


#creating the object
root = tk.Tk()
b = App(root)
root.geometry("1000x620+100+50")
root.resizable(True, False)
root.title("Delete Appointment")
root.iconphoto(False, tk.PhotoImage(file='resources/icon.png'))

# end the loop
root.mainloop()
