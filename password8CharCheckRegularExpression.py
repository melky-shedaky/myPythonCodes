#onlyPassKeyCheckRegularExpression
import re
psky= input("Enter your password: ")
Pattern = r"[a-zA-Z0-9@._]{8,}"
if re.fullmatch(Pattern,psky):
    print("Passkey Is STRONG")
else:
    print("Password must Atleast Contain 8 charcters ")
