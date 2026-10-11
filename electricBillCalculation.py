##Task 9: Electricity Bill
##Calculate the electricity bill based on units:
##•	Up to 100 units → ₹2 per unit
##•	101–200 units → ₹3 per unit
##•	Above 200 units → ₹5 per unit
##Algorithm:
##1.	Start
##2.	Read the number of units.
##3.	If units are up to 100, calculate using ₹2/unit.
##4.	Else if units are up to 200, calculate using ₹3/unit.
##5.	Otherwise, calculate using ₹5/unit.
##6.	Display the bill.
##7.	Stop.
units = int(input("enter electricity units : "))
if units >= 100:
    bill = units*2
elif units >= 200:
    bill = units*3
else:
    bill = units*5

print("Electricity Bill is: ₹",bill)
