from tkinter import *
import os
from PIL import ImageTk, Image

root = Tk()

root.title("Wallpaper Viewer")
root.geometry("250x400")
root.configure(background="black")
files = os.listdir("C:\\Users\\Nandani\\Desktop\\PythonCode\\wallpapers")

img_array = []
for file in files:
    img = Image.open(os.path.join("C:\\Users\\Nandani\\Desktop\\PythonCode\\wallpapers\\tk.jpg",file))
    resized_img = img.resize((200,300))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label = Label(root,image=img_array[0])
img_label.pack(pady=(15, 10))
root.mainloop()
