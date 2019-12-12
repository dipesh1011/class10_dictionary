import re
mail=input("Enter your mail")
vmail='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
if re.search(vmail,mail):
    print("It is a valid mail.")
else:
    print("It is not a valid mail.")
