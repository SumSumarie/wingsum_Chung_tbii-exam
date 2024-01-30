import tkinter as tk
from datetime import datetime
from datetime import date
from tkcalendar import Calendar
from tkcalendar import DateEntry
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


def enter_user_data():
    """This is the definition of storing data of the users"""
    #create a timestamp
    current_timestamp=datetime.now()
    #call the birthday
    birthday = cal.get_date()
    # get the list of user ids
    user_ids = list(pd.read_csv("data/user_data.csv").username)
    #warining message box will be shown when the username or the magic key were taken
    if username.get() in user_ids:
        tk.messagebox.showwarning("warning", "This username is taken")
    else:
        user_data = {
            "username":username.get(),
            "birthday": birthday,
            "create_at":current_timestamp
        }
        # converting the dictionary to a data frame
        user_data = pd.DataFrame([user_data])
        user_data.to_csv("data/user_data.csv", index=False, header=False, mode='a')

def home_page():
    """This the home page"""
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
                            command=return_user_page)
    return_user_button.place(relx = 0.5,anchor = 'center',y=550)

def new_user_page():
    global username, cal
    #enter_user_data()
    # clean all the widgets from the previous page
    clear_widgets(root)
    # call the birthday
    #birthday = cal.get_date()
    #add the image in the main page
    add_image(root, 'images/beginning_smile.png',screen_width,screen_height)
    #place the button to go back to main page from the home_button definition
    home_button()
    # add a message saying 'Open your Moody Foody Diary'
    title_label = tk.Label(root,
                           text='---------Moody Foody Diary---------',
                           font='optima 25 bold',
                           bg='light yellow',
                           borderwidth=20)
    title_label.place(relx = 0.5,anchor = 'center',y=100)
    # add a message asking the user for their user name
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
    # add a calendar behind the label birthday
    cal = DateEntry(root,
                    font="Arial 20",
                    selectmode="day",
                    style='my.DateEntry'
                    )
    cal.place(x=130, y=350)
    #add the button to click to create a Moody Foody Diary
    create_diary_button=tk.Button(root,
                            text="Create your Moody Foody Diary",
                            font='optima 20 bold',
                            command=calendar_page_new)
    create_diary_button.place(relx = 0.5,anchor = 'center',y=500)


def return_user_page():
    global username, magic_key
    # clean all the widgets from the previous page
    clear_widgets(root)
    #add the image in the main page
    add_image(root, 'images/beginning_smile.png',screen_width,screen_height)
    #place the button to go back to main page from the home_button definition
    home_button()
    # add a message saying 'Open your Moody Foody Diary'
    title_label = tk.Label(root,
                           text='This is your Moody Foody Diary',
                           font='optima 20 bold',
                           bg='light yellow',
                           borderwidth=25)
    title_label.place(relx = 0.5,anchor = 'center',y=150)
    # add a message asking the user for their user name
    username_label = tk.Label(root, text='Username', font='optima 20 bold', borderwidth=3)
    username_label.place(x=20,y=300)
    #add a user-name entry box
    username=tk.StringVar()
    username_entry=tk.Entry(root,
                        textvar=username,
                        font='optima 20 bold',
                        width=15)
    username_entry.place(x=130,y=300)
    #add the button to click to enter your diary
    enter_diary_button=tk.Button(root,
                            text="Enter your diary",
                            font='optima 20 bold',
                            command=calendar_page_return)
    enter_diary_button.place(relx = 0.5,anchor = 'center',y=500)

def calendar_page_new():
    """This is a calendar page after the main page(log in)"""
    # clean all the widgets from the previous page
    clear_widgets(root)
    # add the image in the homepage
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
    #add a welcome label
    welcome_label=tk.Label(root,
                           text=(f"{username.get()}"),
                           font=("Optima", 25,"bold"),
                           bg='light yellow'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=100)
    #add a welcome label
    welcome_label=tk.Label(root,
                           text=("Welcome to"),
                           font=("Optima", 20,"bold"),
                           bg='light yellow'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=140)
    #add a welcome label
    welcome_label=tk.Label(root,
                           text=("your own Moody Foody Diary"),
                           font=("Optima", 25,"bold"),
                           bg='light yellow'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=180)
    current_date = date.today()
    #add a label for today's date
    today_date_label=tk.Label(root,
                           text=(f"Date of today: {current_date}"),
                           font=("Optima", 25,"bold"),
                           bg='light yellow'
                            )
    today_date_label.place(relx = 0.5,anchor = 'center',y=250)
    # store the birthday
    #add a label for birthday
    birthday_date_label=tk.Label(root,
                                 text=("birthday"),
                           #text=(f"Your birthday is {birthday}"),
                           font=("Optima", 25,"bold"),
                           bg='light yellow'
                            )
    birthday_date_label.place(relx = 0.5,anchor = 'center',y=300)



def calendar_page_return():
    """This is a calendar page after the main page(log in)"""
    # clean all the widgets from the previous page
    clear_widgets(root)

    # add the image in the homepage
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(home_page)
    #place the button to go back to main page from the home_button definition
    home_button()
    # add the view_diary button
    view_diary = tk.Button(root,
                           font=("Optima", 25, "bold"),
                           text="View your diaries",
                           command=view_diary_page
                           )
    view_diary.place(relx=0.5, anchor='center', y=450)
    #add a create_diary button for entering the diary information
    create_diary = tk.Button(root,
                         text="Create a new diary",
                         font=("Optima", 25, "bold"),
                         command=mood_colour_page
                         )
    create_diary.place(relx=0.5, anchor='center', y=520)
    #add a welcome label
    welcome_label=tk.Label(root,
                           text=(f"{username.get()}"),
                           font=("Optima", 25,"bold"),
                           bg='light yellow'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=100)
    #add a welcome label
    welcome_label=tk.Label(root,
                           text=("Welcome to"),
                           font=("Optima", 20,"bold"),
                           bg='light yellow'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=140)
    #add a welcome label
    welcome_label=tk.Label(root,
                           text=("your own Moody Foody Diary"),
                           font=("Optima", 25,"bold"),
                           bg='light yellow'
                            )
    welcome_label.place(relx = 0.5,anchor = 'center',y=180)
    #get the date of today
    current_date = date.today()
    #add a calendar to choose the date of today
    cal = Calendar(root,
                   selectmode='day',
                   year=current_date.year,
                   month=current_date.month,
                   day=current_date.day)
    cal.place(relx = 0.5,anchor = 'center',y=320)


def mood_colour_page():
    """This is a page for selecting the mood colour"""
    # clean all the widgets from the previous page
    clear_widgets(root)
    # add the image in the homepage
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(calendar_page_new)
    #place the button to go back to main page from the home_button definition
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
    # adding image on each colour page
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(mood_colour_page)
    #place the button to go back to main page from the home_button definition
    home_button()
    question_label = tk.Label(root, text='What is your mood today?',
                              font='optima 18 bold',
                              bg='light yellow',
                              fg='black',
                              borderwidth=12)
    # where would you like to place this button
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
    """This is a page asking the weather of today"""
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

    # add the image in the homepage
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(lambda:mood_emoji_page(f'{mood_emoji}'))
    #place the button to go back to main page from the home_button definition
    home_button()

    #add a message to ask the weather of today
    question_label = tk.Label(root, text='What is the weather today?',
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

    # add the image in the homepage
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(lambda:weather_page(f'{weather_selection}'))
    #place the button to go back to main page from the home_button definition
    home_button()
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

def store_data():
    # store the emoji data
    user_mood_data = {"username": username.get(),
                        "mood_colour": mood_colour,
                        "mood_emoji": mood_emoji,
                        "weather": weather_selection,
                        "health": health,
                        "diary":diary_entry.get("1.0",'end-1c')
                        }
    # converting the dictionary to a data frame
    user_data = pd.DataFrame([user_mood_data])
    user_data.to_csv("data/user_mood_data.csv", index=False, header=False, mode='a')
    # add buttons of getting a recipe
    recipe_button = tk.Button(text='Now you have your recipe', font='optima 15 bold', height=1, width=20,command=recipe)
    recipe_button.place(relx=0.5, rely=0.5, anchor='center', y=260)

"""
def show_data():
 ""'This is a page to read the data""'
    users_data=pd.read_csv("data/user_mood_data.csv")
    date=list(users_data.date)

    for d in date:
        tk.Label(root,
                 text=d)
        entry =list(users_data[users_data.date]==d].diary_entry)[5]
        tk.Label(root,text=entry)
"""

def diary_page(health_button):
    global weather_button,health, diary_entry
    """This ia a page for entering the diary"""
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

    # add image on each colour page
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(lambda:health_page(f'{health}'))
    #place the button to go back to main page from the home_button definition
    home_button()

    # add the welcome question
    welcome = tk.Label(text=f"Write down your Moody Diary ",
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
    # add buttons of Enter
    save_button = tk.Button(text='SAVE', font='optima 15 bold', height=1, width=7,command=store_data)
    save_button.place(relx=0.5, rely=0.5, anchor='center', y=220)


def diary_page_return(health_button):
    global weather_button,health, diary_entry
    """This ia a page for entering the diary"""
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

    # add image on each colour page
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(view_diary_page)
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
    # add buttons of Enter
    view_recipe_button = tk.Button(text='View your recipe', font='optima 15 bold', height=1, width=20,command=recipe_return)
    view_recipe_button.place(relx=0.5, rely=0.5, anchor='center', y=220)



def recipe():
    """This is a page for generating the recipes"""
    global title_label,back_button,img
    # clean all the widgets from the previous page
    clear_widgets(root)
    #adding the random recipy based on the colours that the users selected
    add_image(root, f'images/{random.choice(options)}',screen_width,screen_height)
    # create and place a home page button
    calender_page = tk.Button(root,
                         text="🗓️",
                         command=calendar_page_return)
    calender_page.place(relx=0.5, anchor='center', y=620)

def recipe_return():
    """This is a page for generating the recipes"""
    global title_label,back_button,img
    # clean all the widgets from the previous page
    clear_widgets(root)
    #adding the random recipy based on the colours that the users selected
    add_image(root, f'images/{random.choice(options)}',screen_width,screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(view_diary_page)

def view_diary_page():
    """This is a page for viewing the diary"""
    # clean all the widgets from the previous page
    clear_widgets(root)
    # add image on each colour page
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(calendar_page_return)
    # place the button to go back to main page from the home_button definition
    home_button()

    # add the welcome question
    welcome = tk.Label(text="Read your Moody Foody Diary",
                       font='optima 25 bold',
                       bg='light yellow',
                       #bg=f'{mood_colour}'
                       borderwidth=3,
                       )
    welcome.place(relx=0.5, rely=0.1, anchor='center', y=50)

    #add the mood emoji in the mood_emoji_page
    date_label=tk.Label(text=f'Date: {date.today()}',
                        font='optima 20 bold',
                        bg='light yellow',
                        borderwidth=3,
                        #command=enter_user_data
                        )
    date_label.place(relx=0.5, rely=0.1, anchor='center', y=100)

    #add the mood emoji in the mood_emoji_page
    mood_emoji_label=tk.Label(text=f'Your mood: {mood_emoji}',
                        font='optima 20 bold',
                        bg='light yellow',
                        borderwidth=3,
                        )
    mood_emoji_label.place(relx=0.5, rely=0.1, anchor='center', y=150)

    #add the weather in the weather_page
    weather_label=tk.Label(text=f'Weather: {weather_selection}',
                        font='optima 20 bold',
                        bg='light yellow',
                        borderwidth=3,
                        )
    weather_label.place(relx=0.5, rely=0.1, anchor='center', y=190)

    # add the weather in the health_page
    health_label = tk.Label(text=f'Health condition: {health}',
                       font='optima 20 bold',
                       bg='light yellow',
                       borderwidth=3,
                       )
    health_label.place(relx=0.5, rely=0.1, anchor='center', y=230)

    #add the Moody Diary button
    moody_diary=tk.Button(text='Moody Diary',
                          font='optima 20 bold',
                          height=2,
                          width=10,
                          command=lambda:diary_page_return(f"weather_selection")
                          )
    moody_diary.place(relx=0.5, rely=0.5, anchor='center', y=50)

    #add the Foody Recipe button
    foody_recipe = tk.Button(text='Foody Recipe',
                             font='optima 20 bold',
                             height=2,
                             width=10,
                             command=recipe_return
                             )
    foody_recipe.place(relx=0.5, rely=0.5, anchor='center', y=150)


#start with the home page
home_page()

#execute the code
root.mainloop()