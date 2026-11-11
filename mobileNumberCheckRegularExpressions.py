import re
mblNo = input("Enter Mobile Number : ")
if re.fullmatch(r'[6-9]\d{9}',mblNo):
    print("Valid Mobile Number") 
else: 
    print("Invalid Mobile Number") 
