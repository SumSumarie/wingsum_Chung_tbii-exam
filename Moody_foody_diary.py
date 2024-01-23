import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
from datetime import date
from tkcalendar import Calendar
from tkcalendar import DateEntry
import pandas as pd
#from dateutil.relativedelta import relativedelta
#from tkinter import ttk
#import random
#from create_new_user import create_new_user_page

#set tk as root
root = tk.Tk()
#give it a title
root.title("Moody Foody Diary")
#change the size
screen_width= 350
screen_height= 650
root.minsize(screen_width,screen_height)

def clean_widget():
    for i in root.winfo_children():
        i.destroy()


def add_image(root, file_path, width, height):
    global pic, f1
    f1= tk.Frame(root)
    img = Image.open(file_path)
    #change the size of the image
    img = img.resize((width,height), Image.LANCZOS)
    pic=ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

def create_new_user_page():

    clean_widget()
    # add the image in the homepage
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    #create a home page button
    homepage=tk.Button(root,
                       text="🏠",
                       command=create_diary)

    homepage.place(relx = 0.2,anchor = 'ne',y=15)

    new_user_page_label=tk.Label(root,
                           text=(f"{name.get()}, "
                                 "now you have your own Moody Foody Diary"),
                           font=("Optima", 15,"bold")
                            )
    new_user_page_label.place(relx = 0.5,anchor = 'center',y=100)

    #get the date of today
    current_date = date.today()
    #add a calendar to choose the date of today
    cal = Calendar(root, selectmode='day',
                   year=current_date.year, month=current_date.month,
                   day=current_date.day)

    cal.place(relx = 0.5,anchor = 'center',y=300)

    view_diary = tk.Button(root,
                          text="View Diary"
                          )

    view_diary.place(relx=0.5, anchor='center', y=400)

    new_diary = tk.Button(root,
                         text="+",
                         font=("Optima", 30, "bold"),
                         command=mood_emoji_page
                         )

    new_diary.place(relx=0.9, anchor='center', y=600)


def mood_emoji_page():

    clean_widget()
    question = tk.Label(root,
                        text=(f"{name.get()}, How are you today?"),
                        font=("Optima", 15, "bold")
                        )
    question.place(relx=0.5, anchor='center', y=100)

    #adding smile emoji
    smile_emoji = tk.Button(root,
                          text="😀",
                          font=("Optima", 25, "bold")
                          )

    smile_emoji.place(relx=0.15, anchor='center', y=200)
    # adding sad emoji
    sad_emoji = tk.Button(root,
                            text="🥹",
                            font=("Optima", 25, "bold")
                            )

    sad_emoji.place(relx=0.3, anchor='center', y=200)
    # adding smile emoji
    cheerful_emoji = tk.Button(root,
                          text="🥳",
                          font=("Optima", 25, "bold")
                          )

    cheerful_emoji.place(relx=0.45, anchor='center', y=200)
    # adding smile emoji
    star_eyes_emoji = tk.Button(root,
                               text="🤩",
                               font=("Optima", 25, "bold")
                               )

    star_eyes_emoji.place(relx=0.6, anchor='center', y=200)





def create_returning_user_page():
    global return_email, return_password
    clean_widget()
    #add the image in the homepage
    add_image(root, 'images/beginning_smile.png',screen_width,screen_height)
    #create a home page button
    homepage=tk.Button(root,
                       text="🏠",
                       command=create_diary)
    homepage.place(relx = 0.2,anchor = 'ne',y=15)

    return_page_label=tk.Label(root,
                           text="WELCOME BACK to "
                                "your Moody Foody Diary",
                           font=("Optima", 15,"bold")
                            )
    return_page_label.place(relx = 0.5,anchor = 'center',y=100)
    # print a message asking the user for their email
    return_email_label = tk.Label(root, text='Email', font='optima 20 bold', borderwidth=3)
    # where would you like to place this button
    return_email_label.place(x=20,y=250)
    return_email=tk.StringVar()
    return_email_entry=tk.Entry(root,
                        textvar=email,
                        font='optima 20 bold',
                        width=15)
    return_email_entry.place(x=130,y=250)

    # print a message asking the user for their password
    return_password_label = tk.Label(root, text='password', font='optima 20 bold', borderwidth=3)
    # where would you like to place this button
    return_password_label.place(x=20, y=300)
    return_password = tk.StringVar()
    return_password_entry = tk.Entry(root,
                           textvar=password,
                           font='optima 20 bold',
                           width=15)
    return_password_entry.place(x=130, y=300)
    #create the button to click to create_returning_user_page
    open_diary_button = tk.Button(root,
                              text="Open your diary",
                              font='optima 15 bold',
                              command=create_returning_user_page)
    open_diary_button.place(relx=0.5, anchor='center', y=400)

def enter_user_data():
    """this is the definition of storing data of the users"""
    #create a timestamp
    current_timestamp=datetime.now()

    user_data = {
        "name":name.get(),
        "email":email.get(),
        "birthday": birthday.get(),
        "create_at":current_timestamp
    }

    #get the list of user ids
    user_ids=list(pd.read_csv("data/users_data.csv").user_id)

    if email.get() in user_ids:
        tk.messagebox.showwarning("warning","This email is taken")
    else:
        #converting the dictionary to a data frame
        user_data_df=pd.DataFrame([user_data])
        user_data_df.to_csv("data/users_data.csv",index=False,header=False,mode='a')
        for i in root.winfo_children():
            i.destroy()

        thank_button=tk.Label(root,
                 text=(f"Thank you for submitting your data {name.get()}")
                 )
        thank_button.place(x=150,y=200)

        print(user_data_df)

def create_diary():
    global name, email, birthday, password
    clean_widget()
    #add the image in the homepage
    add_image(root, 'images/beginning_smile.png',screen_width,screen_height)
    # print a message saying 'Open your Moody Foody Diary'
    title_label = tk.Label(root, text='This is your Moody Foody Diary', font='optima 20 bold',bg='light yellow', borderwidth=25)
    # where would you like to place this button
    title_label.place(relx = 0.5,anchor = 'center',y=150)

    # print a message asking the user for their name
    name_label = tk.Label(root, text='Name', font='optima 20 bold', borderwidth=3)
    # where would you like to place this button
    name_label.place(x=20,y=250)
    name=tk.StringVar()
    name_entry=tk.Entry(root,
                        textvar=name,
                        font='optima 20 bold',
                        width=15)
    name_entry.place(x=130,y=250)
    # print a message asking the user for their email
    email_label = tk.Label(root, text='Email', font='optima 20 bold', borderwidth=3)
    # where would you like to place this button
    email_label.place(x=20,y=300)
    email=tk.StringVar()
    email_entry=tk.Entry(root,
                        textvar=email,
                        font='optima 20 bold',
                        width=15)
    email_entry.place(x=130,y=300)

    # print a message asking the user for their password
    password_label = tk.Label(root, text='password', font='optima 20 bold', borderwidth=3)
    # where would you like to place this button
    password_label.place(x=20, y=350)
    password = tk.StringVar()
    password_entry = tk.Entry(root,
                           textvar=password,
                           font='optima 20 bold',
                           width=15)
    password_entry.place(x=130, y=350)

    # print a message asking the user for their birthday
    birthday_label = tk.Label(root, text='Birthday', font='optima 20 bold', borderwidth=3)
    # where would you like to place this button
    birthday_label.place(x=20,y=400)
    #place a calender behind the label birthday
    cal = DateEntry(root,
                    width=18,
                    height=55,
                    selectmode="day")
    cal.place(x=130, y=400)
    birthday= cal.get_date()

    #create the button to click to create_new_user_page
    new_user_button=tk.Button(root,
                            text="create your diary",
                            font='optima 20 bold',
                            command=create_new_user_page)
    new_user_button.place(relx = 0.5,anchor = 'center',y=500)

    #create the button to click to create_returning_user_page
    return_user_button = tk.Button(root,
                              text="Already have your diary?",
                              font='optima 15 bold',
                              command=create_returning_user_page)
    return_user_button.place(relx=0.5, anchor='center', y=600)





#initiate pygame
#pg.init()
#load the music
#pg.mixer.music.load("music/music.mp3")
#play the music
#pg.mixer.music.play()

#start with the create_diary page
create_diary()

#execute the code
root.mainloop()