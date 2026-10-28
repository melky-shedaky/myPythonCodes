#Palindrome String
tx=input("Enter A text: ")
if tx == tx[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
