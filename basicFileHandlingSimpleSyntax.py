f= open("report.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

with open("report.txt","r") as f:
    print(f.read(3))
    print(f.readline())
    print(f.readlines())
