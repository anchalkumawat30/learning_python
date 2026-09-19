#print a table 
n= int(input("Enter a number to display a table: "))
for i in range(1,11):
    print(n ," X ", i, " = ", n*i)
    
    
#print a table upto the number 
n = int(input("Enter a number to display the table upto that number: "))
for i in range(1,n+1):
    print("\nTable of ", i)
    for j in range(1,11):
        print(i ," X ", j, " = ", i*j)
    print("\n\n")