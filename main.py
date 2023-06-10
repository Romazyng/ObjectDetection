import tkinter as tk
import customtkinter
from tkinter import filedialog
import numpy as np
import cv2
import fileinput
import os
import pathlib
import sys
import os.path
import subprocess

def open_file_video():
        subprocess.run(["python", "video.py"])

def open_file_photo():
        subprocess.run(["python", "photos.py"])


app = customtkinter.CTk()
app.title("ObjectDetection")
app.geometry("400x400")


button = customtkinter.CTkButton(app, text="Видео", command=open_file_video)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
app.grid_columnconfigure(0, weight=1)
button = customtkinter.CTkButton(app, text="Картинка", command=open_file_photo)
app.grid_columnconfigure(0, weight=1)
button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

app.mainloop()