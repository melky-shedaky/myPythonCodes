##Task 6: Positive, Negative or Zero
##Problem: Determine whether a given number is positive, negative, or zero.
##Algorithm:
##1.	Start
##2.	Read a number.
##3.	If number is greater than 0, display "Positive".
##4.	Else if number is less than 0, display "Negative".
##5.	Otherwise, display "Zero".
##6.	Stop.
num = int(input("enter a number: "))
if num >= 1 :
    print(num,"is postive Number")
elif num == 0:
    print(num,"is zero")
else:
    print(num,"is negative num")
