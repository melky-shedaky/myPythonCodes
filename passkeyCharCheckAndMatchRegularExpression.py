#Passkey/Password Match - with eight charcter Atleast
import re
p1 = input("Enter Your Password: ")
p2 = input("Re-Enter Your Password: ")
pt=r"[a-zA-Z0-9._@]{8-12}"
if re.fullmatch(pt,p1):
    if(re.match(p1,p2)):
        print("Matched")
    else:
        print("Not-Matched")
else:
    print("Password Must COntain 8-12 Charcter Atleast")
