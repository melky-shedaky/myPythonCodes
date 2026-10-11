#palindrome
s=input("enter a text : ").lower()
l=len(s)
for i in range(l):
    if(s[i]!=s[l-i-1]):
       print("not palindrome")
       break;
else: print("palindrome")

#
print("\n")

#palindrome with half of the string
s=input("enter a text : ").lower()
l=len(s)
for i in range(l//2):
    if(s[i]!=s[l-i-1]):
       print("not palindrome")
       break;
else:
    print("palindrome")





    
