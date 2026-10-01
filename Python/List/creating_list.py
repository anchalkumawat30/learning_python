# Creating a list 
print("Creating a list :- ")
number = [10,20,30]
print ("The List is = ",number)
print()
# input using itereter 
print("input using itereter :- ")
num = []
n = int(input("How many number : "))
for i in range(n):
     value = int(input("Enter a number : "))
     num.append(value)
print("The List is = ",num)
print()
# input without using itereter 
print("input without using itereter :- ")
name = input("Enter name : ").split()
print("The number is : ",name)
print()
#  input without using itereter and with comma , 
print("input without using itereter and with comma , :- ")
name1 = input("Enter name : ").split(",")
print("The name is : ", name1)