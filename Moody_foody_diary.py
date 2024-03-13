import tkinter as tk
from datetime import datetime
from datetime import date
from tkcalendar import Calendar
import pandas as pd
from src.helper import clear_widgets, add_image
from tkinter import messagebox
import pygame as pg
import random

#set tk as root
root = tk.Tk()
#give it a title
root.title("Moody Foody Diary")
#change the size of the screen
screen_width= 350
screen_height= 650
root.minsize(screen_width,screen_height)

def home_button():
    """This is a definition of the button for going back to home page """
    # create and place a home page button
    homepage = tk.Button(root,
                         text="🏠",
                         command=home_page)
    homepage.place(relx=0.5, anchor='center', y=620)

def back_button(page):
    """This is a definition of the button for going back to the previous page"""
    #create and place a Back button
    back=tk.Button(root,
                    text="⬅",
                    command=page
                   )
    back.place(relx = 0.2,anchor = 'ne',y=15)

def show_today_date():
    """This is a definition to show the date of today on each page of selection"""
    #set current_date as the date of today
    current_date = date.today()
    # add and place a label for today's date
    today_date_label = tk.Label(root,
                                text=(f"{current_date}"),
                                font=("Optima", 15, "bold"),
                                bg='light yellow'
                                )
    today_date_label.place(y=20,x=250)


def enter_user_data():
    """This is the definition of storing data of the users"""
    global current_timestamp
    #create a timestamp
    current_timestamp=datetime.now()
    #call the birthday
    birthday = cal.get_date()
    # get the list of user ids
    user_ids = list(pd.read_csv("data/user_data.csv").username)

    #warining message box will be shown when the username or the magic key were taken
    if username.get() in user_ids:
        tk.messagebox.showwarning("warning", "This username is taken")
        return False
    #if the username was not taken, then store the data of the username, birthday and the current timestamp in the user_data.csv file
    else:
        user_data = {
            "username":username.get(),
            "birthday": birthday,
            "create_at":current_timestamp
        }
        # converting the dictionary to a data frame
        user_data = pd.DataFrame([user_data])
        user_data.to_csv("data/user_data.csv", index=False, header=False, mode='a')
        return True

def home_page():
    """This the definition of showing the starting page """
    global username, magic_key, birthday
    # clean all the widgets from the previous page
    clear_widgets(root)
    # initiate pygame
    pg.init()
    # load the music
    pg.mixer.music.load("music/home_page.mp3")
    # play the music
    pg.mixer.music.play()
    #add the image in the home page
    add_image(root, 'images/cover.jpg',screen_width,screen_height)
    # add a message saying 'Open your Moody Foody Diary'
    title_label = tk.Label(root,
                           text='---------Moody Foody Diary---------',
                           font='optima 25 bold',
                           bg='light yellow',
                           borderwidth=20)
    title_label.place(relx = 0.5,anchor = 'center',y=100)
    #add the button to for new user page
    new_user_button=tk.Button(root,
                            text="New User",
                            font='optima 20 bold',
                            command=new_user_page)
    new_user_button.place(relx = 0.5,anchor = 'center',y=500)
    #add the button to for return user page
    return_user_button=tk.Button(root,
                            text="Return User",
                            font='optima 20 bold',
                            command=check_return_user)
    return_user_button.place(relx = 0.5,anchor = 'center',y=550)

def new_user_page():
    """This is a definition of the register page for new users to create their username and enter their birthday"""
    global username,cal
    # clean all the widgets from the previous page
    clear_widgets(root)
    #add the image in the new user page
    add_image(root, 'images/beginning_smile.png',screen_width,screen_height)
    #place the button to go back to home page from the home_button definition
    home_button()
    # add the title of 'Moody Foody Diary'
    title_label = tk.Label(root,
                           text='---------Moody Foody Diary---------',
                           font='optima 25 bold',
                           bg='light yellow',
                           borderwidth=20)
    title_label.place(relx = 0.5,anchor = 'center',y=100)
    # add a message asking the user for their username
    username_label = tk.Label(root, text='Username', font='optima 20 bold', borderwidth=3)
    username_label.place(x=20,y=250)
    #add a user-name entry box
    username=tk.StringVar()
    username_entry=tk.Entry(root,
                        textvar=username,
                        font='optima 20 bold',
                        width=15)
    username_entry.place(x=130,y=250)
    # add a message asking the user for their birthday
    birthday_label = tk.Label(root, text='Birthday', font='optima 20 bold', borderwidth=3)
    birthday_label.place(x=20,y=350)
    # add a calendar behind the label birthday( The style of the calender: https://pypi.org/project/tkcalendar/)
    cal = Calendar(root,
                    font="Arial 8",
                    selectmode="day",
                    style='my.DateEntry',
                    date_pattern='Y-mm-dd',
                    foreground="red",
                    selectforeground="red"
                    )
    cal.place(x=130, y=350)

    # add the button to click to create a Moody Foody Diary
    create_diary_button = tk.Button(root,
                                    text="Create your Moody Foody Diary",
                                    font='optima 20 bold',
                                    command=after_create_diary_button
                                    )
    create_diary_button.place(relx=0.5, anchor='center', y=550)


def after_create_diary_button():
    """This is the definition for the instruction after clicking the button "Create your Moody Foody Diary" in the new_user_page"""
    global current_user,birthday_date
    #add if-else statement to add constrains when the date of birthday are the same date of today and the user didn't type in the username
    if str(cal.get_date())!=str(datetime.now().date()) and username.get():
        #When the birthday is not the same date of today and the user type in the username, it will get the username and the selected birthday, and wait for displaying in calendar_page_new page
        if enter_user_data():
            current_user = username.get()
            birthday_date=str(cal.get_date())
            calendar_page_new()
    if str(cal.get_date())==str(datetime.now().date()):
        # when the selected birthday is the same of the date of today, show the error message
        error_message = tk.Label(text="Are you sure you are born today?",
                                 bg="red",
                                 fg="white"
                                 )
        error_message.place(relx=0.65, anchor='center', y=520)
    if not username.get():
        # when the user didn't type in the username, show the error message
        error_message = tk.Label(text="You have not entered your username",
                                 bg="red",
                                 fg="white"
                                 )
        error_message.place(relx=0.65, anchor='center', y=300)


def check_return_user():
    """This is a definition of the page for return user to enter"""
    global username
    # clean all the widgets from the previous page
    clear_widgets(root)
    #add the image in the main page
    add_image(root, 'images/beginning_smile.png',screen_width,screen_height)
    #place the button to go back to main page from the home_button definition
    home_button()
    # add the title of "Moody Foody Diary"
    title_label = tk.Label(root,
                           text='---------Moody Foody Diary---------',
                           font='optima 25 bold',
                           bg='light yellow',
                           borderwidth=20)
    title_label.place(relx = 0.5,anchor = 'center',y=100)
    # add a message asking the user for their username
    username_label = tk.Label(root, text='Username', font='optima 20 bold', borderwidth=3)
    username_label.place(x=20, y=250)
    # add a user-name entry box
    username = tk.StringVar()
    username_entry = tk.Entry(root,
                              textvar=username,
                              font='optima 20 bold',
                              width=15)
    username_entry.place(x=130, y=250)
    #add the button to click to enter your diary
    enter_diary_button=tk.Button(root,
                            text="Enter your diary",
                            font='optima 20 bold',
                            command=check_entry
                                 )
    enter_diary_button.place(relx = 0.5,anchor = 'center',y=500)

def check_entry():
    """This is a definition for the return page to show when the user didn't type in the username, or the username has not been registered """
    global current_user, birthday_date
    # when the user types in the username, it will check with the data in the dataframe
    if username.get():
        current_user = username.get()
        user_data = pd.read_csv("data/user_data.csv")
        #read the birthday in the dataframe
        for i in user_data.index:
            if user_data.loc[i, "username"] == current_user:
                birthday_date = user_data.loc[i, "birthday"]
    # if the user doesn't type in the username, it is show the error message
    else:
        error_message = tk.Label(text="You have not entered your username")
        error_message.place(relx=0.5, anchor='center', y=300)

    #check the csv file to see if the username matched the one in the dataframe or not
    user_data=pd.read_csv("data/user_data.csv")

    for i in user_data.index:
        # if the username matches the one in the dataframe, then it will go to calendar_page_return
         if current_user==user_data.loc[i,"username"]:
             calendar_page_return()
             break
        # if the username doesn't match the one in the dataframe, then it will show the error messages and the button for going back to new user page
         else:
             error_message = tk.Label(text="You haven't registered.")
             error_message.place(relx=0.5, anchor='center', y=300)
             error_message2 = tk.Label(text="Would you like to register as new user?")
             error_message2.place(relx=0.5, anchor='center', y=350)
             # add the button to for new user page
             new_user_button = tk.Button(root,
                                         text="New User",
                                         font='optima 20 bold',
                                         command=new_user_page)
             new_user_button.place(relx=0.5, anchor='center', y=550)

def return_user_page():
    """This is a definition of the return user page after the user selected "return user" on the first page"""
    global current_user
    #clean all the widgets from the previous page
    clear_widgets(root)
    #add the image in the main page
    add_image(root, 'images/beginning_smile.png',screen_width,screen_height)
    #place the button to go back to main page from the home_button definition
    home_button()
    # add a welcome message
    title_label = tk.Label(root,
                           text='This is your Moody Foody Diary',
                           font='optima 20 bold',
                           bg='light yellow',
                           borderwidth=25)
    title_label.place(relx = 0.5,anchor = 'center',y=150)
    # add a message asking the user for their username
    username_label = tk.Label(root, text='Username', font='optima 20 bold', borderwidth=3)
    username_label.place(x=20,y=300)
    #add a username entry box
    username=tk.StringVar()
    username_entry=tk.Entry(root,
                        textvar=username,
                        font='optima 20 bold',
                        width=15)
    username_entry.place(x=130,y=300)


def calendar_page_new():
    """This is definition of a calendar page after the register page for new users"""
    # clean all the widgets from the previous page
    clear_widgets(root)
    # add the background image in this page
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(new_user_page)
    #place the button to go back to main page from the home_button definition
    home_button()
    #add a create_diary button for entering the diary information
    create_diary = tk.Button(root,
                            text="Create a new diary",
                            font=("Optima", 25, "bold"),
                            command=mood_colour_page
                            )
    create_diary.place(relx=0.5, anchor='center', y=520)
    #add a label to show the username
    welcome_label=tk.Label(root,
                           text=(current_user),
                           font=("Optima", 40,"bold"),
                           bg='light pink'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=100)
    #add labels to show the welcoming messages "Welcome to your own Moody Foody Diary"
    welcome_label=tk.Label(root,
                           text=("Welcome to"),
                           font=("Optima", 20,"bold"),
                           bg='orange'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=160)
    welcome_label=tk.Label(root,
                           text=("your own"),
                           font=("Optima", 25,"bold"),
                           bg='yellow'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=200)
    welcome_label=tk.Label(root,
                           text=("Moody Foody Diary"),
                           font=("Optima", 25,"bold"),
                           bg='light green'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=240)
    # add a label for today's date
    show_today_date()
    #add labels to show the surprise message of birthday
    birthday_date_label=tk.Label(root,
                                 text=("There will be a little surprise"),
                                 font=("Optima", 25,"bold"),
                                 bg='light blue'
                                 )
    birthday_date_label.place(relx = 0.5,anchor = 'center',y=320)
    birthday_date_label=tk.Label(root,
                                 text=("for you in your birthday"),
                                 font=("Optima", 25,"bold"),
                                 bg='light blue'
                                 )
    birthday_date_label.place(relx = 0.5,anchor = 'center',y=360)
    # add a label to show the birthday that the users selected in the register page for new users
    birthday_date_label=tk.Label(root,
                                 text=(birthday_date),
                                 font=("Optima", 30,"bold"),
                                 bg='light pink'
                                 )
    birthday_date_label.place(relx = 0.5,anchor = 'center',y=400)


def calendar_page_return():
    """This is definition of the calendar page after creating a new diary """
    global current_date, mood_colour
    # clean all the widgets from the previous page
    clear_widgets(root)
    # add the image in the homepage
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(home_page)
    #place the button to go back to main page from the home_button definition
    home_button()
    # add the button for viewing the existing diaries
    view_diary = tk.Button(root,
                           font=("Optima", 25, "bold"),
                           text="View your diaries",
                           #The reference of binding two commands: (https: // www.geeksforgeeks.org / how - to - bind - multiple - commands - to - tkinter - button /)
                           command=lambda:[get_selected_date(),view_diary_page(selected_date)]
                           )
    view_diary.place(relx=0.5, anchor='center', y=450)
    #add a button for writing another new diary
    create_diary = tk.Button(root,
                         text="Create a new diary",
                         font=("Optima", 25, "bold"),
                         command=mood_colour_page
                         )
    create_diary.place(relx=0.5, anchor='center', y=520)
    #add username of the current user
    username_label=tk.Label(root,
                           text=(current_user),
                           font=("Optima", 25,"bold"),
                           bg='light yellow'
                            )
    username_label.place(relx = 0.5,anchor = 'center',y=100)
    #add welcome labels to show the message "Welcome to your own Moody Foody Diary"
    welcome_label=tk.Label(root,
                           text=("Welcome to"),
                           font=("Optima", 20,"bold"),
                           bg='light yellow'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=140)
    welcome_label=tk.Label(root,
                           text=("your own Moody Foody Diary"),
                           font=("Optima", 25,"bold"),
                           bg='light yellow'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=180)
    # get the date of today
    current_date = date.today()
    # reade the dataframe to get the username in the current user
    diary_data=pd.read_csv("data/user_mood_data.csv")
    diary_data=diary_data.loc[diary_data["username"]==current_user]
    #get the information of the last line in the dataframe of there are multiple entry on the same day(https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html)
    current_entry = diary_data.loc[diary_data["created_at"] == str(current_date)].tail(1)
    #fetch the value of the variable mood_colour in the dataframe
    mood_colour = current_entry["mood_colour"].values[0]
    #add a calender with the colour of the date changing based on the mood_colour the user selected for their diary
    global cal
    cal = Calendar(root,
                   selectmode='day',
                   year=current_date.year,
                   month=current_date.month,
                   day=current_date.day,
                   date_pattern='Y-mm-dd',
                   foreground="red",
                   #this is for changing the colour of the date based on mood_colour
                   selectforeground=f"{mood_colour}"
                   )
    cal.place(relx=0.5, anchor='center', y=320)
    #bind the function of change_colour_of_date to selecting the date in the calender(Virtual Events: https://tkcalendar.readthedocs.io/en/stable/Calendar.html)
    cal.bind("<<CalendarSelected>>", change_colour_of_date)

    def get_selected_date():
        """This is a definition for getting the selected birthday"""
        global selected_date
        selected_date=str(cal.get_date())

def change_colour_of_date(event):
    """This is a definition of changing the colour of the date for the calender, which will bind with the <<CalendarSelected>>"""
    selected_date = str(cal.selection_get())
    diary_data = pd.read_csv("data/user_mood_data.csv")
    diary_data = diary_data.loc[diary_data["username"] == current_user]
    current_entry = diary_data.loc[diary_data["created_at"] == str(selected_date)].tail(1)

    #if there is diary entry on that day, the colour of that day in the calendar will be the mood colour
    if len(current_entry) > 0:
        mood_colour = current_entry["mood_colour"].values[0]
        cal.configure(selectforeground=f"{mood_colour}")

    #if there is no diary entry on that day, the colour of that day in the calendar will be white
    else:
        cal.configure(selectforeground="white")


def mood_colour_page():
    """This is a page for selecting the mood colour"""
    # clean all the widgets from the previous page
    clear_widgets(root)
    # add the background image with colourful smiling faces in the mood_colour_page
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(calendar_page_new)
    #place the button to go back to home page from the home_button definition
    home_button()
    #add a message asking for the colour of the mood today
    question_label = tk.Label(root, text='What is the colour of your mood today?',
                              font='optima 18 bold',
                              bg='light yellow',
                              fg='black',
                              borderwidth=12)
    question_label.place(relx=0.5, anchor='center', y=100)
    #Add the button to choose red as the colour of the mood today
    red_button = tk.Button(text=':)',
                           fg='red',
                           font='Arial 20 bold',
                           height=2,
                           width=10,
                           command=lambda: mood_emoji_page("red_button")
                           )
    red_button.place(relx=0.5, rely=0.57, anchor='center', y=-195)
     #Add the button to choose orange as the colour of the mood today
    orange_button = tk.Button(text=':)',
                              fg='orange',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda: mood_emoji_page("orange_button")
                              )
    orange_button.place(relx=0.5, rely=0.57, anchor='center', y=-130)
    # Add the button to choose yellow as the colour of the mood today
    yellow_button = tk.Button(text=':)',
                              fg='yellow',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda: mood_emoji_page("yellow_button")
                              )
    yellow_button.place(relx=0.5, rely=0.57, anchor='center', y=-65)
    # Add the button to choose green as the colour of the mood today
    green_button = tk.Button(text=':)',
                             fg='green',
                             font='Arial 20 bold',
                             height=2,
                             width=10,
                             command=lambda: mood_emoji_page("green_button")
                             )
    green_button.place(relx=0.5, rely=0.57, anchor='center', y=0)
    # Add the button to choose Indigo as the colour of the mood today
    cyan_button = tk.Button(text=':)',
                            fg='cyan',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda: mood_emoji_page("cyan_button")
                            )
    cyan_button.place(relx=0.5, rely=0.57, anchor='center', y=65)
    # Add the button to choose blue as the colour of the mood today
    blue_button = tk.Button(text=':)',
                            fg='blue',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda: mood_emoji_page("blue_button")
                            )
    blue_button.place(relx=0.5, rely=0.57, anchor='center', y=130)
    # Add the button to choose purple as the colour of the mood today
    purple_button = tk.Button(text=':)',
                              fg='purple',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda: mood_emoji_page("purple_button")
                              )
    purple_button.place(relx=0.5, rely=0.57, anchor='center', y=195)

    #adding the label to show the date of today at the right top corner
    show_today_date()

def mood_emoji_page(mood_colour_button):
    """this is the page to choose the mood emoji"""
    global mood_colour,options,mood_emoji,emoji_button
    #when the users chose red button, it will randomly pick the recipes related to the colour red
    if mood_colour_button == "red_button":
        mood_colour = "red"
        options = ["red01.jpg", "red02.jpg", "red03.jpg"]
    # when the users chose orange button, it will randomly pick the recipes related to the colour orange
    elif mood_colour_button == "orange_button":
        mood_colour = "orange"
        options = ["orange01.jpg", "orange02.jpg", "orange03.jpg"]
    # when the users chose yellow button, it will randomly pick the recipes related to the colour yellow
    elif mood_colour_button == "yellow_button":
        mood_colour = "yellow"
        options = ["yellow01.jpg", "yellow02.jpg", "yellow03.jpg"]
    # when the users chose green button, it will randomly pick the recipes related to the colour green
    elif mood_colour_button == "green_button":
        mood_colour = "green"
        options = ["green01.jpg", "green02.jpg", "green03.jpg"]
    #when the users chose cyan button, it will randomly pick the recipes related to the colour cyan
    elif mood_colour_button == "cyan_button":
        mood_colour = "cyan"
        options = ["cyan01.jpg", "cyan02.jpg", "cyan03.jpg"]
    # when the users chose blue button, it will randomly pick the recipes related to the colour blue
    elif mood_colour_button == "blue_button":
        mood_colour = "blue"
        options = ["blue01.jpg", "blue02.jpg", "blue03.jpg"]
    # when the users chose purple button, it will randomly pick the recipes related to the colour purple
    elif mood_colour_button == "purple_button":
        mood_colour = "purple"
        options = ["purple01.jpg", "purple02.jpg", "purple03.jpg"]
    # clean all the widgets from the previous page
    clear_widgets(root)
    # add background image with the selected mood colour in the mood_emoji_page
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(mood_colour_page)
    #place the button to go back to main page from the home_button definition
    home_button()
    # adding the label to show the date of today at the right top corner
    show_today_date()
    #add the label for asking the mood
    question_label = tk.Label(root, text='What is your mood today?',
                              font='optima 18 bold',
                              bg='light yellow',
                              fg='black',
                              borderwidth=12)
    question_label.place(relx=0.5, anchor='center', y=100)

    # add grinning_emoji button
    grinning_emoji = tk.Button(root,
                            text="😀",
                            font=("Optima", 25, "bold"),
                            height=1,
                            width=1,
                            command=lambda:weather_page("grinning_emoji")
                            )
    grinning_emoji.place(relx=0.2, rely=0.2, anchor='center', y=50)

    # add beaming_emoji button
    beaming_emoji = tk.Button(root,
                          text="😁",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page("beaming_emoji")
                          )
    beaming_emoji.place(relx=0.2, rely=0.2, anchor='center', y=100)

    # add smiling_emoji button
    smiling_emoji = tk.Button(root,
                               text="☺️",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page("smiling_emoji")
                               )

    smiling_emoji.place(relx=0.2, rely=0.2, anchor='center', y=150)

    # add heart_eyes_emoji button
    heart_eyes_emoji = tk.Button(root,
                                text="😍",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("heart_eyes_emoji")
                                )
    heart_eyes_emoji.place(relx=0.2, rely=0.2, anchor='center', y=200)

    # add heart_emoji button
    heart_emoji = tk.Button(root,
                                text="🥰",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("heart_emoji")
                                )
    heart_emoji.place(relx=0.2, rely=0.2, anchor='center', y=250)

    # add winking_emoji button
    winking_emoji = tk.Button(root,
                                text="😉",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("winking_emoji")
                                )
    winking_emoji.place(relx=0.2, rely=0.2, anchor='center', y=300)

    # add face_savoring_emoji button
    face_savoring_emoji = tk.Button(root,
                                text="😋",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("face_savoring_emoji")
                                )
    face_savoring_emoji.place(relx=0.2, rely=0.2, anchor='center', y=350)

    # add sunglasses_emoji button
    sunglasses_emoji = tk.Button(root,
                            text="😎",
                            font=("Optima", 25, "bold"),
                            height=1,
                            width=1,
                            command=lambda:weather_page("sunglasses_emoji")
                            )
    sunglasses_emoji.place(relx=0.4, rely=0.2, anchor='center', y=50)

    # add star_struck_emoji
    star_struck_emoji = tk.Button(root,
                          text="🤩",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page("star_struck_emoji")
                          )
    star_struck_emoji.place(relx=0.4, rely=0.2, anchor='center', y=100)

    # add partying_emoji button
    partying_emoji = tk.Button(root,
                               text="🥳",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page("partying_emoji")
                               )
    partying_emoji.place(relx=0.4, rely=0.2, anchor='center', y=150)

    # add zany_face_emoji button
    zany_face_emoji = tk.Button(root,
                                text="🤪",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("zany_face_emoji")
                                )
    zany_face_emoji.place(relx=0.4, rely=0.2, anchor='center', y=200)

    # add tongue_emoji button
    tongue_emoji = tk.Button(root,
                                text="😝",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("tongue_emoji")
                                )
    tongue_emoji.place(relx=0.4, rely=0.2, anchor='center', y=250)

    # add tears_of_joy_emoji button
    tears_of_joy_emoji = tk.Button(root,
                                text="😂",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("tears_of_joy_emoji")
                                )
    tears_of_joy_emoji.place(relx=0.4, rely=0.2, anchor='center', y=300)

    # add single_tear_emoji button
    single_tear_emoji = tk.Button(root,
                                text="🥲",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("single_tear_emoji")
                                )
    single_tear_emoji.place(relx=0.4, rely=0.2, anchor='center', y=350)

    # add unamused_emoji button
    unamused_emoji = tk.Button(root,
                            text="😒",
                            font=("Optima", 25, "bold"),
                            height=1,
                            width=1,
                            command=lambda:weather_page("unamused_emoji")
                            )
    unamused_emoji.place(relx=0.6, rely=0.2, anchor='center', y=50)

    # add confounded_emoji button
    confounded_emoji = tk.Button(root,
                          text="😖",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page("confounded_emoji")
                          )
    confounded_emoji.place(relx=0.6, rely=0.2, anchor='center', y=100)

    # add tired_emoji button
    tired_emoji = tk.Button(root,
                               text="😫",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page("tired_emoji")
                               )
    tired_emoji.place(relx=0.6, rely=0.2, anchor='center', y=150)

    # add pleading_emoji button
    pleading_emoji = tk.Button(root,
                                text="🥺",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("pleading_emoji")
                                )
    pleading_emoji.place(relx=0.6, rely=0.2, anchor='center', y=200)

    # add steam_nose_emoji button
    steam_nose_emoji = tk.Button(root,
                                text="😤",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("steam_nose_emoji")
                                )
    steam_nose_emoji.place(relx=0.6, rely=0.2, anchor='center', y=250)

    # add crying_emoji button
    crying_emoji = tk.Button(root,
                                text="😭",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("crying_emoji")
                                )
    crying_emoji.place(relx=0.6, rely=0.2, anchor='center', y=300)

    # add enraged_emoji button
    enraged_emoji = tk.Button(root,
                                text="😡",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("enraged_emoji")
                                )
    enraged_emoji.place(relx=0.6, rely=0.2, anchor='center', y=350)

    # add swear_emoji button
    swear_emoji = tk.Button(root,
                            text="🤬",
                            font=("Optima", 25, "bold"),
                            height=1,
                            width=1,
                            command=lambda:weather_page("swear_emoji")
                            )
    swear_emoji.place(relx=0.8, rely=0.2, anchor='center', y=50)

    # add exploding_head_emoji button
    exploding_head_emoji = tk.Button(root,
                          text="🤯",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page("exploding_head_emoji")
                          )
    exploding_head_emoji.place(relx=0.8, rely=0.2, anchor='center', y=100)

    # add flushed_face_emoji button
    flushed_face_emoji = tk.Button(root,
                               text="😳",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page("flushed_face_emoji")
                               )
    flushed_face_emoji.place(relx=0.8, rely=0.2, anchor='center', y=150)

    # add fear_emoji button
    fear_emoji = tk.Button(root,
                                text="😱",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("fear_emoji")
                                )
    fear_emoji.place(relx=0.8, rely=0.2, anchor='center', y=200)

    # add anxious_emoji button
    anxious_emoji = tk.Button(root,
                                text="😰",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("anxious_emoji")
                                )
    anxious_emoji.place(relx=0.8, rely=0.2, anchor='center', y=250)

    # add dizziness_emoji button
    dizziness_emoji = tk.Button(root,
                                text="😵‍💫",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("dizziness_emoji")
                                )
    dizziness_emoji.place(relx=0.8, rely=0.2, anchor='center', y=300)

    # add sleeping_emoji button
    sleeping_emoji = tk.Button(root,
                                text="😴",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("sleeping_emoji")
                                )
    sleeping_emoji.place(relx=0.8, rely=0.2, anchor='center', y=350)



def weather_page(emoji_button):
    """This is definition of a page asking the weather of today"""
    global mood_colour, mood_colour_button,mood_emoji
    # clean all the widgets from the previous page
    clear_widgets(root)

    #add different mood emojis to different emoji buttons
    if emoji_button=="grinning_emoji":
        mood_emoji="😀"
    elif emoji_button=="beaming_emoji":
        mood_emoji="😁"
    elif emoji_button=="smiling_emoji":
        mood_emoji="☺️"
    elif emoji_button=="beaming_emoji":
        mood_emoji="😁"
    elif emoji_button=="heart_eyes_emoji":
        mood_emoji="😍"
    elif emoji_button=="heart_emoji":
        mood_emoji="🥰"
    elif emoji_button=="winking_emoji":
        mood_emoji="😉"
    elif emoji_button=="face_savoring_emoji":
        mood_emoji="😋"
    elif emoji_button=="sunglasses_emoji":
        mood_emoji="😎"
    elif emoji_button=="partying_emoji":
        mood_emoji="🥳"
    elif emoji_button=="star_struck_emoji":
        mood_emoji="🤩"
    elif emoji_button=="zany_face_emoji":
        mood_emoji="🤪️"
    elif emoji_button=="tongue_emoji":
        mood_emoji="😝"
    elif emoji_button=="tears_of_joy_emoji":
        mood_emoji="😂"
    elif emoji_button=="single_tear_emoji":
        mood_emoji="🥲"
    elif emoji_button == "unamused_emoji":
        mood_emoji = "😒"
    elif emoji_button == "confounded_emoji":
        mood_emoji = "😖"
    elif emoji_button == "tired_emoji":
        mood_emoji = "😫"
    elif emoji_button == "pleading_emoji":
        mood_emoji = "🥺"
    elif emoji_button == "steam_nose_emoji":
        mood_emoji = "😤"
    elif emoji_button == "crying_emoji":
        mood_emoji = "😭"
    elif emoji_button == "enraged_emoji":
        mood_emoji = "😡"
    elif emoji_button == "swear_emoji":
        mood_emoji = "🤬"
    elif emoji_button == "exploding_head_emoji":
        mood_emoji = "🤯"
    elif emoji_button == "flushed_face_emoji":
        mood_emoji = "😳"
    elif emoji_button == "fear_emoji":
        mood_emoji = "😱"
    elif emoji_button == "anxious_emoji":
        mood_emoji = "😰"
    elif emoji_button == "dizziness_emoji":
        mood_emoji = "️😵‍💫"
    elif emoji_button == "sleeping_emoji":
        mood_emoji = "😴"

    # add background image with the selected mood colour in the weather page
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(lambda:mood_emoji_page(f'{mood_emoji}'))
    #place the button to go back to main page from the home_button definition
    home_button()
    # adding the label to show the date of today at the right top corner
    show_today_date()

    #add a message to ask the weather of today
    question_label = tk.Label(root,
                              text='What is the weather today?',
                              font='optima 18 bold',
                              bg='light yellow',
                              fg='black',
                              borderwidth=12)
    question_label.place(relx=0.5, anchor='center', y=100)

    # Add the button to choose sunny
    sunny_button = tk.Button(text='☀️',
                           font='Arial 20 bold',
                           height=2,
                           width=10,
                           command=lambda:health_page("sunny_button")
                           )
    sunny_button.place(relx=0.5, rely=0.57, anchor='center', y=-195)
    # Add the button to choose sunny with clouds
    sunny_with_clouds_button = tk.Button(text='🌤️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:health_page("sunny_with_clouds_button")
                              )
    sunny_with_clouds_button.place(relx=0.5, rely=0.57, anchor='center', y=-130)
    # Add the button to choose cloudy
    cloudy_button= tk.Button(text='☁️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:health_page("cloudy_button")
                              )
    cloudy_button.place(relx=0.5, rely=0.57, anchor='center', y=-65)
    # The button to choose rain with sun
    rain_with_sun_button = tk.Button(text='🌦️',
                             font='Arial 20 bold',
                             height=2,
                             width=10,
                             command=lambda:health_page("rain_with_sun_button")
                             )
    rain_with_sun_button.place(relx=0.5, rely=0.57, anchor='center', y=0)
    # Add the button to choose rainy
    rainy_button = tk.Button(text='🌧️',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda:health_page("rainy_button")
                            )
    rainy_button.place(relx=0.5, rely=0.57, anchor='center', y=65)
    # Add the button to choose clouds with lightning
    clouds_with_lightning_button = tk.Button(text='⛈️',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda:health_page("clouds_with_lightning_button")
                            )
    clouds_with_lightning_button.place(relx=0.5, rely=0.57, anchor='center', y=130)
    # Add the button to choose snowy
    snowy_button = tk.Button(text='🌨️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:health_page("snowy_button")
                              )
    snowy_button.place(relx=0.5, rely=0.57, anchor='center', y=195)
    # Add the button to choose heavy snowy
    heavy_snowy_button = tk.Button(text='❄️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:health_page("heavy_snowy_button")
                              )
    heavy_snowy_button.place(relx=0.5, rely=0.57, anchor='center', y=195)


def health_page(weather_button):
    global mood_colour,mood_emoji,weather_selection,health
    # clean all the widgets from the previous page
    clear_widgets(root)
    #add different weather emojis to different weather buttons
    if weather_button=="sunny_button":
        weather_selection = "☀️"
    elif weather_button=="sunny_with_clouds_button":
        weather_selection = "🌤"
    elif weather_button=="cloudy_button":
        weather_selection = "☁️"
    elif weather_button=="rain_with_sun_button":
        weather_selection = "🌦️"
    elif weather_button=="rainy_button":
        weather_selection = "🌧"
    elif weather_button=="sunny_with_clouds_button":
        weather_selection = "🌤"
    elif weather_button=="snowy_button":
        weather_selection = "🌨️"
    elif weather_button=="heavy_snowy_button":
        weather_selection = "❄️"

    # add background image with the selected mood colour in the health page
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(lambda:weather_page(f'{weather_selection}'))
    #place the button to go back to main page from the home_button definition
    home_button()
    # adding the label to show the date of today at the right top corner
    show_today_date()
    #add the question label to ask the health condition of the users
    question_label = tk.Label(root, text='How physically healthy are you?',
                              font='optima 18 bold',
                              bg='light yellow',
                              fg='black',
                              borderwidth=12)
    question_label.place(relx=0.5, anchor='center', y=100)

    # Add the button to choose Excellent
    excellent_button = tk.Button(text='Excellent',
                           font='Arial 20 bold',
                           height=2,
                           width=10,
                           command=lambda:diary_page("excellent_button")
                           )
    excellent_button.place(relx=0.5, rely=0.57, anchor='center', y=-195)
    # Add the button to choose Good
    good_button = tk.Button(text='Good️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:diary_page("good_button")
                              )
    good_button.place(relx=0.5, rely=0.57, anchor='center', y=-130)
    # Add the button to choose So_so
    so_so_button= tk.Button(text='So so',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:diary_page("so_so_button")
                              )
    so_so_button.place(relx=0.5, rely=0.57, anchor='center', y=-65)
    # Add the button to choose rain with sun
    not_well_button = tk.Button(text='Not well',
                             font='Arial 20 bold',
                             height=2,
                             width=10,
                             command=lambda:diary_page("not_well_button")
                             )
    not_well_button.place(relx=0.5, rely=0.57, anchor='center', y=0)
    # Add the button to choose Super_bad️
    super_bad_button = tk.Button(text='Super bad️',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda:diary_page("super_bad_button")
                            )
    super_bad_button.place(relx=0.5, rely=0.57, anchor='center', y=65)




def diary_page(health_button):
    """This ia a definition for the page of entering the diary"""
    global weather_button,health, diary_entry
    # destroy all the button in the colour button page
    clear_widgets(root)

    # add different physical health conditions to different health buttons
    if health_button=="excellent_button":
        health = "Excellent"
    elif health_button=="good_button":
        health = "Good"
    elif health_button=="so_so_button":
        health = "So so"
    elif health_button=="not_well_button":
        health = "Not well"
    elif health_button=="super_bad_button":
        health = "Super bad"

    # add background image with the selected mood colour in the diary_page
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # add the button to go back to previous page from the back_button definition
    back_button(lambda:health_page(f'{health}'))
    #place the button to go back to main page from the home_button definition
    home_button()
    # adding the label to show the date of today at the right top corner
    show_today_date()

    # add the welcome message
    welcome = tk.Label(text="Write down your Moody Diary",
                       font='optima 25 bold',
                       bg='light yellow',
                       borderwidth=3
                       )
    welcome.place(relx=0.5, rely=0.1, anchor='center', y=50)

    #add the label to show the selected mood emoji of the mood_emoji_page on diary_page
    mood_emoji_label=tk.Label(text=f"Your mood: {mood_emoji}",
                        font='optima 20 bold',
                        bg='light yellow',
                        borderwidth=3,
                        )
    mood_emoji_label.place(relx=0.5, rely=0.1, anchor='center', y=100)

    #add the label to show the selected weather label of the weather_page on diary_page
    weather_label=tk.Label(text=f"Weather: {weather_selection}",
                        font='optima 20 bold',
                        bg='light yellow',
                        borderwidth=3,
                        )
    weather_label.place(relx=0.5, rely=0.1, anchor='center', y=140)

    # add the label to show the selected health label of the health_page on diary_page
    health_label = tk.Label(text=f"Health condition: {health}",
                       font='optima 20 bold',
                       bg='light yellow',
                       borderwidth=3,
                       )
    health_label.place(relx=0.5, rely=0.1, anchor='center', y=180)

    # add the diary entry box
    diary_entry=tk.Text(root,height=18, width=45)
    diary_entry.place(relx=0.5, rely=0.5, anchor='center', y=80)
    # add buttons of Save, in which the app will store the data of the above selections with the definition of store_data
    save_button = tk.Button(text='SAVE', font='optima 15 bold', height=1, width=7,command=store_data)
    save_button.place(relx=0.5, rely=0.5, anchor='center', y=220)


def diary_page_return():
    """This is a definition for the page of reading the diary"""
    global weather_button,health, diary_entry
    # destroy all the button in the colour button page
    clear_widgets(root)
    # add background image with the selected mood colour in the diary_page_return
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(view_diary_page(selected_date))
    #place the button to go back to main page from the home_button definition
    home_button()
    # add the welcome question
    welcome = tk.Label(text="Read your Moody Diary ",
                       font='optima 25 bold',
                       bg='light yellow',
                       borderwidth=3
                       )
    welcome.place(relx=0.5, rely=0.1, anchor='center', y=50)

    #add the mood emoji label in the mood_emoji_page
    mood_emoji_label=tk.Label(text=f"Your mood: {mood_emoji}",
                        font='optima 20 bold',
                        bg='light yellow',
                        borderwidth=3,
                        )
    mood_emoji_label.place(relx=0.5, rely=0.1, anchor='center', y=100)

    #add the weather label in the weather_page
    weather_label=tk.Label(text=f"Weather: {weather_selection}",
                        font='optima 20 bold',
                        bg='light yellow',
                        borderwidth=3,
                        )
    weather_label.place(relx=0.5, rely=0.1, anchor='center', y=140)

    # add the weather label in the health_page
    health_label = tk.Label(text=f"Health condition: {health}",
                       font='optima 20 bold',
                       bg='light yellow',
                       borderwidth=3,
                       )
    health_label.place(relx=0.5, rely=0.1, anchor='center', y=180)

    # add the diary entry box
    diary_entry=tk.Text(root,height=18, width=45)
    diary_entry.place(relx=0.5, rely=0.5, anchor='center', y=80)
    # add buttons to view your recipe
    view_recipe_button = tk.Button(text='View your recipe', font='optima 15 bold', height=1, width=20,command=recipe_return)
    view_recipe_button.place(relx=0.5, rely=0.5, anchor='center', y=220)



def recipe():
    """This is a definition of a page for generating the recipes"""
    global title_label,back_button,img,recipe_choice
    # clean all the widgets from the previous page
    clear_widgets(root)

    #adding the random recipy based on the colours that the users selected
    recipe_choice = random.choice(options)

    #reading the data from the user_mood_data.csv file
    diary_data = pd.read_csv("data/user_mood_data.csv")
    selected_date = str(cal.get_date())
    #print(recipe_choice)
    diary_data["recipe_choice"] = recipe_choice
    #read the recipe choice of the date selected by the current user
    diary_data["recipe_choice"].loc[(diary_data["username"] == current_user) & (diary_data["created_at"] == selected_date)] = recipe_choice
    #print(diary_data)
    #print(recipe_choice)
    diary_data.to_csv("data/user_mood_data.csv", index=False)
    add_image(root, f'images/{recipe_choice}',screen_width,screen_height)
    # create and place a home page button
    calender_page = tk.Button(root,
                         text="🗓️",
                         command=calendar_page_return)
    calender_page.place(relx=0.5, anchor='center', y=620)

def recipe_return():
    """This is a page for generating the recipes"""
    global title_label,back_button,img, recipe_choice
    # clean all the widgets from the previous page
    clear_widgets(root)
    #adding the random recipy based on the colours that the users selected
    diary_data = pd.read_csv("data/user_mood_data.csv")
    selected_date = str(cal.get_date())
    #diary_data["recipe_choice"] = recipe_choice
    recipe_choice = diary_data.loc[(diary_data["username"] == current_user) & (diary_data["created_at"] == selected_date)].tail(1)
    #select the recipe choice in the dataframe
    recipe_choice=recipe_choice["recipe_choice"].values[0]
    print(recipe_choice)
    #add the image of the previously generated recipe
    add_image(root, f'images/{recipe_choice}',screen_width,screen_height)
    # place the button to go back to previous page from the back_button definition
    #back_button(view_diary_page(selected_date))
    home_button()

def store_data():
    """This is a definition for storing the data of the diary choices"""
    #when the user haven't entered the diary, it will show the error message
    if not diary_entry.get("1.0",'end-1c'):
        error_message = tk.Label(text="You have not entered your diary",
                                 bg="red",
                                 fg="white"
                                )
        error_message.place(relx=0.5, anchor='center', y=210)

    #if the user have entered the diary, it will store the date
    else:
        user_mood_data = {"username": current_user,
                            "mood_colour": mood_colour,
                            "mood_emoji": mood_emoji,
                            "weather": weather_selection,
                            "health": health,
                            #get the input from the Tkinter Text Widget: (https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-widget)
                            "diary": diary_entry.get("1.0", 'end-1c'),
                            "created_at":datetime.now().date()
                            }
        # converting the dictionary to a data frame
        user_data = pd.DataFrame([user_mood_data])
        user_data.to_csv("data/user_mood_data.csv", index=False, header=False, mode='a')
        # add buttons of getting a recipe after saving the diary data
        recipe_button = tk.Button(text='Now you have your recipe', font='optima 15 bold', height=1, width=20,command=recipe)
        recipe_button.place(relx=0.5, rely=0.5, anchor='center', y=260)

def view_diary_page(selected_date):
    """This is a definition of the page for viewing the diary"""
    # clean all the widgets from the previous page
    clear_widgets(root)
    #reading the dataframe to get the values of each variables
    diary_data=pd.read_csv("data/user_mood_data.csv")
    diary_data=diary_data.loc[diary_data["username"]==current_user]
    diary_dates=diary_data['created_at'].to_list()

    #if there is diary entry at the selected date, it will fetch the data of the that day
    if selected_date in diary_dates:
        global mood_colour,mood_emoji,health,weather,diary
        current_entry=diary_data.loc[diary_data["created_at"]==selected_date].tail(1)
        mood_colour=current_entry["mood_colour"].values[0]
        mood_emoji = current_entry["mood_emoji"].values[0]
        health = current_entry["health"].values[0]
        weather = current_entry["weather"].values[0]
        diary = current_entry["diary"].values[0]

        # add background image with the selected mood colour in the view_diary_page
        add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
        # place the button to go back to previous page from the back_button definition
        back_button(calendar_page_return)
        # place the button to go back to main page from the home_button definition
        home_button()

        diary_data=pd.read_csv("data/user_mood_data.csv")
        print(diary_data)

        # add the welcome question
        welcome = tk.Label(text="Read your Moody Foody Diary",
                           font='optima 25 bold',
                           bg='light yellow',
                           #bg=f'{mood_colour}'
                           borderwidth=3,
                           )
        welcome.place(relx=0.5, rely=0.1, anchor='center', y=50)

        #add the mood emoji in the mood_emoji_page
        date_label=tk.Label(text='Date: ' + selected_date,
                            font='optima 20 bold',
                            bg='light yellow',
                            borderwidth=3,
                            #command=enter_user_data
                            )
        date_label.place(relx=0.5, rely=0.1, anchor='center', y=100)

        #get the data from the current user in the dataframe
        diary_data=diary_data.loc[diary_data["username"]==current_user]
        #
        list_index=[]
        for i in diary_data.index:
            diary_entry=False
            if selected_date== str(diary_data.loc[i,"created_at"]):
                diary_entry=True
                list_index.append(i)
            if diary_entry==True:
                i=list_index[-1]
                print(i)
                #add the mood emoji selected in the mood_emoji_page to the view_diary_page
                mood_emoji_label=tk.Label(text='Your mood: ' + diary_data.loc[i,"mood_emoji"],
                                    font='optima 20 bold',
                                    bg='light yellow',
                                    borderwidth=3,
                                    )
                mood_emoji_label.place(relx=0.5, rely=0.1, anchor='center', y=150)

                #add the weather selected in the weather_page to the view_diary_page
                weather_label=tk.Label(text='Weather: ' + diary_data.loc[i,"weather"],
                                    font='optima 20 bold',
                                    bg='light yellow',
                                    borderwidth=3,
                                    )
                weather_label.place(relx=0.5, rely=0.1, anchor='center', y=190)

                # add the weather selected in the health_page  to the view_diary_page
                health_label = tk.Label(text='Health: ' + diary_data.loc[i,"health"],
                                   font='optima 20 bold',
                                   bg='light yellow',
                                   borderwidth=3,
                                   )
                health_label.place(relx=0.5, rely=0.1, anchor='center', y=230)

                #add the diary entry box
                diary_box = tk.Canvas(root, width=300, height=230, bg="white")
                diary_box.place(relx=0.5, rely=0.5, anchor='center', y=110)
                diary_label = tk.Label(text=  diary_data.loc[i, "diary"],
                                        font='optima 10 bold',
                                        bg="white"
                                        )
                diary_label.place(x=27, y=325)

                # add buttons for viewing the Foody Recipe
                foody_recipe_button = tk.Button(text='View your Foody Recipe', font='optima 15 bold', height=1, width=20,
                                               command=recipe_return)
                foody_recipe_button.place(relx=0.5, rely=0.5, anchor='center', y=250)

    #if the there is no diary entry, then it will go to the entry diary page with the message of no diary entry
    else:
        # add the background image of the smiling faces with different colours in the page where there is no diary entry and selected mood colour
        add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
        # place the button to go back to main page from the home_button definition
        home_button()
        # add a title of "Moody Foody Diary"
        title_label = tk.Label(root,
                               text='---------Moody Foody Diary---------',
                               font='optima 25 bold',
                               bg='light yellow',
                               borderwidth=20)
        title_label.place(relx=0.5, anchor='center', y=100)
        #add the message for showing no diary entry
        no_diary_message=tk.Label(text="You haven't created your diary that day",
                                  font=20,
                                  bg="red",
                                  fg="white")
        no_diary_message.place(relx=0.5, rely=0.5, anchor='center', y=100)


#The app will start with the home page
home_page()

#execute the code
root.mainloop()