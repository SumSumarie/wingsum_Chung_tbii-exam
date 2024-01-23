import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime, timedelta

def date_click():
    date = cal.get_date()
    print(f"You clicked on date: {date}")

root = tk.Tk()
root.title("Customizable Calendar")

cal = Calendar(root, selectmode="day", year=2024, month=1, day=1)
cal.pack(padx=10, pady=10)

# Change color for specific dates (here, every 5th day is colored red)
for day in range(1, 32):
    if day % 5 == 0:
        date = datetime(2024, 1, day).date()
        cal.tag_config(f"2024-01-{day}", background="red")

        # Create an event on the date with the configured tag
        cal.calevent_create(date, "Red Day", f"2024-01-{day}")

# Button to get the selected date
button = tk.Button(root, text="Get Date", command=date_click)
button.pack(pady=10)

root.mainloop()