from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.geometry("444x444")
root.minsize(200, 100)
root.maxsize(1200, 988)
backgroundimg = Image.open("C:\\Users\\Nandani\\Desktop\\PythonCode\\bi burger gui.jpeg")
background_end = ImageTk.PhotoImage(backgroundimg)
bd_setting = Label(root, image=background_end)
bd_setting.place(x=0, y=0)
root.mainloop()
