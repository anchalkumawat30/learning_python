#use of Row String , F-String and Formate() function
# Row String 
print("Use of Row String :- ") 
print(r"C:\new\test")
print()
# F-String
print("Use of F-String :- ")
name = input("Enter your name : ")
age = int(input("Enter your age : ")) 
print(f"My name is {name} and I am {age} years old")
print()
# formate() function
print("Use of formate() function")
name1 = input("Enter your name : ")
age1 = int(input("Enter your age : ")) 
print("My name is {} and I am {} years old".format(name1,age1))