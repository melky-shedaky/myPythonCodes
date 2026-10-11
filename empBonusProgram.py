emp_no = int(input("Enter Employee Number: "))
dept = int(input("Enter Department Number: "))
salary = float(input("Enter Salary: "))

if dept == 10:
    if salary < 5000:
        bonus = 1000
    else:
        bonus = 2000

elif dept == 20:
    if salary < 6000:
        bonus = 500
    else:
        bonus = 700
else:
    bonus = 0

print("Employee Number:", emp_no)
print("Department:", dept)
print("Salary:", salary)
print("Bonus:", bonus)
