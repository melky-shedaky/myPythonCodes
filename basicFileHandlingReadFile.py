f = open("notes.txt","r")
print(f.read()) #whole file, one string
f.close()


##with open("notes.txt","r") as f:
##    lines = f.readlines()
##    print(lines)    
### file automatically closed here, even if an error occurs
