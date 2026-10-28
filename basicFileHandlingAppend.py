with open("report.txt","w") as f:
    f.write("MCA I-SEMESTER\n")
    f.write("Python Programming\n")
    f.write("File Handling Fuction\n")
#"a" mode: appends without erasing existing content
with open("report.txt","a") as f:
    f.write("submitted on time.\n")

#print(f.read())
