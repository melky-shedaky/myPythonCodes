# Factorial using while loop

num = int(input("Enter a number: "))

fact = 1
i = 1

if num < 0:
    print("Factorial is not possible for negative numbers")
else:
    while i <= num:

        if i == 0:
            continue

        fact = fact * i
        i = i + 1

    else:
        print("While loop completed successfully")

    print("Factorial =", fact)

# pass statement
if num == 0:
    pass
