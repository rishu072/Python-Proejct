import os
from itertools import cycle
import time
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of Image paths (Add your image file paths here)
image_paths = [
    r"",
    r"",
    r"",
    r"",
    r""
]

# Filter out empty paths or non-existent files
valid_paths = [path for path in image_paths if path and os.path.exists(path)]

# Resize the image to standard size
image_size = (1080, 1080)

images = []
for path in valid_paths:
    try:
        img = Image.open(path).resize(image_size)
        images.append(img)
    except Exception as e:
        print(f"Error loading image {path}: {e}")

photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

if not photo_images:
    label.config(text="No valid images found. Please add image paths in image_paths list in main.py.")

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        root.update()
        time.sleep(3)

def start_slideshow():
    if photo_images:
        update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()