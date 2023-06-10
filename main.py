import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image
import numpy as np
import cv2
import os.path
import subprocess

def humanbytes(B):
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)
    

def open_file_video():
        subprocess.run(["python", "video.py"])

def open_file_photo():
        subprocess.run(["python", "photos.py"])

def display_image():
        image_path = filedialog.askopenfilename()
        if image_path.endswith('.png') or image_path.endswith('.jpg'):
                img = Image.open(image_path)
                img.show()
app = ctk.CTk()
app.title("ObjectDetection")
app.geometry("400x500")

my_font = ctk.CTkFont(family="Roboto", size=22)

title_label = ctk.CTkLabel(app, text='Object Detection', font=my_font)
title_label.pack(padx=10, pady=(40, 50))

button_video = ctk.CTkButton(app, font=my_font, text="Видео", command=open_file_video)
button_video.pack(pady=10)

app.grid_columnconfigure(0, weight=1)

button_image = ctk.CTkButton(app, font=my_font, text="Картинка", command=open_file_photo)
button_image.pack(padx=40, pady=20)


# image_size_label = ctk.CTkLabel(app, text=f"Размеры выбранного изображения:{easy_size}")
# image_size_label.pack(pady=5)


app.mainloop()