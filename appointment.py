import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sqlite3
from tkcalendar import DateEntry

# Connect to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Tkinter window
class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Location Selection")
        self.master.geometry("1000x620+100+50")  # Resolution of the window
        self.master.resizable(True, False)  # Preventing the resize feature

        # Canvas setup
        self.canvas = tk.Canvas(master, width=1000, height=620, bg='lightblue')
        self.canvas.pack()

        # Background Image
        self.bg_image = tk.PhotoImage(file="resources/images123.png")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        # Heading
        self.heading = tk.Label(self.canvas, text="Enter patient details", font=('arial 18'), fg='black', bg='lightblue')
        self.heading.place(x=400, y=50)

        # Patient's name
        self.name_label = tk.Label(self.canvas, text="Patient's Name", font=('arial 12'), fg='black', bg='lightblue')
        self.name_label.place(x=300, y=100)
        self.name_var = tk.StringVar()
        self.name_ent = tk.Entry(self.canvas, width=30, textvariable=self.name_var)
        self.name_ent.place(x=450, y=100)
        self.name_var.trace_add("write", self.validate_name)  # Event binding for real-time validation

        # Age
        self.age_label = tk.Label(self.canvas, text="Age", font=('arial 12'), fg='black', bg='lightblue')
        self.age_label.place(x=300, y=140)
        self.age_var = tk.StringVar()
        self.age_ent = tk.Entry(self.canvas, width=30, textvariable=self.age_var)
        self.age_ent.place(x=450, y=140)
        self.age_var.trace_add("write", self.validate_age)  # Event binding for real-time validation

        # Gender
        self.gender_label = tk.Label(self.canvas, text="Gender", font=('arial 12'), fg='black', bg='lightblue')
        self.gender_label.place(x=300, y=180)
        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")  # Default value
        self.gender_radio_male = tk.Radiobutton(self.canvas, text="Male", variable=self.gender_var, value="Male", font=('arial', 11), bg='lightblue')
        self.gender_radio_male.place(x=450, y=180)
        self.gender_radio_female = tk.Radiobutton(self.canvas, text="Female", variable=self.gender_var, value="Female", font=('arial', 11), bg='lightblue')
        self.gender_radio_female.place(x=510, y=180)
        self.gender_radio_trans = tk.Radiobutton(self.canvas, text="Transgender", variable=self.gender_var, value="Transgender", font=('arial', 11), bg='lightblue')
        self.gender_radio_trans.place(x=590, y=180)

        # Date
        self.date_label = tk.Label(self.canvas, text="Date", font=('arial 12'), fg='black', bg='lightblue')
        self.date_label.place(x=300, y=220)
        self.date_ent = DateEntry(self.canvas, width=27, date_pattern='dd/mm/yyyy')
        self.date_ent.place(x=450, y=220)

        # Location
        self.location_label = tk.Label(self.canvas, text="Location", font=('arial 12'), fg='black', bg='lightblue')
        self.location_label.place(x=300, y=260)
        self.location_var = tk.StringVar()
        self.location_var.set("Select City")  # Default value
        self.location_combobox = ttk.Combobox(self.canvas, textvariable=self.location_var, values=["Chennai", "Trichy","Thanjavur", "Madurai", "Pudukkottai"])
        self.location_combobox.config(width=15, font=('arial', 11))
        self.location_combobox.place(x=450, y=260)

        # Appointment time
        self.time_label = tk.Label(self.canvas, text="Time (HH:MM)", font=('arial 12'), fg='black', bg='lightblue')
        self.time_label.place(x=300, y=300)
        self.time_ent = tk.Entry(self.canvas, width=30)
        self.time_ent.place(x=450, y=300)

        # Phone number
        self.phone_label = tk.Label(self.canvas, text="Phone Number", font=('arial 12'), fg='black', bg='lightblue')
        self.phone_label.place(x=300, y=340)
        self.phone_ent = tk.Entry(self.canvas, width=30)
        self.phone_ent.place(x=450, y=340)

        # Button to add appointment
        self.submit = tk.Button(self.canvas, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=390)

        # Button to go back home
        self.back_home = tk.Button(self.canvas, text="Back Home", width=20, height=2, bg='steelblue', command=root.destroy)
        self.back_home.place(x=490, y=390)

    # Function to call when the submit button is clicked
    def add_appointment(self):
        # Getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_var.get()
        self.val4 = self.location_var.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

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

# Creating the object
root = tk.Tk()
app = MyApp(root)

# Title of the window
root.title("Add new appointment")

# End the loop
root.mainloop()
