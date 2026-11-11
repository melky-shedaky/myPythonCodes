#PasswordStrength
import re
password = input("Enter Password : ") 
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$' 
if re.fullmatch(pattern, password): 
    print("Strong Password") 
else: 
    print("Weak Password") 



#password must be 8 with strength chekc with allows special Charcter but not must
pw = input("Enter Password : ")
pt = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z0-9@#$%^&+=!._]{8,}$'
if re.fullmatch(pt,pw): 
    print("Strong Password") 
else: 
    print("Weak Password") 
