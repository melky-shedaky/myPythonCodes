#natural numbers
n=int(input('enter range: '))
for i in range(1,n+1):
    print(i)

#even numbers
n=int(input('enter range: '))
for i in range(2,n+1,2):
    print(i)

#odd number
n=int(input('enter range: '))
for i in range(1,n+1,2):
    print(i)

#differanciate the natural into EVEN & ODD
n=int(input('enter range: '))
for i in range(1,n+1):
    if (i%2==0):
        print(i," even")
    else:
        print(i," odd")

#sum of natural number using for
n = int(input('enter range : '))
s = 0
for i in range(1,n+1):
    s = s + i
print(s)

#sum of natural, sum of even & sum of odd
n = int(input('enter range: '))
ns,es,os = 0,0,0
for i in range(1,n+1):
    ns=ns+i
    if(i%2==0):
        es=es+i
    else:
        os=os+i
print(ns)
print(es)
print(os)
