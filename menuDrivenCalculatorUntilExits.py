#operator-taking as an empty string
op = ""
while op != "7" and op != "x" and op != "X":
#Printing menu of the Calculator 
    print("\nMENU-DRIVEN CALCULATOR")
    print("1. ADDITION (+)")
    print("2. SUBTRACTION (-)")
    print("3. MULTIPLICATION (*)")
    print("4. DIVISION (/)")
    print("5. FLOOR DIVISION (//)")
    print("6. MODULUS (%)")
    print("7. EXIT (X)")
#taking input of the operation
    op = input("Enter operation value {1,2,3,4,5,6,7} or operator {+,-,*,/,//,%}: ")
#calculator exiting condition
    if op == "7" or op == "x" or op == "X":
        print("Calculator closed.")
        break
#addition
    if op == "1" or op == "+":
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        res = num1 + num2
        print("ADDITION (+)")
        print("Result =", res)
#subtraction
    elif op == "2" or op == "-":
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        res = num1 - num2
        print("SUBTRACTION (-)")
        print("Result =", res)
#multiplication
    elif op == "3" or op == "*":
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))
        res = num1 * num2
        print("MULTIPLICATION (*)")
        print("Result =", res)
#division
    elif op == "4" or op == "/":
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))

        if num2 == 0:
            print("Cannot divide by zero")
        else:
            res = num1 / num2
            print("DIVISION (/)")
            print("Result =", res)
#floor division
    elif op == "5" or op == "//":
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))

        if num2 == 0:
            print("Cannot divide by zero")
        else:
            res = num1 // num2
            print("FLOOR DIVISION (//)")
            print("Result =", res)
#modulus
    elif op == "6" or op == "%":
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))

        if num2 == 0:
            print("Cannot divide by zero")
        else:
            res = num1 % num2
            print("MODULUS (%)")
            print("Result =", res)
#for invalid operator
    else:
        print("INVALID OPERATOR")
