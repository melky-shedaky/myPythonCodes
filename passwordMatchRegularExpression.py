#Passkey/Password Match
import re
p1 = input("Enter Your Password: ")
p2 = input("Re-Enter Your Password: ")
if(re.match(p1,p2)):
    print("Matched")
else:
    print("Not-Matched")
