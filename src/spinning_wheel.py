import tkinter as tk
import random
import math

# Wheel colors
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']


def spin_wheel():
    # Randomly choose a color
    color = random.choice(colors)

    # Clear the canvas
    canvas.delete("wheel")

    # Draw the wheel
    for i in range(0, 360, 60):
        start_angle = math.radians(i)
        end_angle = math.radians(i + 60)
        canvas.create_arc(50, 50, 250, 250, start=start_angle, extent=60, style=tk.PIESLICE, fill=color, tags="wheel")

    # Update the canvas
    canvas.update()


root = tk.Tk()
root.title("Spinning Wheel")

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

spin_button = tk.Button(root, text="Spin", command=spin_wheel)
spin_button.pack()

root.mainloop()
