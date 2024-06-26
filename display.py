try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import sqlite3

# Connection to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

class App:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='lightblue')  # Set background color for the main window

        # background
        self.canvas = Canvas(master, width=1400, height=600, bg='lightblue')
        self.canvas.pack()

    #  # Creating the format in master
    #     self.canvas = Canvas(master, width=1400, height=600)
    #     self.canvas.pack()

        # Background Image
        self.bg_image = PhotoImage(file="resources/images123.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_image)

        # heading label
        self.heading = Label(master, text="Display Appointments",  fg='black', font=('arial 18'), bg='lightblue')
        self.heading.place(x=400, y=50)

        # search criteria -->name 
        self.name = Label(master, text="Enter Patient's Name", font=('arial 12'), bg='lightblue')
        self.name.place(x=300, y=100)

        # entry for the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=450, y=100)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=300, y=180)

        # back button
        self.search = Button(master, text="Back Home", width=12, height=1, bg='steelblue', command=root.destroy)
        self.search.place(x=450, y=180)

    
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
        # ===================entries for each label
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

root = Tk()
b = App(root)
root.geometry("1000x620+100+50")
root.resizable(True, False)
root.title("Display Appointment")
root.mainloop()
