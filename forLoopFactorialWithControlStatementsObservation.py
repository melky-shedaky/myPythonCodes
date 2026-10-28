# Factorial using for loop

num = int(input("Enter a number: "))

fact = 1

if num < 0:
    print("Factorial is not possible for negative numbers")
else:
    for i in range(1, num + 1):

        if i == 0:
            continue

        if i == num + 1:
            break

        fact = fact * i

    else:
        print("For loop completed successfully")

    print("Factorial =", fact)

# pass statement
if num == 0:
    pass
