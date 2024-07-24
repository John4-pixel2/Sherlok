import tkinter as tk
from tkinter import messagebox#, scrolledtext
#import requests
#from bs4 import BeautifulSoup
#import random
from tkinter import PhotoImage

class GameInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Sherlock Holmes: The Marilyn Monroe Case - Game")
        self.root.geometry("800x600")
        
# Creating the main window
root = tk.Tk()
root.title("Sherlock Holmes: The Marilyn Monroe Case")
root.geometry("800x600")

root.title("Time Traveler Detective")
#image_path=PhotoImage(file=r"Images_For_Sherlok/Präsentation1.jpg")
#bg_image=tkinter.Label(root, image=image_path)
#bg_image.pack()

label = tk.Label(root, text="Sherlock Holmes: The Marilyn Monroe Case", font=('Arial', 23))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height= 3, font=('Arial, 16'))
textbox.pack(padx=10)

myentry = tk.Entry(root)
myentry.pack()


self.button= tk.Button(self.root, text = show Message, font, command =self.show_messge()