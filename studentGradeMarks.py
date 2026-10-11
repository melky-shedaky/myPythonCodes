##if-elif-else-multiple possibiliities
#task5:Grade Calculator
#display the grade based on the marks.
#Marks	Grade, 90–100:A, 75–89:B, 60–74:C, 40–59:D, Below 40:F
##Algorithm:
##1.	Start
##2.	Read marks.
##3.	If marks are 90 or above, display A.
##4.	Else if marks are 75 or above, display B.
##5.	Else if marks are 60 or above, display C.
##6.	Else if marks are 40 or above, display D.
##7.	Otherwise, display F.
##8.	Stop.
name = input("enter the name of the student: ").upper()
marks=int(input("enter marks: "))
if marks >= 90:
    print(name,"GRADE IS: A")
elif marks >= 75:
    print(name,"GRADE IS: B")
elif marks >= 60:
    print(name,"GRADE IS: C")
elif marks >= 40:
    print(name,"GRADE IS: D")
else:
    print(name,"is failed")
