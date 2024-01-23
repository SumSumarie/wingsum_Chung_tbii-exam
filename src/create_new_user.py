import tkinter as tk
from Moody_foody_diary_Dec31 import create_diary
from PIL import Image, ImageTk
from datetime import datetime
from datetime import date
from tkcalendar import Calendar
from tkcalendar import DateEntry
from tkinter import ttk
import random

#set tk as root
root = tk.Tk()
#give it a title
root.title("Moody Foody Diary")
#change the size
screen_width= 350
screen_height= 650
root.minsize(screen_width,screen_height)
def create_new_user_page():

    for i in root.winfo_children():
        i.destroy()
    # add the image in the homepage
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    #create a home page button
    homepage=tk.Button(root,
                       text="🏠",
                       command=create_diary)

    homepage.place(relx = 0.2,anchor = 'ne',y=15)

    new_user_page_label=tk.Label(root,
                           text="Now you have created "
                                "your own Moody Foody Diary",
                           font=("Optima", 15,"bold")
                            )
    new_user_page_label.place(relx = 0.5,anchor = 'center',y=100)

#execute the code
root.mainloop()