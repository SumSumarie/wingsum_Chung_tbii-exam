import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import DateEntry
from functools import partial
import random
import datetime
import pandas as pd
from src.helper import add_image, clear_widgets

root = tk.Tk()
root.title("Journaling App")
screen_width = 400
screen_height = 700
root.geometry(f"{screen_width}x{screen_height}")
font = ("Sitka Small", 12)
user_xp = 0
xp_label = tk.Label(root, text=f"XP: {user_xp}", font=font, bg="white", fg="black")
xp_label.pack(anchor="center")

questions = [
    "how are you feeling today?",
    "who'd you hang with today?",
    "were you productive today?",
    "did you try something new today?"
]

choices = [
    ["🤩", "😄", "😐", "😔", "😭"],
    ["friends 🤝", "family 👨‍👩‍👧‍👦", "colleagues 👩‍💻", "strangers 👥️️", "nobody 🚫️"],
    ["Very Productive 🚀", "Somewhat Productive 🌱", "Neutral 😐", "Not Very Productive 🐢", "Unproductive 🛌"],
    ["Something exciting! 🌟", "A little something new 🌱", "Not really anything new 🤷", "Nothing new, just the usual routine 🔄"]
]

quests = {
    "unproductive": [
        "Organize your workspace for 10 minutes.🧹\nA tidy space can boost productivity.✨",
        "Set a small, achievable goal for today.🎯\nCompleting it can kickstart your productivity.🚀",
        "Spend 5 minutes meditating.🧘\nClearing your mind can improve focus\nand reduce stress.😌",
        "Take a 15-minute walk outside.🚶‍♂️\nA change of scenery can refresh your mind\nand increase creativity.🌳"
    ],
    "routine": [
        "Try a new hobby or activity you've been curious about.🎨\nIt's time to explore new horizons!🌄",
        "Change one thing in your daily routine.🔄\nSmall changes can lead to big discoveries.🔍",
        "Cook a meal using a recipe you've never\ntried before.🍳Experimenting in the kitchen\ncan be a fun and rewarding challenge.🥘",
        "Wake up 30 minutes earlier than usual.⏰\nUsing this time for yourself can set\na positive tone for the day.🌅"
    ],
    "positive": [
        "Share your success story with a friend\nor family member.🗣️Your journey can\ninspire others!💖",
        "Write down what made you happy today.📝\nIt can serve as \na blueprint for future success.🌟",
        "Compliment someone sincerely.💬\nSpreading positivity can make you\nand the other person feel good.😊",
        "List three things you're grateful for.📋\nGratitude can shift your focus from\nwhat's lacking to the abundance around you.❤️"
    ]
}



# two datastructures, one for temporary storing the user responses (dictionary), one for responses from all days (df)
entries_df = pd.DataFrame(columns=['date', 'feelings', 'people', 'productivity', 'newexperience', 'thoughts'])
user_data = {"date": "", "feelings": "", "people": "", "productivity": "", "newexperience": "", "thoughts": ""}
cal = None

user_xp = 0


def assign_quests(feelings, productivity, new_experience):
    """Assign quests based on user responses."""
    assigned_quests = []

    if productivity in ["Not Very Productive 🐢", "Unproductive 🛌"]:
        # adds one of the quests for each response, random is only used to not show the same quest twice - it is still based on the user responses
        assigned_quests.append(random.choice(quests["unproductive"]))
    if new_experience in ["Not really 🤷", "No, just the usual routine 🔄"]:
        assigned_quests.append(random.choice(quests["routine"]))
    if feelings in ["🤩", "😄"] or productivity == "Very Productive 🚀":
        assigned_quests.append(random.choice(quests["positive"]))

    # Limit to 3 quests if more are available
    return assigned_quests[:3]


def display_quests():
    """Display assigned quests to the user."""
    quests_to_show = assign_quests(user_data['feelings'], user_data['productivity'], user_data['newexperience'])
    clear_widgets(root, exclude=[xp_label])
    set_background(root, "image/bggreen.jpg")

    quest_label = tk.Label(root, text="Choose one Quest to Lift Your Mood:", font=font, bg="white", fg="black")
    quest_label.pack(pady=(10, 5))

    if quests_to_show:  # Check if the list is not empty
        for quest in quests_to_show:
            quest_button = tk.Button(root, text=quest, font=font, bg="white",
                                     command=lambda q=quest: complete_quest(q))
            quest_button.pack(pady=5)
    else:
        no_quests_label = tk.Label(root, text="No quests available right now.", font=font, bg="white", fg="black")
        no_quests_label.pack(pady=(10, 5))

    back_button = tk.Button(root, text="Back to Homepage", font=font, command=lambda: create_homepage(root))
    back_button.pack(pady=(10, 0))


def complete_quest(quest):
    """Mark a quest as completed and reward the user."""
    messagebox.showinfo("Quest Completed!", "Well done! You've earned 20 XP for completing this quest.")
    update_xp(20)
    create_homepage(root)


def save_entry(thoughts=None):
    global user_data, entries_df
    if thoughts is not None:
        user_data['thoughts'] = thoughts
        update_xp(10)
    new_entry_df = pd.DataFrame([user_data])

    # adds the new entry to the list of entries, ignore index is used to fix duplicate indexing, Reference: https://saturncloud.io/blog/how-to-concatenate-rows-of-two-dataframes-in-pandas/
    entries_df = pd.concat([entries_df, new_entry_df], ignore_index=True)
    display_quests()  # Show quests after saving entry


def update_xp(amount):
    global user_xp
    user_xp += amount
    xp_label.config(text=f"XP: {user_xp}")


def show_entry():
    global entries_df, cal
    selected_date = cal.get_date().strftime('%Y-%m-%d')
    if selected_date in entries_df['date'].values:
        display_entry_details(selected_date)
    else:
        messagebox.showinfo("No Entry", "No entry exists for this date.")


def view_past_entries():
    global cal, entries_df
    clear_widgets(root, exclude=[xp_label])
    set_background(root, "image/bggreen.jpg")

    cal_label = tk.Label(root, text="Select a date and travel back in time 🚀", font=font, bg="white", fg="black")
    cal_label.pack(pady=(10, 0))
    cal = DateEntry(root, width=20, font=font, select_mode='day', date_pattern='yyyy-mm-dd')
    cal.pack(pady=(0, 10))

    show_entry_button = tk.Button(root, text="Show Entry", font=font, command=show_entry)
    show_entry_button.pack(pady=5)

    back_button = tk.Button(root, text="Back to Homepage", font=font, command=lambda: create_homepage(root))
    back_button.pack(pady=(10, 0))


def display_entry_details(selected_date):
    global entries_df
    clear_widgets(root, exclude=[xp_label])
    set_background(root, "image/bggreen.jpg")

    entry_data = entries_df[entries_df['date'] == selected_date].iloc[0]
    entry_details_text = f"On the {entry_data['date']} you felt very {entry_data['feelings']}, maybe because you met {entry_data['people']}. You were also {entry_data['productivity']} and experienced {entry_data['newexperience']}. But better hear that from yourself: \n{entry_data['thoughts']}"

    # widgets were used, so the text is not all in one line, Reference: https://chat.openai.com/share/24cbbdff-ee94-4dee-8d43-fdab2d6f89f4
    detail_text_widget = tk.Text(root, font=font, bg="white", fg="black", wrap=tk.WORD)
    detail_text_widget.pack(expand=True, fill=tk.BOTH)
    detail_text_widget.insert(tk.END, entry_details_text)
    detail_text_widget.config(state=tk.DISABLED)

    back_button = tk.Button(root, text="Back", font=font, command=view_past_entries)
    back_button.pack(pady=10)


def journal_text():
    global user_data
    clear_widgets(root, exclude=[xp_label])
    set_background(root, "image/bggreen.jpg")
    mood = user_data['feelings']
    if mood in ["🤩", "😄"]:
        mood_text = "Glad you're feeling positive today!\nFeel free to share any good vibes from your day here:"
    else:
        mood_text = "Feeling down today?\nVent about what's got you down here if you need to let it out:"

    mood_label = tk.Label(root, text=mood_text, font=font, bg="white", fg="black", wraplength=300)
    mood_label.pack(pady=(10, 10))

    thoughts_text = tk.Text(root, width=40, height=10, font=font)
    thoughts_text.pack()

    submit_button = tk.Button(root, text="Submit", font=font, bg="white",
                              command=lambda: save_entry(thoughts_text.get("1.0", "end-1c")))
    submit_button.pack(pady=(10, 0))


def store_choice(choice, page_count):
    global user_data
    categories = ["feelings", "people", "productivity", "newexperience"]
    if page_count < len(categories):
        category = categories[page_count]
        user_data[category] = choice
        update_xp(5)
        next_step = page_count + 1
        if next_step < len(questions):
            questionaire(next_step)
        else:
            journal_text()
    else:
        print("Invalid page count or questionnaire already completed.")


def questionaire(page_count):
    clear_widgets(root, exclude=[xp_label])
    set_background(root, "image/bggreen.jpg")
    question_label = tk.Label(root, text=questions[page_count], font=font, bg="white", fg="black")
    question_label.pack(anchor="center")
    # the buttons are created dynamically, so I can change the choices anytime, Reference: https://stackoverflow.com/a/22290388
    for choice in choices[page_count]:
        choice_button = tk.Button(root, text=choice, font=font, bg="white",
                                  command=partial(store_choice, choice, page_count))
        choice_button.pack(pady=10)


def create_new_entry(root):
    global cal, user_data
    clear_widgets(root, exclude=[xp_label])
    set_background(root, "image/bggreen.jpg")
    user_data["date"] = ""  # Reset date in user_data
    date_label = tk.Label(root, text="Select the date for your diary entry", font=font, bg="white", fg="black")
    date_label.pack(anchor="center")
    cal = DateEntry(root, width=20, font=font, select_mode='day')
    cal.pack(pady=10)
    submit_date = tk.Button(root, text="Continue", font=font, bg="white", command=save_date_and_continue)
    submit_date.pack(pady=10)


def save_date_and_continue():
    global user_data, cal
    # sets the date in a specific format, Reference: https://stackoverflow.com/questions/50625818/how-to-get-the-selected-date-for-dateentry-in-tkcalendar-python
    user_data["date"] = cal.get_date().strftime('%Y-%m-%d')
    questionaire(0)


def view_stats():
    global entries_df
    clear_widgets(root, exclude=[xp_label])
    set_background(root, "image/bggreen.jpg")

    today = datetime.date.today()
    past_30_days_label = tk.Label(root, text="No Problem, Skipper! \nYour Analysis for the past month:", font=font, bg="white", fg="black")
    past_30_days_label.pack(pady=(20, 5))

    # iterates through the entries of the past 30 days and saves them, Reference: https://stackoverflow.com/a/3059362
    past_30_days_stats = entries_df[entries_df['date'].isin([(today - datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(30)])]

    if not past_30_days_stats.empty:
        # checks how often specific responses are chosen within the past month, multiplied by 100 to have a percentage value, Reference: https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html
        good_days = past_30_days_stats['feelings'].isin(['🤩', '😄']).mean() * 100
        bad_days = past_30_days_stats['feelings'].isin(['😔', '😭']).mean() * 100
        productive_days = past_30_days_stats['productivity'].isin(['Very Productive 🚀', 'Somewhat Productive 🌱']).mean() * 100
        explorer_days = past_30_days_stats['newexperience'].isin(["Something exciting! 🌟", "A little something new 🌱"]).mean() * 100

        stats_text = f"My ledger shows last month you felt happy {good_days:.0f}% of the days. In contrast, {bad_days:.0f}% were not so chipper, according to my calculations."

        for feeling in ['🤩', '😄', '😐', '😔', '😭']:
            people = past_30_days_stats[past_30_days_stats['feelings'] == feeling]['people'].value_counts().head(1).index.tolist()
        if people:
            stats_text += f"The data reveals you felt most {feeling} around {people[0]}, if my hypothesis is correct."

        stats_text += f"My analysis shows you were rather productive {productive_days:.0f}% of the time and discovered something new on {explorer_days:.0f}% of the days, or so my figures indicate."

        if user_xp < 200:
            stats_text += f"\n\nWell, well, well, your {user_xp} XP confirms my hypothesis - you're still a mere hatchling! Waddle on back tomorrow to move up the pecking order!"
        elif user_xp >= 200 and user_xp < 500:
            stats_text += f"\n\nAh, {user_xp} XP eh? My calculations determine you're no longer a baby bird, but you've got a ways to go before ruling the roost!"
        elif user_xp >= 500 and user_xp < 1000:
            stats_text += f"\n\nHmm, {user_xp} XP you say? My abacus indicates you're soaring up the ranks faster than a Peregrine Falcon in a nosedive!"
        elif user_xp >= 1000 and user_xp < 2000:
            stats_text += f"\n\nAstounding! With {user_xp} XP recorded, you're well on your way to becoming the king penguin of this journal colony!"
        elif user_xp >= 2000 and user_xp < 5000:
            stats_text += f"\n\nIncredible! {user_xp} XP puts you among the journaling elite! Why, you'll be leading this flock in no time at all!"
        elif user_xp >= 5000:
            stats_text += f"\n\nBy my calculations, your {user_xp} XP confirms your status as supreme journal emperor! All hail the journaling legend!"

        # widgets were used, so the text is not all in one line, Reference: https://chat.openai.com/share/24cbbdff-ee94-4dee-8d43-fdab2d6f89f4
        detail_stats_widget = tk.Text(root, font=font, bg="white", fg="black", wrap=tk.WORD, height=10)
        detail_stats_widget.pack(expand=True, fill=tk.BOTH)
        detail_stats_widget.insert(tk.END, stats_text)
        detail_stats_widget.config(state=tk.DISABLED)
    else:
        no_data_label = tk.Label(root, text="No data available for the past month", font=font, bg="white", fg="black")
        no_data_label.pack(pady=(10, 0))

    back_button = tk.Button(root, text="Back to Homepage", font=font, command=lambda: create_homepage(root))
    back_button.pack(pady=(10, 0))


def create_homepage(root):
    user_data = {"date": "", "feelings": "", "people": "", "productivity": "", "newexperience": "", "thoughts": ""}
    clear_widgets(root, exclude=[xp_label])
    set_background(root, "image/bggreen.jpg")

    new_entry_button = tk.Button(root, text="New Entry 📓📝", font=font, command=lambda: create_new_entry(root))
    new_entry_button.pack(pady=10)

    view_entries_button = tk.Button(root, text="Travel Back in Time 🔙🕓", font=font, command=view_past_entries)
    view_entries_button.pack(pady=10)

    stats_button = tk.Button(root, text="Kowalski, Analysis 🔎📊", font=font, command=view_stats)
    stats_button.pack(pady=10)


create_homepage(root)
root.mainloop()