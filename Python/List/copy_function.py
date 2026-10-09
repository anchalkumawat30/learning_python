# Use copy () function
from copy import deepcopy
print("copy() function :- ")
a = [1,2,3]
b = a.copy()
print(a)
print(b)
b.append(4)
print(a)
print(b)
print()
# Assignment va Copy 
print("Assignment va Copy() function :- ")
c = [1,2,3]
d = c
print(c)
print(d)
d.append(4)
print(c)
print(d)
print()
#Shallow copy 
print("Shallow copy() function :- ")
e = [[1,2],[3,4]]
f = e.copy()
f[0][0] = 100
print(e)
print(f)
# Deep copy 
print("deep copy() function :- ")
g = [[1,2],[3,4]]
h = deepcopy(g)
h[0][0] = 100
print(g)
print(h)