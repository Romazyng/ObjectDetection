# import tkinter as tk
# import pathlib
# from tkinter import filedialog
# import subprocess
 
# def open_file():
#     filename = filedialog.askopenfilename()
#     if filename:
#         subprocess.run(["python", "photos.py", filename])
#     print(pathlib.PurePath(filename).name)
 
# root = tk.Tk()
# button = tk.Button(root, text="Выбрать файл", command=open_file)
# button.pack()
 
# root.mainloop()