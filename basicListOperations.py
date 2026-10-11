#sequenctial DataType (LIST):
fruits = ["apple","mango","kiwi","grape"]
marks = [88,45,62,39,84]
mixed = ["MCA", 12, 23.7, True ]
print(fruits,"\n",marks,"\n",mixed)
print(fruits[0])
print(fruits[-1])


#list Slicing
nu=[10,20,30,40,50,60]
print(nu[1:4])
print(nu[:3])
print(nu[3:])
print(nu[::2])
print(nu[::-1])


#list adding elements
f=["apple","banana"]

f.append("kiwi")
print(f)
f.insert(1,"gireesh")
print(f)
f.extend(["date","day"])
print(f)

#list-remvoing elements
n=[10,20,30,40,50,20]
n.remove(20)
print(n)
n.pop(-1)
print(n)
del n[1:2]
print(n)
n.clear()
print(n)


n=[10,20,40,30,50,60,80,85,70,90]
print(len(n))
print(type(n))
n.sort()
print(n)
n.sort(reverse=True)
print(n)
n.reverse()
print(n)
print(n.index(50))
print(n.count(40))
num=n.copy()
print(num)
