import tkinter as tk
from tkcalendar import Calendar
from helper import clear_widgets, add_image


#set tk as root
root = tk.Tk()
#give it a title
root.title("Moody Foody Diary")
#change the size
screen_width= 350
screen_height= 650
root.minsize(screen_width,screen_height)


# Your diary entries dictionary
diary_entries = {
    "2024-01-01": "Today I did...",
    "2024-01-02": "Had a great time...",
    # and so on...
}




def update_diary():
    date = cal.get_date()
    diary_text.delete(1.0, tk.END)  # Clear previous text
    diary_text.insert(tk.END, diary_entries.get(date, "No diary entry for this date."))

def save_diary():
    date = cal.get_date()
    entry = diary_text.get(1.0, tk.END)
    diary_entries[date] = entry.strip()

#add the image in the homepage
add_image(root, '../images/beginning_smile.png',screen_width,screen_height)


cal = Calendar(root, selectmode="day")
cal.pack(padx=20, pady=20)

view_button = tk.Button(root, text="View Diary", command=update_diary)
view_button.pack(pady=10)

diary_text = tk.Text(root, height=10, width=40)
diary_text.pack(padx=20, pady=20)

save_button = tk.Button(root, text="Save Diary", command=save_diary)
save_button.pack(pady=10)

root.mainloop()
