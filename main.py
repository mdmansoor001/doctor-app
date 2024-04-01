import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess

class AppointmentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Doc Appointment")
        self.geometry("1000x620+100+50")
        
        # Load and resize the background image
        image = Image.open("resources/doclogo1.png")
        image = image.resize((1400,650), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(image)

        # Create a label with the background image
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Buttons
        button_font = ('Helvetica', 30)
        buttons = [
            ("Create Appointment", run_another_file),
            ("View Appointment", display),
            ("Update Appointment", update),
            ("Delete Appointment", delete),
        ]

        # Grid buttons in one column and center them
        for index, (button_text, command) in enumerate(buttons):
            button = tk.Button(self, text=button_text, command=command, font=button_font, bg='lightblue')
            button.grid(row=index, column=2, padx=20, pady=20, sticky="ew", columnspan=3)

    def close_window(self):
        self.destroy()

def run_another_file():
    subprocess.run(['python', 'appointment.py'])

def delete():
    subprocess.run(['python', 'delete.py'])

def display():
    subprocess.run(['python', 'display.py'])

def update():
    subprocess.run(['python', 'update.py'])

# Resolution of the window


if __name__ == "__main__":
    app = AppointmentApp()
    app.mainloop()
