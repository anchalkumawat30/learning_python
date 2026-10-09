# use sort() function
print("use sort() function :- ")
a = [30,10,20]
a.sort()
print(a)
print()
# use reverse sort 
print("Use reverse sort :- ")
a.sort(reverse = True)
print(a)
print()
# Key in sorting 
print("Key in sorting :- ")
d = ["cat","elephant", "dog", "hi"]
d.sort(key = len)
print(d)
print()
#Reverse with key 
print("Reverse with key :- ")
e = ["cat","elephant", "dog", "hi"]
e.sort(key = len , reverse=True)
print(e)
print()
# use sorted() function 
print("Use sorted() function :- ")
b = [30,10,20]
c = sorted(b)
print(b)
print(c)