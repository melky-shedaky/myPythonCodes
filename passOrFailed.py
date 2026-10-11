##Task 4: Pass or Fail
##Problem: Determine whether a student has passed based on marks. Passing mark is 40.
##Algorithm:
##1.	Start
##2.	Read marks.
##3.	Check whether marks are greater than or equal to 40.
##4.	If yes, display "Pass".
##5.	Otherwise, display "Fail".
##6.	Stop.

name = input("enter student name : ")
marks = int(input("enter of the student marks : "))
if marks < 40 :
    print(name,"is failed")
else:
    print(name,"is passed")
