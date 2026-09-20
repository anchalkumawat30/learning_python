#print biggest number from 3 number
a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))

if a >= b and a >= c:
    print(a," is biggest ")

elif b >= a and b >= c:
    print(b," is biggest ")
    
else :
    print(c," is biggest ")
    