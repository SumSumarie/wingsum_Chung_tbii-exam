import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
root.geometry("200x200")

# Create a canvas widget
canvas = tk.Canvas(root, width=100, height=100, bg='white', highlightthickness=0)
canvas.pack()

# Create a circular button using the canvas
button = canvas.create_oval(10, 10, 90, 90, outline='black', fill='lightblue')

# Bind a function to the button click event
canvas.tag_bind(button, '<Button-1>', lambda event: on_button_click())

root.mainloop()