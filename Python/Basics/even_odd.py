#With One number
a = int(input("Enter a number "))
if a%2 == 0 :
     print("Even")
else :
     print("Odd")
     
# With multiple numbers
b = int(input("\nEnter a number to check even or odd upto that number "))
print("\n\nEven number")
for i in range(1,b+1):
     if i%2 == 0 :
          print(i,end=" ")
print("\n\nOdd number")        
for j in range(1,b+1):
     if j%2!= 0:
          print(j,end=" ")