##Task 8: Student Result
##Problem: A student passes only if they have scored at least 40 marks. If they pass, determine whether they received distinction (75 or above).
##Algorithm:
##1.	Start
##2.	Read marks.
##3.	Check whether marks are greater than or equal to 40.
##4.	If yes:
##o	Check whether marks are greater than or equal to 75.
##o	If yes, display "Pass with Distinction".
##o	Otherwise, display "Pass".
##5.	Otherwise, display "Fail".
##6.	Stop.

m = int(input("Enter your marks : "))

if m >= 40:
    if m >= 75:
        print("Pass with Distinction")
    else:
        print("Pass")
else:
    print("Fail")
##
##if m <= 100:
##    if m >= 40:
##        if m >= 75:
##            print("Pass with Distinction")
##        else:
##            print("Pass")
##    else:
##        print("Fail")
##else:
##    print("error://<Marks entered is higher then limitation>")
##
