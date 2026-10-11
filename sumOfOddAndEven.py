#sum of n number with differenciating the even odd
x = int(input('enter a number: '))
i = 1
t = 0
e=0
o=0
while(i<=x):
    t = t+i
    if(i%2==0):
        e = e+i
    else:
        o = o+i
    i=i+1
print('sum of natural numbers: ',t)
print('sum of odd num: ',o)
print('sum of even num: ',e)
