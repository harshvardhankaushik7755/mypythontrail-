from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()
    print(email,password)
    #password = 1234
    if "@" in email:
        pass
        if email == "harsh@gmail.com" and password == "1234":
            messagebox.showinfo("ok","login succesful")    
        elif email == "harsh@gmail.com" and password != "1234":
            messagebox.showinfo("your email is correct but your password is wrong")
            password = input("Bhai","firse password bol ")
            if password == "1234":
                messagebox.showinfo("correct")
            else:
                messagebox.showinfo("still incorrect")
        else:
            messagebox.showinfo("wrong credentials")
    else:
        messagebox.showinfo("Wrong email")
root = Tk()
root.title("login form")
root.geometry("350x500")
root.configure(background="#0096DC")

img = Image.open('C:\\Users\\Nandani\\Desktop\\PythonCode\Project1\\flipkart.png')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)
img_label.pack(pady=(10,10))
text_label = Label(root,text="Flipkart",fg="white",bg="#0096DC")
text_label.pack()
text_label.config(font=("verdana", 24))

email_label = Label(root,text="Enter Email",fg="white",bg="#0096DC")
email_label.pack(pady=(20,5))
email_label.config(font=("verdana",12))
email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label = Label(root,text="Enter Password",fg="white",bg="#0096DC")
password_label.pack(pady=(20,5))
password_label.config(font=("verdana",12))
password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root,text="login now",bg="white",fg="black",width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=("verdana",12))

root.mainloop()