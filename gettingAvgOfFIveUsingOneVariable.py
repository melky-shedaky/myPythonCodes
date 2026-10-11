s_name = input("enter the student name : ")
s_id = input("enter the student id : ")
ttl = 0
i = 1
while(i<=5):
    marks = int(input("enter a sub marks: "))
    ttl = ttl + marks
    i = i + 1
avg = ttl/5
print('the stundent name ' + str(s_name) + '\nStudent ID : ' + str(s_id) + '\nmarks are : ' + str(ttl) + '\nAverage percentage is' + str(avg))
