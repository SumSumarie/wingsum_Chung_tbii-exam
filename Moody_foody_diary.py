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
    # create a home page button
    homepage = tk.Button(root,
                         text="🏠",
                         command=home_page)
    # place the homepage button
    homepage.place(relx=0.5, anchor='center', y=620)

def back_button(page):
    """This is a definition of the button for going back to the previous page"""
    #create a Back button
    back=tk.Button(root,
                    text="⬅",
                    command=page
                   )
    #place the Back button
    back.place(relx = 0.2,anchor = 'ne',y=15)

def enter_user_data():
    """this is the definition of storing data of the users"""
    #create a timestamp
    current_timestamp=datetime.now()
    # get the list of user ids
    user_ids = list(pd.read_csv("data/user_data.csv").username)
    #warining message box will be shown when the username or the magic key were taken
    if username.get() in user_ids:
        tk.messagebox.showwarning("warning", "This username is taken")
    elif magic_key.get() in user_ids:
        tk.messagebox.showwarning("warning", "This magic key is taken")
    else:
        user_data = {
            "username":username.get(),
            "magic_key":magic_key.get(),
            #"birthday": birthday.get(),
            "create_at":current_timestamp
        }
        # converting the dictionary to a data frame
        user_data = pd.DataFrame([user_data])
        user_data.to_csv("data/user_data.csv", index=False, header=False, mode='a')
        # clean all the widgets from the previous page
        clear_widgets(root)
        #thank-you button for submitting the username
        thank_button=tk.Label(root,
                 text=(f"Thank you for submitting your data {username.get()}")
                 )
        thank_button.place(x=150,y=200)

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
    #add the image in the main page
    add_image(root, 'images/beginning_smile.png',screen_width,screen_height)
    # print a message saying 'Open your Moody Foody Diary'
    title_label = tk.Label(root,
                           text='This is your Moody Foody Diary',
                           font='optima 20 bold',
                           bg='light yellow',
                           borderwidth=25)
    # place this title_label button
    title_label.place(relx = 0.5,anchor = 'center',y=150)
    # print a message asking the user for their user name
    username_label = tk.Label(root, text='Username', font='optima 20 bold', borderwidth=3)
    # place this username label
    username_label.place(x=20,y=250)
    #create a user-name entry box
    username=tk.StringVar()
    username_entry=tk.Entry(root,
                        textvar=username,
                        font='optima 20 bold',
                        width=15)
    # place the user-name entry box
    username_entry.place(x=130,y=250)
    # print a message asking the user for their magic key to open the diary
    magic_key_label = tk.Label(root, text='Magic Key', font='optima 20 bold', borderwidth=3)
    # where would you like to place this label
    magic_key_label.place(x=20,y=300)
    # create a magic-key entry box
    magic_key=tk.StringVar()
    magic_key_entry=tk.Entry(root,
                        textvar=magic_key,
                        font='optima 20 bold',
                        width=15)
    magic_key_entry.place(x=130,y=300)
    # print a message asking the user for their birthday
    birthday_label = tk.Label(root, text='Birthday', font='optima 20 bold', borderwidth=3)
    # where would you like to place this button
    birthday_label.place(x=20,y=350)
    #create a calendar behind the label birthday
    cal = DateEntry(root,
                    width=18,
                    height=55,
                    selectmode="day")
    # place the calendar
    cal.place(x=130, y=350)
    #the calendar can get the date the users chose
    birthday= cal.get_date()
    #create the button to click to create a diary
    create_diary_button=tk.Button(root,
                            text="create your diary",
                            font='optima 20 bold',
                            command=calendar_page)
    #place the button
    create_diary_button.place(relx = 0.5,anchor = 'center',y=500)
    """
    #create the button to click to create_returning_user_page
    return_user_button = tk.Button(root,
                              text="Already have your diary?",
                              font='optima 15 bold',
                              command=create_returning_user_page)
    return_user_button.place(relx=0.5, anchor='center', y=600)
    """

def calendar_page():
    """This is a calendar page after the main page(log in)"""
    # store the data
    enter_user_data()
    # clean all the widgets from the previous page
    clear_widgets(root)
    # add the image in the homepage
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(home_page)
    #place the button to go back to main page from the home_button definition
    home_button()
    # create the view_diary button
    view_diary = tk.Button(root,
                           font=("Optima", 25, "bold"),
                           text="View your diaries",
                           command=view_diary_page
                           )
    # place the view_diary button
    view_diary.place(relx=0.5, anchor='center', y=400)
    #create a create_diary button for entering the diary information
    create_diary = tk.Button(root,
                         text="Create a new diary",
                         font=("Optima", 25, "bold"),
                         command=mood_colour_page
                         )
    #place the create_diary button
    create_diary.place(relx=0.5, anchor='center', y=500)
    #create a welcome label
    welcome_label=tk.Label(root,
                           text=(f"{username.get()}, "
                                 "welcome to your own Moody Foody Diary"),
                           font=("Optima", 15,"bold")
                            )
    #place the welcome label
    welcome_label.place(relx = 0.5,anchor = 'center',y=100)

    #get the date of today
    current_date = date.today()
    #add a calendar to choose the date of today
    cal = Calendar(root,
                   selectmode='day',
                   year=current_date.year,
                   month=current_date.month,
                   day=current_date.day)
    #place the calendar
    cal.place(relx = 0.5,anchor = 'center',y=270)

def mood_colour_page():
    """This is a page for selecting the mood colour"""
    # clean all the widgets from the previous page
    clear_widgets(root)
    # add the image in the homepage
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(calendar_page)
    #place the button to go back to main page from the home_button definition
    home_button()
    #print a message asking for the colour of the mood today
    question_label = tk.Label(root, text='What is the colour of your mood today?',
                              font='optima 18 bold',
                              bg='light yellow',
                              fg='black',
                              borderwidth=12)
    # place the message
    question_label.place(relx=0.5, anchor='center', y=100)
    # The button to choose red as the colour of the mood today
    red_button = tk.Button(text=':)',
                           fg='red',
                           font='Arial 20 bold',
                           height=2,
                           width=10,
                           command=lambda: mood_emoji_page("red_button")
                           )
    # place the red button
    red_button.place(relx=0.5, rely=0.57, anchor='center', y=-195)
     # The button to choose orange as the colour of the mood today
    orange_button = tk.Button(text=':)',
                              fg='orange',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda: mood_emoji_page("orange_button")
                              )
    # place the orange button
    orange_button.place(relx=0.5, rely=0.57, anchor='center', y=-130)
    # The button to choose yellow as the colour of the mood today
    yellow_button = tk.Button(text=':)',
                              fg='yellow',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda: mood_emoji_page("yellow_button")
                              )
    # place the yellow button
    yellow_button.place(relx=0.5, rely=0.57, anchor='center', y=-65)
    # The button to choose green as the colour of the mood today
    green_button = tk.Button(text=':)',
                             fg='green',
                             font='Arial 20 bold',
                             height=2,
                             width=10,
                             command=lambda: mood_emoji_page("green_button")
                             )
    # place the green button
    green_button.place(relx=0.5, rely=0.57, anchor='center', y=0)
    # The button to choose Indigo as the colour of the mood today
    cyan_button = tk.Button(text=':)',
                            fg='cyan',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda: mood_emoji_page("cyan_button")
                            )
    # place the cyan button
    cyan_button.place(relx=0.5, rely=0.57, anchor='center', y=65)
    # The button to choose blue as the colour of the mood today
    blue_button = tk.Button(text=':)',
                            fg='blue',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda: mood_emoji_page("blue_button")
                            )
    # place the blue button
    blue_button.place(relx=0.5, rely=0.57, anchor='center', y=130)
    # The button to choose purple as the colour of the mood today
    purple_button = tk.Button(text=':)',
                              fg='purple',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda: mood_emoji_page("purple_button")
                              )
    # place the purple button
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

    # adding 😀 emoji
    grinning_emoji = tk.Button(root,
                            text="😀",
                            font=("Optima", 25, "bold"),
                            height=1,
                            width=1,
                            command=lambda:weather_page("grinning_emoji")
                            )

    grinning_emoji.place(relx=0.2, rely=0.2, anchor='center', y=50)
    # adding 😁 emoji
    beaming_emoji = tk.Button(root,
                          text="😁",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page("beaming_emoji")
                          )

    beaming_emoji.place(relx=0.2, rely=0.2, anchor='center', y=100)
    # adding ☺️ emoji
    smiling_emoji = tk.Button(root,
                               text="☺️",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page("smiling_emoji")
                               )

    smiling_emoji.place(relx=0.2, rely=0.2, anchor='center', y=150)
    # adding 😍 emoji
    heart_eyes_emoji = tk.Button(root,
                                text="😍",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("heart_eyes_emoji")
                                )

    heart_eyes_emoji.place(relx=0.2, rely=0.2, anchor='center', y=200)
    # adding 🥰 emoji
    heart_emoji = tk.Button(root,
                                text="🥰",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("heart_emoji")
                                )

    heart_emoji.place(relx=0.2, rely=0.2, anchor='center', y=250)

    # adding 😉 emoji
    winking_emoji = tk.Button(root,
                                text="😉",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("winking_emoji")
                                )

    winking_emoji.place(relx=0.2, rely=0.2, anchor='center', y=300)

    # adding 😋 emoji
    face_savoring_emoji = tk.Button(root,
                                text="😋",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("face_savoring_emoji")
                                )

    face_savoring_emoji.place(relx=0.2, rely=0.2, anchor='center', y=350)

    # adding 😎 emoji
    sunglasses_emoji = tk.Button(root,
                            text="😎",
                            font=("Optima", 25, "bold"),
                            height=1,
                            width=1,
                            command=lambda:weather_page("sunglasses_emoji")
                            )

    sunglasses_emoji.place(relx=0.4, rely=0.2, anchor='center', y=50)
    # adding 🤩 emoji
    star_struck_emoji = tk.Button(root,
                          text="🤩",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page("star_struck_emoji")
                          )

    star_struck_emoji.place(relx=0.4, rely=0.2, anchor='center', y=100)
    # adding 🥳️ emoji
    partying_emoji = tk.Button(root,
                               text="🥳",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page("partying_emoji")
                               )

    partying_emoji.place(relx=0.4, rely=0.2, anchor='center', y=150)
    # adding 🤪 emoji
    zany_face_emoji = tk.Button(root,
                                text="🤪",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("zany_face_emoji")
                                )

    zany_face_emoji.place(relx=0.4, rely=0.2, anchor='center', y=200)
    # adding 😝 emoji
    tongue_emoji = tk.Button(root,
                                text="😝",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("tongue_emoji")
                                )

    tongue_emoji.place(relx=0.4, rely=0.2, anchor='center', y=250)

    # adding 😂 emoji
    tears_of_joy_emoji = tk.Button(root,
                                text="😂",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("tears_of_joy_emoji")
                                )

    tears_of_joy_emoji.place(relx=0.4, rely=0.2, anchor='center', y=300)

    # adding 🥲 emoji
    single_tear_emoji = tk.Button(root,
                                text="🥲",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("single_tear_emoji")
                                )

    single_tear_emoji.place(relx=0.4, rely=0.2, anchor='center', y=350)

    # adding 😒 emoji
    unamused_emoji = tk.Button(root,
                            text="😒",
                            font=("Optima", 25, "bold"),
                            height=1,
                            width=1,
                            command=lambda:weather_page("unamused_emoji")
                            )

    unamused_emoji.place(relx=0.6, rely=0.2, anchor='center', y=50)
    # adding 😖 emoji
    confounded_emoji = tk.Button(root,
                          text="😖",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page("confounded_emoji")
                          )

    confounded_emoji.place(relx=0.6, rely=0.2, anchor='center', y=100)
    # adding 😫 emoji
    tired_emoji = tk.Button(root,
                               text="😫",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page("tired_emoji")
                               )

    tired_emoji.place(relx=0.6, rely=0.2, anchor='center', y=150)
    # adding 🥺 emoji
    pleading_emoji = tk.Button(root,
                                text="🥺",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("pleading_emoji")
                                )

    pleading_emoji.place(relx=0.6, rely=0.2, anchor='center', y=200)
    # adding 😤 emoji
    steam_nose_emoji = tk.Button(root,
                                text="😤",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("steam_nose_emoji")
                                )

    steam_nose_emoji.place(relx=0.6, rely=0.2, anchor='center', y=250)

    # adding 😭 emoji
    crying_emoji = tk.Button(root,
                                text="😭",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("crying_emoji")
                                )

    crying_emoji.place(relx=0.6, rely=0.2, anchor='center', y=300)

    # adding 😡 emoji
    enraged_emoji = tk.Button(root,
                                text="😡",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("enraged_emoji")
                                )

    enraged_emoji.place(relx=0.6, rely=0.2, anchor='center', y=350)

    # adding 🤬 emoji
    swear_emoji = tk.Button(root,
                            text="🤬",
                            font=("Optima", 25, "bold"),
                            height=1,
                            width=1,
                            command=lambda:weather_page("swear_emoji")
                            )

    swear_emoji.place(relx=0.8, rely=0.2, anchor='center', y=50)
    # adding 🤯 emoji
    exploding_head_emoji = tk.Button(root,
                          text="🤯",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page("exploding_head_emoji")
                          )

    exploding_head_emoji.place(relx=0.8, rely=0.2, anchor='center', y=100)
    # adding 😳 emoji
    flushed_face_emoji = tk.Button(root,
                               text="😳",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page("flushed_face_emoji")
                               )

    flushed_face_emoji.place(relx=0.8, rely=0.2, anchor='center', y=150)
    # adding 😱 emoji
    fear_emoji = tk.Button(root,
                                text="😱",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("fear_emoji")
                                )

    fear_emoji.place(relx=0.8, rely=0.2, anchor='center', y=200)
    # adding 😰 emoji
    anxious_emoji = tk.Button(root,
                                text="😰",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("anxious_emoji")
                                )

    anxious_emoji.place(relx=0.8, rely=0.2, anchor='center', y=250)

    # adding 😵‍💫 emoji
    dizziness_emoji = tk.Button(root,
                                text="😵‍💫",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page("dizziness_emoji")
                                )

    dizziness_emoji.place(relx=0.8, rely=0.2, anchor='center', y=300)

    # adding 😴 emoji
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
    back_button(lambda:mood_emoji_page(mood_colour_button))
    #place the button to go back to main page from the home_button definition
    home_button()
    #print a message to ask the weather of today
    question_label = tk.Label(root, text='What is the weather today?',
                              font='optima 18 bold',
                              bg='light yellow',
                              fg='black',
                              borderwidth=12)
    # where would you like to place this button
    question_label.place(relx=0.5, anchor='center', y=100)

    # The button to choose sunny
    sunny_button = tk.Button(text='☀️',
                           font='Arial 20 bold',
                           height=2,
                           width=10,
                           command=lambda:health_page("sunny_button")
                           )
    sunny_button.place(relx=0.5, rely=0.57, anchor='center', y=-195)
    # The button to choose sunny with clouds
    sunny_with_clouds_button = tk.Button(text='🌤️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:health_page("sunny_with_clouds_button")
                              )
    sunny_with_clouds_button.place(relx=0.5, rely=0.57, anchor='center', y=-130)
    # The button to choose cloudy
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
    # The button to choose rainy
    rainy_button = tk.Button(text='🌧️',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda:health_page("rainy_button")
                            )
    rainy_button.place(relx=0.5, rely=0.57, anchor='center', y=65)
    # The button to choose clouds with lightning
    clouds_with_lightning_button = tk.Button(text='⛈️',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda:health_page("clouds_with_lightning_button")
                            )
    clouds_with_lightning_button.place(relx=0.5, rely=0.57, anchor='center', y=130)
    # The button to choose snowy
    snowy_button = tk.Button(text='🌨️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:health_page("snowy_button")
                              )
    snowy_button.place(relx=0.5, rely=0.57, anchor='center', y=195)

    # The button to choose heavy snowy
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
    back_button(weather_page)
    #place the button to go back to main page from the home_button definition
    home_button()
    question_label = tk.Label(root, text='How physically healthy are you?',
                              font='optima 18 bold',
                              bg='light yellow',
                              fg='black',
                              borderwidth=12)
    # where would you like to place this button
    question_label.place(relx=0.5, anchor='center', y=100)

    # The button to choose Excellent
    excellent_button = tk.Button(text='Excellent',
                           font='Arial 20 bold',
                           height=2,
                           width=10,
                           command=lambda:diary_page("excellent_button")
                           )
    excellent_button.place(relx=0.5, rely=0.57, anchor='center', y=-195)
    # The button to choose Good
    good_button = tk.Button(text='Good️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:diary_page("good_button")
                              )
    good_button.place(relx=0.5, rely=0.57, anchor='center', y=-130)
    # The button to choose So_so
    so_so_button= tk.Button(text='So so',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:diary_page("so_so_button")
                              )
    so_so_button.place(relx=0.5, rely=0.57, anchor='center', y=-65)
    # The button to choose rain with sun
    not_well_button = tk.Button(text='Not well',
                             font='Arial 20 bold',
                             height=2,
                             width=10,
                             command=lambda:diary_page("not_well_button")
                             )
    not_well_button.place(relx=0.5, rely=0.57, anchor='center', y=0)
    # The button to choose Super_bad️
    super_bad_button = tk.Button(text='Super bad️',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda:diary_page("super_bad_button")
                            )
    super_bad_button.place(relx=0.5, rely=0.57, anchor='center', y=65)

def diary_page(health_button):
    """This ia a page for entering the diary"""
    # destroy all the button in the colour button page
    clear_widgets(root)
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


    # adding image on each colour page
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(health_page)
    #place the button to go back to main page from the home_button definition
    home_button()
    # the welcome question
    welcome = tk.Label(text=f"Write down your Moody Diary ",
                       font='optima 25 bold',
                       bg='light grey',
                       borderwidth=3, fg=f'{mood_colour}'
                       )
    # place welcome question on a grid
    welcome.place(relx=0.5, rely=0.1, anchor='center', y=50)
    #print the mood emoji in the mood_emoji_page
    mood_emoji_label=tk.Label(text=f"Your mood: {mood_emoji}",
                        font='optima 20 bold',
                        bg='light grey',
                        borderwidth=3,
                        fg=f'{mood_colour}'
                        )
    mood_emoji_label.place(relx=0.5, rely=0.1, anchor='center', y=100)
    #print the weather in the weather_page
    weather_label=tk.Label(text=f"Weather: {weather_selection}",
                        font='optima 20 bold',
                        bg='light grey',
                        borderwidth=3,
                        fg=f'{mood_colour}'
                        )
    weather_label.place(relx=0.5, rely=0.1, anchor='center', y=140)
    # print the weather in the health_page
    health_label = tk.Label(text=f"Health condition: {health}",
                       font='optima 20 bold',
                       bg='light grey',
                       borderwidth=3,
                       fg=f'{mood_colour}'
                       )
    health_label.place(relx=0.5, rely=0.1, anchor='center', y=180)

    #add storyinp as a stringVar
    storyinp = tk.StringVar()
    # add the box for entering a story related to this colour
    story_box = tk.Entry(root, textvar=storyinp, font='arial 20 bold')
    # place story box on a grid
    story_box.place(relx=0.5, rely=0.5, anchor='center', y=80,width=350,height=250)
    # add buttons of Enter
    save_button = tk.Button(text='SAVE', font='optima 20 bold', height=2, width=7,command=recipe)
    save_button.place(relx=0.5, rely=0.5, anchor='center', y=240)
        # store the emoji data
    user_mood_data = {"username": username.get(),
                        "mood_colour": mood_colour,
                        "mood_emoji": mood_emoji,
                        "weather": weather_selection,
                        "health": health,
                        "diary":storyinp.get()
                        }
    # converting the dictionary to a data frame
    user_data = pd.DataFrame([user_mood_data])
    user_data.to_csv("data/user_mood_data.csv", index=False, header=False, mode='a')

def recipe():
    """This is a page for generating the recipes"""
    global title_label,back_button,img
    # clean all the widgets from the previous page
    clear_widgets(root)
    #adding the random recipy based on the colours that the users selected
    add_image(root, f'images/{random.choice(options)}',screen_width,screen_height)
    #adding a close button leading to the daypage of the changed-colour day button, but it doesn't work
    #save_button = tk.Button(text='Save', fg='grey', font='optima 9 bold', height=1,width=3)
    #save_button.place(relx=0.8, anchor='center', y=100)
    # place the button to go back to previous page from the back_button definition
    #back_button(lambda:diary_page(health_button))
    #place the button to go back to main page from the home_button definition
    home_button()

def view_diary_page():
    """This is a page for viewing the diary"""
    # clean all the widgets from the previous page
    clear_widgets(root)
    # adding image on each colour page
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    # place the button to go back to previous page from the back_button definition
    back_button(calendar_page)
    # place the button to go back to main page from the home_button definition
    home_button()
    # the welcome question
    welcome = tk.Label(text="Read your Moody Foody Diary",
                       font='optima 25 bold',
                       bg='light yellow',
                       #bg=f'{mood_colour}'
                       borderwidth=3,
                       #fg=f'{mood_colour}'
                       )
    # place welcome question on a grid
    welcome.place(relx=0.5, rely=0.1, anchor='center', y=50)
    #print the mood emoji in the mood_emoji_page
    date_label=tk.Label(text="f'Date: {date}'",
                        font='optima 20 bold',
                        bg='light yellow',
                        borderwidth=3,
                        #fg=f'{mood_colour}'
                        )
    date_label.place(relx=0.5, rely=0.1, anchor='center', y=100)
    #print the mood emoji in the mood_emoji_page
    mood_emoji_label=tk.Label(text="f'Your mood: {mood_emoji}'",
                        font='optima 20 bold',
                        bg='light grey',
                        borderwidth=3,
                        #fg=f'{mood_colour}'
                        )
    mood_emoji_label.place(relx=0.5, rely=0.1, anchor='center', y=150)
    #print the weather in the weather_page
    weather_label=tk.Label(text="f'Weather: {weather_selection}'",
                        font='optima 20 bold',
                        bg='light grey',
                        borderwidth=3,
                        #fg=f'{mood_colour}'
                        )
    weather_label.place(relx=0.5, rely=0.1, anchor='center', y=190)
    # print the weather in the health_page
    health_label = tk.Label(text="f'Health condition: {health}'",
                       font='optima 20 bold',
                       bg='light grey',
                       borderwidth=3,
                       #fg=f'{mood_colour}'
                       )
    health_label.place(relx=0.5, rely=0.1, anchor='center', y=230)
    moody_diary=tk.Button(text='Moody Diary', font='optima 20 bold', height=2, width=10)
    moody_diary.place(relx=0.5, rely=0.5, anchor='center', y=50)
    foody_recipe = tk.Button(text='Foody Recipe', font='optima 20 bold', height=2, width=10)
    foody_recipe.place(relx=0.5, rely=0.5, anchor='center', y=150)


def create_returning_user_page():
    global return_email, return_password
    # clean all the widgets from the previous page
    clear_widgets(root)
    #add the image in the homepage
    add_image(root, 'images/beginning_smile.png',screen_width,screen_height)
    #create a home page button
    homepage=tk.Button(root,
                       text="✖",
                       command=home_page)
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




#start with the home page
home_page()

#execute the code
root.mainloop()