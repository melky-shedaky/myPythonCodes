# Dictionary for storing contact details

contacts = {
    "Melky": "9876543210",
    "John": "6303760889"
}

print("Original Contacts:")
print(contacts)

# Retrieve contact
print("\nMelky's Phone Number:", contacts["Melky"])

# Add new contact
contacts["David"] = "9999999999"
print("\nAfter Adding David:")
print(contacts)

# Update contact
contacts["John"] = "1021041080"
print("\nAfter Updating John's Number:")
print(contacts)

# Delete contact
del contacts["David"]
print("\nAfter Deleting David:")
print(contacts)
