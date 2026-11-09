#Email Verfication 
import re
em = input("Enter E-Mail : ")
Pt = r"^[A-Za-z0-9._]+@[A-Za-z]+.[A-Za-z]{2,}$"
if re.fullmatch(Pt, em):
    print(em,"VALID EMail")
else:
    print(em,"INVALID EMail")
