##Task 10: Calculator
##Create a simple calculator that accepts two numbers and an operator (+, -, *, /).
##Algorithm:
##1.	Start
##2.	Read the first number.
##3.	Read the second number.
##4.	Read the operator.
##5.	If operator is +, perform addition.
##6.	Else if operator is -, perform subtraction.
##7.	Else if operator is *, perform multiplication.
##8.	Else if operator is /, perform division.
##9.	Otherwise, display "Invalid operator".
##10.	Stop.

num1 = float(input("enter a number: "))
num2 = float(input("enter a number: "))
op = input("please enter a operator{+,-,*,/,//,%}: ")
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
elif op == "//":
    print(num1//num2)
elif op == "%":
    print(num1%num2)
else:
    print("invalid operator")
