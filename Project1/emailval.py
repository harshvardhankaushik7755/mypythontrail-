import re
email_veri = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your Email : ")

if re.search(email_veri, user_email):
    print(" Rightemail")
else:
    print("Wrong")