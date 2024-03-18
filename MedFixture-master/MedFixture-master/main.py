import os
import customtkinter as ctk
import tkinter as tk
import subprocess
from PIL import Image, ImageTk

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

ctk.set_appearance_mode("System") 

ctk.set_default_color_theme("green")    
 
appWidth, appHeight = 800, 900 



def run_another_file():
    subprocess.run(['python', 'appointment.py'])
def delete():
    subprocess.run(['python', 'delete.py']) 
def display():
    subprocess.run(['python', 'display.py']) 
def update():
    subprocess.run(['python', 'update.py'])
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
   
     
        # self.generateResultsButton = ctk.CTkButton(self,
        #                                  text="Create Appointment",command = run_another_file)
    
        image = Image.open("resources/images.png")
        photo = ImageTk.PhotoImage(image)

        self.background_label = tk.Label(self, image=photo)
        self.background_label.image = photo
        self.background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.title("Doc Appointment")
        self.geometry(f"{appWidth}x{appHeight}")
        self.resizable(True,False)

        

        self.generateResultsButton = ctk.CTkButton(self,
                                           text="Create Appointment",
                                           command=run_another_file,
                                           font =('Helvetica', 30))  # Adjust the font size as needed
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")
        self.generateResultsButton1 = ctk.CTkButton(self,
                                         text="View Appointment",command = display,font =('Helvetica', 30))
        self.generateResultsButton1.grid(row=6, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")
        self.generateResultsButton2 = ctk.CTkButton(self,command = update ,text="Update Appointment",font =('Helvetica', 30))
        self.generateResultsButton2.grid(row=7, column=1,
                                        columnspan=2,
                                        padx=20, pady=20,
                                        sticky="ew")
        self.generateResultsButton3 = ctk.CTkButton(self,
                                         text="Delete Appointment",command = delete,font =('Helvetica', 30))
        self.generateResultsButton3.grid(row=8, column=1,
                                        columnspan=2,   
                                        padx=20, pady=20,
                                        sticky="ew")
 

 
if __name__ == "__main__":
    app = App()
    app.mainloop()