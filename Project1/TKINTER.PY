from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Log In page")
root.minsize(700,700)
root.configure(background = "#0096DC")
img = ImageTk.PhotoImage(Image.open"flipkart-logo.png")
resized_img = img.resize(100,100)
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image = img)
img_label.pack()
root.mainloop()
#testing