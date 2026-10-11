# Developing a program to calculate electricity bills using slabs.
# 0 – 30 units: ₹1.90 per unit
# 31 – 75 units: ₹3.00 per unit
# 76 – 125 units: ₹4.50 per unit
# 126 – 225 units: ₹6.00 per unit
# 226 – 400 units: ₹8.75 per unit
# 401+ units: ₹9.75 per unit
unit = float(input("Enter your electricity units: "))
bill = 0
if unit <= 30:
    bill = unit * 1.90
    # Slab 1: 0–30 units
elif unit <= 75:
    bill = unit * 3.00
    # Slab 2: 31–75 units
elif unit <= 125:
    bill = unit * 4.50
    # Slab 3: 76–125 units
elif unit <= 225:
    bill = unit * 6.00
    # Slab 4: 126–225 units
elif unit <= 400:
    bill = unit * 8.75
    # Slab 5: 226–400 units
else:
    bill = unit * 9.75
    # Slab 6: 401+ units
print(f"Your electricity bill is: ₹{bill:.2f}")
