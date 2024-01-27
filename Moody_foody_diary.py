import tkinter as tk
from datetime import datetime
from datetime import date
from tkcalendar import Calendar
from tkcalendar import DateEntry
import pandas as pd
from src.helper import clear_widgets, add_image
from tkinter import messagebox
#from dateutil.relativedelta import relativedelta
#from tkinter import ttk
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
    """This is a page after the main page(log in)"""
    # store the data
    enter_user_data()

    clear_widgets(root)
    # add the image in the homepage
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    #create a home page button
    homepage=tk.Button(root,
                       text="✖️",
                       command=main_page)

    homepage.place(relx = 0.2,anchor = 'ne',y=15)

    new_user_page_label=tk.Label(root,
                           text=(f"{username.get()}, "
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
                         command=mood_colour_question
                         )

    new_diary.place(relx=0.9, anchor='center', y=600)

def mood_colour_question():
    # destroy everything in the daypage
    clear_widgets(root)
    # add the image in the homepage
    add_image(root, 'images/beginning_smile.png', screen_width, screen_height)
    # Asking the colour of the users' mood today
    # create a home page button
    homepage = tk.Button(root,
                         text="✖️",
                         command=main_page)

    homepage.place(relx=0.2, anchor='ne', y=15)
    question_label = tk.Label(root, text='What is the colour of your mood today?',
                              font='optima 18 bold',
                              bg='light yellow',
                              fg='black',
                              borderwidth=12)
    # where would you like to place this button
    question_label.place(relx=0.5, anchor='center', y=100)

    #mood_colour_button=["red_button","orange_button","yellow_button","green_button","cyan_button","blue_button","purple_button"]

    # The button to choose red as the colour of the mood today
    red_button = tk.Button(text=':)',
                           fg='red',
                           font='Arial 20 bold',
                           height=2,
                           width=10,
                           command=lambda: mood_emoji_page("red_button")
                           )
    red_button.place(relx=0.5, rely=0.57, anchor='center', y=-195)
     # The button to choose orange as the colour of the mood today
    orange_button = tk.Button(text=':)',
                              fg='orange',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda: mood_emoji_page("orange_button")
                              )
    orange_button.place(relx=0.5, rely=0.57, anchor='center', y=-130)
    # The button to choose yellow as the colour of the mood today
    yellow_button = tk.Button(text=':)',
                              fg='yellow',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda: mood_emoji_page("yellow_button")
                              )
    yellow_button.place(relx=0.5, rely=0.57, anchor='center', y=-65)
    # The button to choose green as the colour of the mood today
    green_button = tk.Button(text=':)',
                             fg='green',
                             font='Arial 20 bold',
                             height=2,
                             width=10,
                             command=lambda: mood_emoji_page("green_button")
                             )
    green_button.place(relx=0.5, rely=0.57, anchor='center', y=0)
    # The button to choose Indigo as the colour of the mood today
    cyan_button = tk.Button(text=':)',
                            fg='cyan',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda: mood_emoji_page("cyan_button")
                            )
    cyan_button.place(relx=0.5, rely=0.57, anchor='center', y=65)
    # The button to choose blue as the colour of the mood today
    blue_button = tk.Button(text=':)',
                            fg='blue',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda: mood_emoji_page("blue_button")
                            )
    blue_button.place(relx=0.5, rely=0.57, anchor='center', y=130)
    # The button to choose purple as the colour of the mood today
    purple_button = tk.Button(text=':)',
                              fg='purple',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda: mood_emoji_page("purple_button")
                              )
    purple_button.place(relx=0.5, rely=0.57, anchor='center', y=195)



#this is the page where the recipes will come next randomly based on the colour the users chose
def mood_emoji_page(mood_colour_selection):
    global mood_colour,options

    #when the users chose red button, it will randomly pick the recipes related to the colour red
    if mood_colour_selection == "red_button":
        mood_colour = "red"
        options = ["red01.jpg", "red02.jpg", "red03.jpg"]
    # when the users chose orange button, it will randomly pick the recipes related to the colour orange
    elif mood_colour_selection == "orange_button":
        mood_colour = "orange"
        options = ["orange01.jpg", "orange02.jpg", "orange03.jpg"]
    # when the users chose yellow button, it will randomly pick the recipes related to the colour yellow
    elif mood_colour_selection == "yellow_button":
        mood_colour = "yellow"
        options = ["yellow01.jpg", "yellow02.jpg", "yellow03.jpg"]
    # when the users chose green button, it will randomly pick the recipes related to the colour green
    elif mood_colour_selection == "green_button":
        mood_colour = "green"
        options = ["green01.jpg", "green02.jpg", "green03.jpg"]
    #when the users chose cyan button, it will randomly pick the recipes related to the colour cyan
    elif mood_colour_selection == "cyan_button":
        mood_colour = "cyan"
        options = ["cyan01.jpg", "cyan02.jpg", "cyan03.jpg"]
    # when the users chose blue button, it will randomly pick the recipes related to the colour blue
    elif mood_colour_selection == "blue_button":
        mood_colour = "blue"
        options = ["blue01.jpg", "blue02.jpg", "blue03.jpg"]
    # when the users chose purple button, it will randomly pick the recipes related to the colour purple
    elif mood_colour_selection == "purple_button":
        mood_colour = "purple"
        options = ["purple01.jpg", "purple02.jpg", "purple03.jpg"]


    # store the data
    user_mood_data = {"username": username.get(),
                      "mood_colour":mood_colour
                      }
    # converting the dictionary to a data frame
    user_data = pd.DataFrame([user_mood_data])
    user_data.to_csv("data/user_mood_data.csv", index=False, header=False, mode='a')


    # destroy all the button in the colour button page
    clear_widgets(root)
    # adding image on each colour page
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # create a home page button
    homepage = tk.Button(root,
                         text="✖️",
                         command=mood_colour_question)

    homepage.place(relx=0.2, anchor='ne', y=15)

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
                            command=lambda:weather_page()
                            )

    grinning_emoji.place(relx=0.2, rely=0.2, anchor='center', y=50)
    # adding 😁 emoji
    beaming_emoji = tk.Button(root,
                          text="😁",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page()
                          )

    beaming_emoji.place(relx=0.2, rely=0.2, anchor='center', y=100)
    # adding ☺️ emoji
    smiling_emoji = tk.Button(root,
                               text="☺️",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page()
                               )

    smiling_emoji.place(relx=0.2, rely=0.2, anchor='center', y=150)
    # adding 😍 emoji
    heart_eyes_emoji = tk.Button(root,
                                text="😍",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    heart_eyes_emoji.place(relx=0.2, rely=0.2, anchor='center', y=200)
    # adding 🥰 emoji
    heart_emoji = tk.Button(root,
                                text="🥰",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    heart_emoji.place(relx=0.2, rely=0.2, anchor='center', y=250)

    # adding 😉 emoji
    winking_emoji = tk.Button(root,
                                text="😉",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    winking_emoji.place(relx=0.2, rely=0.2, anchor='center', y=300)

    # adding 😋 emoji
    face_savoring_emoji = tk.Button(root,
                                text="😋",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    face_savoring_emoji.place(relx=0.2, rely=0.2, anchor='center', y=350)

    # adding 😎 emoji
    sunglasses_emoji = tk.Button(root,
                            text="😎",
                            font=("Optima", 25, "bold"),
                            height=1,
                            width=1,
                            command=lambda:weather_page()
                            )

    sunglasses_emoji.place(relx=0.4, rely=0.2, anchor='center', y=50)
    # adding 🤩 emoji
    star_struck_emoji = tk.Button(root,
                          text="🤩",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page()
                          )

    star_struck_emoji.place(relx=0.4, rely=0.2, anchor='center', y=100)
    # adding 🥳️ emoji
    partying_emoji = tk.Button(root,
                               text="🥳",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page()
                               )

    partying_emoji.place(relx=0.4, rely=0.2, anchor='center', y=150)
    # adding 🤪 emoji
    zany_face_emoji = tk.Button(root,
                                text="🤪",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    zany_face_emoji.place(relx=0.4, rely=0.2, anchor='center', y=200)
    # adding 😝 emoji
    tongue_emoji = tk.Button(root,
                                text="😝",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    tongue_emoji.place(relx=0.4, rely=0.2, anchor='center', y=250)

    # adding 😂 emoji
    tears_of_joy_emoji = tk.Button(root,
                                text="😂",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    tears_of_joy_emoji.place(relx=0.4, rely=0.2, anchor='center', y=300)

    # adding 🥲 emoji
    single_tear_emoji = tk.Button(root,
                                text="🥲",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    single_tear_emoji.place(relx=0.4, rely=0.2, anchor='center', y=350)

    # adding 😒 emoji
    unamused_emoji = tk.Button(root,
                            text="😒",
                            font=("Optima", 25, "bold"),
                            height=1,
                            width=1,
                            command=lambda:weather_page()
                            )

    unamused_emoji.place(relx=0.6, rely=0.2, anchor='center', y=50)
    # adding 😖 emoji
    confounded_emoji = tk.Button(root,
                          text="😖",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page()
                          )

    confounded_emoji.place(relx=0.6, rely=0.2, anchor='center', y=100)
    # adding 😫 emoji
    tired_emoji = tk.Button(root,
                               text="😫",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page()
                               )

    tired_emoji.place(relx=0.6, rely=0.2, anchor='center', y=150)
    # adding 🥺 emoji
    pleading_emoji = tk.Button(root,
                                text="🥺",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    pleading_emoji.place(relx=0.6, rely=0.2, anchor='center', y=200)
    # adding 😤 emoji
    steam_nose_emoji = tk.Button(root,
                                text="😤",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    steam_nose_emoji.place(relx=0.6, rely=0.2, anchor='center', y=250)

    # adding 😭 emoji
    crying_emoji = tk.Button(root,
                                text="😭",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    crying_emoji.place(relx=0.6, rely=0.2, anchor='center', y=300)

    # adding 😡 emoji
    enraged_emoji = tk.Button(root,
                                text="😡",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    enraged_emoji.place(relx=0.6, rely=0.2, anchor='center', y=350)

    # adding 🤬 emoji
    swear_emoji = tk.Button(root,
                            text="🤬",
                            font=("Optima", 25, "bold"),
                            height=1,
                            width=1,
                            command=lambda:weather_page()
                            )

    swear_emoji.place(relx=0.8, rely=0.2, anchor='center', y=50)
    # adding 🤯 emoji
    exploding_head_emoji = tk.Button(root,
                          text="🤯",
                          height=1,
                          width=1,
                          font=("Optima", 25, "bold"),
                          command=lambda:weather_page()
                          )

    exploding_head_emoji.place(relx=0.8, rely=0.2, anchor='center', y=100)
    # adding 😳 emoji
    flushed_face_emoji = tk.Button(root,
                               text="😳",
                               height=1,
                               width=1,
                               font=("Optima", 25, "bold"),
                               command=lambda:weather_page()
                               )

    flushed_face_emoji.place(relx=0.8, rely=0.2, anchor='center', y=150)
    # adding 😱 emoji
    fear_emoji = tk.Button(root,
                                text="😱",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    fear_emoji.place(relx=0.8, rely=0.2, anchor='center', y=200)
    # adding 😰 emoji
    anxious_emoji = tk.Button(root,
                                text="😰",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    anxious_emoji.place(relx=0.8, rely=0.2, anchor='center', y=250)

    # adding 😵‍💫 emoji
    dizziness_emoji = tk.Button(root,
                                text="😵‍💫",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    dizziness_emoji.place(relx=0.8, rely=0.2, anchor='center', y=300)

    # adding 😴 emoji
    sleeping_emoji = tk.Button(root,
                                text="😴",
                                height=1,
                                width=1,
                                font=("Optima", 25, "bold"),
                                command=lambda:weather_page()
                                )

    sleeping_emoji.place(relx=0.8, rely=0.2, anchor='center', y=350)

def diary_page(mood_colour):
    # destroy all the button in the colour button page
    clear_widgets(root)
    # adding image on each colour page
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # create a home page button
    homepage = tk.Button(root,
                         text="✖️",
                         command=mood_colour_question)

    homepage.place(relx=0.2, anchor='ne', y=15)
    # the welcome question
    welcome = tk.Label(text=f"Write down your Moody Diary ", font='optima 25 bold', bg='light grey',
                       borderwidth=3, fg=f'{mood_colour}')
    # place welcome question on a grid
    welcome.place(relx=0.5, rely=0.5, anchor='center', y=-100)
    #add storyinp as a stringVar
    storyinp = tk.StringVar()
    # add the box for entering a story related to this colour
    story_box = tk.Entry(root, textvar=storyinp, font='arial 20 bold')
    # place story box on a grid
    story_box.place(relx=0.5, rely=0.5, anchor='center', y=10, height=150)
    # add buttons of Enter
    enter_button = tk.Button(text='Enter', font='optima 20 bold', height=2, width=7,command=food)
    enter_button.place(relx=0.5, rely=0.5, anchor='center', y=150)


def weather_page():
    global mood_colour
    # destroy everything in the daypage
    clear_widgets(root)
    # add the image in the homepage
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # Asking the colour of the users' mood today
    # create a home page button
    homepage = tk.Button(root,
                         text="✖",
                         command=lambda:diary_page(mood_colour)
                         )

    homepage.place(relx=0.2, anchor='ne', y=15)
    question_label = tk.Label(root, text='What is the weather today?',
                              font='optima 18 bold',
                              bg='light yellow',
                              fg='black',
                              borderwidth=12)
    # where would you like to place this button
    question_label.place(relx=0.5, anchor='center', y=100)

    # mood_colour_button=["red_button","orange_button","yellow_button","green_button","cyan_button","blue_button","purple_button"]

    # The button to choose sunny
    sunny_button = tk.Button(text='☀️',
                           font='Arial 20 bold',
                           height=2,
                           width=10,
                           command=lambda:health_page()
                           )
    sunny_button.place(relx=0.5, rely=0.57, anchor='center', y=-195)
    # The button to choose sunny with clouds
    sunny_with_clouds_button = tk.Button(text='🌤️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:health_page()
                              )
    sunny_with_clouds_button.place(relx=0.5, rely=0.57, anchor='center', y=-130)
    # The button to choose cloudy
    cloudy_button= tk.Button(text='☁️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:health_page()
                              )
    cloudy_button.place(relx=0.5, rely=0.57, anchor='center', y=-65)
    # The button to choose rain with sun
    rain_with_sun_button = tk.Button(text='🌦️',
                             font='Arial 20 bold',
                             height=2,
                             width=10,
                             command=lambda:health_page()
                             )
    rain_with_sun_button.place(relx=0.5, rely=0.57, anchor='center', y=0)
    # The button to choose rainy
    rainy_button = tk.Button(text='🌧️',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda:health_page()
                            )
    rainy_button.place(relx=0.5, rely=0.57, anchor='center', y=65)
    # The button to choose clouds with lightning
    clouds_with_lightning_button = tk.Button(text='⛈️',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda:health_page()
                            )
    clouds_with_lightning_button.place(relx=0.5, rely=0.57, anchor='center', y=130)
    # The button to choose snowy
    snowy_button = tk.Button(text='🌨️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:health_page()
                              )
    snowy_button.place(relx=0.5, rely=0.57, anchor='center', y=195)

    # The button to choose heavy snowy
    heavy_snowy_button = tk.Button(text='❄️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:health_page()
                              )
    heavy_snowy_button.place(relx=0.5, rely=0.57, anchor='center', y=195)


def health_page():
    global mood_colour
    # destroy everything in the daypage
    clear_widgets(root)
    # add the image in the homepage
    add_image(root, f"images/{mood_colour}_smile.jpg", screen_width, screen_height)
    # Asking the colour of the users' mood today
    # create a home page button
    homepage = tk.Button(root,
                         text="✖",
                         command=lambda:diary_page(mood_colour)
                         )

    homepage.place(relx=0.2, anchor='ne', y=15)
    question_label = tk.Label(root, text='How physically healthy are you?',
                              font='optima 18 bold',
                              bg='light yellow',
                              fg='black',
                              borderwidth=12)
    # where would you like to place this button
    question_label.place(relx=0.5, anchor='center', y=100)

    # The button to choose Excellent
    Excellent_button = tk.Button(text='Excellent',
                           font='Arial 20 bold',
                           height=2,
                           width=10,
                           command=lambda:diary_page(mood_colour)
                           )
    Excellent_button.place(relx=0.5, rely=0.57, anchor='center', y=-195)
    # The button to choose Good
    good_button = tk.Button(text='Good️',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:diary_page(mood_colour)
                              )
    good_button.place(relx=0.5, rely=0.57, anchor='center', y=-130)
    # The button to choose So_so
    So_so_button= tk.Button(text='So so',
                              font='Arial 20 bold',
                              height=2,
                              width=10,
                              command=lambda:diary_page(mood_colour)
                              )
    So_so_button.place(relx=0.5, rely=0.57, anchor='center', y=-65)
    # The button to choose rain with sun
    not_well_button = tk.Button(text='Not well',
                             font='Arial 20 bold',
                             height=2,
                             width=10,
                             command=lambda:diary_page(mood_colour)
                             )
    not_well_button.place(relx=0.5, rely=0.57, anchor='center', y=0)
    # The button to choose Super_bad️
    super_bad_button = tk.Button(text='Super bad️',
                            font='Arial 20 bold',
                            height=2,
                            width=10,
                            command=lambda:diary_page(mood_colour)
                            )
    super_bad_button.place(relx=0.5, rely=0.57, anchor='center', y=65)

def food():
    global title_label,back_button,img
    # destroy everything
    clear_widgets(root)
    #adding the random recipy based on the colours that the users selected
    add_image(root, f'images/{random.choice(options)}',screen_width,screen_height)
    #adding a close button leading to the daypage of the changed-colour day button, but it doesn't work
    save_button = tk.Button(text='Save', fg='grey', font='optima 9 bold', height=1,width=4)
    save_button.place(relx=0.5, anchor='center', y=635)
    # create a home page button
    homepage = tk.Button(root,
                         text="🏠",
                         command=main_page)
    homepage.place(relx=0.2, anchor='ne', y=15)


def create_returning_user_page():
    global return_email, return_password
    clear_widgets(root)
    #add the image in the homepage
    add_image(root, 'images/beginning_smile.png',screen_width,screen_height)
    #create a home page button
    homepage=tk.Button(root,
                       text="🏠",
                       command=main_page)
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
    # get the list of user ids
    user_ids = list(pd.read_csv("data/user_data.csv").username)

    if username.get() in user_ids:
        tk.messagebox.showwarning("warning", "This username is taken")
    elif email.get() in user_ids:
        tk.messagebox.showwarning("warning", "This email is taken")
    else:
        user_data = {
            "username":username.get(),
            "email":email.get(),
            #"birthday": birthday.get(),
            "create_at":current_timestamp
        }
        # converting the dictionary to a data frame
        user_data = pd.DataFrame([user_data])
        user_data.to_csv("data/user_data.csv", index=False, header=False, mode='a')
        # clean all the widget
        clear_widgets(root)

        thank_button=tk.Label(root,
                 text=(f"Thank you for submitting your data {username.get()}")
                 )
        thank_button.place(x=150,y=200)


def main_page():
    """This the the main page"""
    global username, email, birthday, password
    clear_widgets(root)
    #add the image in the homepage
    add_image(root, 'images/beginning_smile.png',screen_width,screen_height)
    # print a message saying 'Open your Moody Foody Diary'
    title_label = tk.Label(root, text='This is your Moody Foody Diary', font='optima 20 bold',bg='light yellow', borderwidth=25)
    # where would you like to place this button
    title_label.place(relx = 0.5,anchor = 'center',y=150)

    # print a message asking the user for their name
    username_label = tk.Label(root, text='Username', font='optima 20 bold', borderwidth=3)
    # where would you like to place this button
    username_label.place(x=20,y=250)
    username=tk.StringVar()
    username_entry=tk.Entry(root,
                        textvar=username,
                        font='optima 20 bold',
                        width=15)
    username_entry.place(x=130,y=250)

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
    """
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
    """
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
    """
    #create the button to click to create_returning_user_page
    return_user_button = tk.Button(root,
                              text="Already have your diary?",
                              font='optima 15 bold',
                              command=create_returning_user_page)
    return_user_button.place(relx=0.5, anchor='center', y=600)
    """




#initiate pygame
#pg.init()
#load the music
#pg.mixer.music.load("music/music.mp3")
#play the music
#pg.mixer.music.play()

#start with the create_diary page
main_page()

#execute the code
root.mainloop()