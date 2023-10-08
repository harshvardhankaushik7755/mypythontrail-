import pywhatkit
phonenum = input("Enter you phone number")
#pywhatkit.sendwhatmsg("+919599501792", "maa I a messaging you using my computer withot whatsap (with python)", 20, 2)
pywhatkit.sendwhatmsg(phonenum, "maa I a messaging you using my computer withot whatsap (with python)", 20, 3, True, 2)  