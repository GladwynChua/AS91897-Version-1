
#Import the required libraries
from tkinter import *
import tkinter as tk
from tkinter import Label 
import sys
 

def link():
   print("Loading.....")
   print("Directing to Main Menu")
   

   
#Create an instance of Tkinter frame
win = Tk()

#Set the geometry of the Tkinter library
win.geometry("850x530")
win.attributes("-fullscreen", True)

label = Label(win, text="Multiple Choice  Quiz",
                      width=80, bg="maroon", fg="white", font=("Ariel", 50, "bold"))

label.pack(pady= 40)

#Add Menu
popup = Menu(win, tearoff=0)

def menu_popup(event):
   # display the popup menu
   try:
      popup.tk_popup(event.x_root, event.y_root, 0)
   finally:
      #Release the grab
      popup.grab_release()   
    

border_color = Frame(win, background="black")

button = tk.Button(border_color, text="Start", command=win.destroy, width = 80, height = 10)
button.pack(padx=2, pady=2)
border_color.pack(padx=20, pady=20)

button_2 = tk.Button(border_color, text="Quit", command = quit, width = 80, height = 10)
button_2.pack(padx=2, pady=2)
border_color.pack(padx=20, pady=20)

def quit():
   sys.exit()

mainloop()




