#program-6 : Character Frequency
tx =  input("Enter String: ")
for ch in sorted(set(tx)):
    print(ch,"=",tx.count(ch))
