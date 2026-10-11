#Write a program to determine whether a character is a vowel or consonant.
ch = input("Enter a character: ").lower()
if ch in ("a","e","i","o","u"):
    print("The character",ch,"you entered is a VOWEL")
else:
    print("The Character",ch,"you enter is a Consonant")
