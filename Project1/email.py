email = input("apna email bata")
password = input("apna password bhi bata")
#email = harsh@gamil.com
#password = 1234
if "@" in email:
    pass
    if email == "harsh@gmail.com" and password == "1234":
        print("Welcome")
    elif email == "harsh@gmail.com" and password != "1234":
        print("your email is correct but your oassword is wrong")
        password = input("firse password bol")
        if password == "1234":
            print("correct")
        else:
            print("still incorrect")
    else:
        print("wrong credentials")
else:
    print("Wrong email")
#testing
