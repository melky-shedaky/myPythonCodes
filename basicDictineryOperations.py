# Dictionary Operations

stu = {
    "name": "Melky Shedak",
    "age": 22,
    "course": "M.C.A"
}
# Accessing values
print(stu["name"])
print(stu.get("age"))

# Using get() with a default value
print(stu.get("city", "Not Found"))

# Printing the complete dictionary
print(stu)

# Adding a new key-value pair
stu["city"] = "Kakinada"
print(stu.get("city"))

# Adding roll number
stu.update({"rollno": "O94"})

# Adding parents
stu.update({"parents": ["Micah", "Padma"]})

print(stu)
