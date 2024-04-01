try:
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
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

        self.bg_image = PhotoImage(file="resources/images123.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_image)

        # heading label
        self.heading = Label(master, text="Update Appointments",  fg='black', font=('arial 18'),bg='lightblue')
        self.heading.place(x=400, y=50)

        # search criteria -->name 
        self.name = Label(master, text="Enter Patient's Name", font=('arial 12'),bg='lightblue')
        self.name.place(x=300, y=100)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=490, y=100)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=300, y=180)

        # back button          
        self.search = Button(master, text="Back Home", width=12, height=1, bg='steelblue', command=root.destroy)
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
        self.uname = Label(self.master, text="Patient's Name", font=('arial 12'),bg='lightblue')
        self.uname.place(x=70, y=220)

        self.uage = Label(self.master, text="Age", font=('arial 12'),bg='lightblue')
        self.uage.place(x=70, y=260)

        self.ugender = Label(self.master, text="Gender", font=('arial 12'),bg='lightblue')
        self.ugender.place(x=70, y=300)

        self.ulocation = Label(self.master, text="Location", font=('arial 12'),bg='lightblue')
        self.ulocation.place(x=70, y=340)

        self.utime = Label(self.master, text="Appointment Time (HH:MM)", font=('arial 12'),bg='lightblue')
        self.utime.place(x=70, y=380)

        self.uphone = Label(self.master, text="Phone Number", font=('arial 12'),bg='lightblue')
        self.uphone.place(x=70, y=420)

        # entries for each labels
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=220)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=260)
        self.ent2.insert(END, str(self.age))

        # gender list
        GenderList = ["Male", "Female", "Transgender"]

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



        # Checking for input validation
        if not all([self.val1, self.val2, self.val3, self.val4, self.val5, self.val6]):
            tkinter.messagebox.showwarning("Warning", "Please fill up all the details")
        elif not self.val2.isdigit():
            tkinter.messagebox.showwarning("Warning", "Age must be a number")
        elif not self.val6.isdigit() or len(self.val6) != 10:
            tkinter.messagebox.showwarning("Warning", "Phone number must be a 10-digit number")
        else:
            # Inserting data into the database
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success", f"Appointment for {self.val1} has been created")

    # Function to validate name in real-time
    def validate_name(self, *args):
        if not self.name_var.get().isalpha():
            tkinter.messagebox.showerror("ERROR", "Name must contain only alphabetic characters")

    # Function to validate age in real-time
    def validate_age(self, *args):
        if not self.age_var.get().isdigit():
            tkinter.messagebox.showerror("ERROR", "Age must be a number")

#creating the object
root = tk.Tk()
b = App(root)
root.geometry("1000x620+100+50")
root.resizable(True, False)
root.title("Update Appointment")
root.iconphoto(False, tk.PhotoImage(file='resources/icon.png'))

# end the loop
root.mainloop()
