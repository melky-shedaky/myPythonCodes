name = input("enter the name of the student: ").upper()
marks=int(input("enter marks: "))
if marks <= 100:
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
else:
    print("Error")
