roll_no = "MCA094"
print(roll_no.isalnum())
print(roll_no.isdigit())

text = input("Enter Age: ")
if text.isdigit():
    age = int(text)
    print("valid number: ", age)
else:
    print("DIgit only Please")

#print(roll_no[3:])
