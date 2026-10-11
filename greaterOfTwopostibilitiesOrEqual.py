##Task 7: Largest of Two Numbers with Equality
##Problem: Compare two numbers and determine which is greater, or whether they are equal
num1 = int(input("enter number 1 : "))
num2 = int(input("enter number 2: "))

if num1 > num2:
    print(num1,": number 1 is greater")
else:
    if num2 > num1:
        print(num2,": number 2 is greater")
    else:
        print(num1,": number 1 and",num2,"number2 are equal")
