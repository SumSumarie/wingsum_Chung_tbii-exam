import tkinter as tk
from PIL import Image, ImageTk

def get_pixel_color(event):
    x, y = event.x, event.y
    pixel_color = img.getpixel((x, y))
    print(f"Color at ({x}, {y}): {pixel_color}")

root = tk.Tk()

# Load an image
image = Image.open("../images/beginning_smile.png")
img = ImageTk.PhotoImage(image)


# Get image dimensions
image_width, image_height = image.size

# Create a Canvas with the image
canvas = tk.Canvas(root, width=image.width(), height=image.height())
canvas.create_image(0, 0, anchor="nw", image=img)
canvas.pack()

# Bind a function to get the color on click
canvas.bind("<Button-1>", get_pixel_color)

root.mainloop()