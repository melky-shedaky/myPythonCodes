#Write a program to find the smallest of three numbers.
a = int(input("enter a number 1: "))
b = int(input("enter a number 2: "))
c = int(input("enter a number 3: "))
print("Finding the Smallest of the numbers Given : ",a,",",b,",",c )
if a<=b and a<=c:
    print("the Smallest Number is :",a)
elif b<=a and b<=c:
    print("the Smallest Number is :",b)
else:
    print("the Smallest Number is :",c)
