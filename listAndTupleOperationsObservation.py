# List operations

numbers = [30, 10, 50, 20, 40]

print("Original List:", numbers)

numbers.append(60)
print("After Adding 60:", numbers)

numbers.remove(30)
print("After Removing 30:", numbers)

numbers.sort()
print("After Sorting:", numbers)

numbers.reverse()
print("After Reversing:", numbers)


# Tuple operations

student = ("Melky", 22, "MCA", "Kakinada")

print("\nTuple:", student)

print("First Element:", student[0])

print("Tuple Slicing:", student[1:3])

name, age, course, city = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("City:", city)
