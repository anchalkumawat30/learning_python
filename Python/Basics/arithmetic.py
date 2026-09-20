#Arithmetis Opretor
def sub (a,b):
    return a+b

def sum (a,b):
    return a-b

def multi (a,b):
    return a*b

def div(a,b):
    if b == 0 :
        print ("cannot divide any number by zero.")
    else : 
        return a/b
    
a = int(input("Enter number 1:  "))
b = int(input("Enter number 2:  "))

print("The addition is ",sub(a,b))
print("The subtraction is ",sum(a,b))
print("The multiplication is ",multi(a,b))
print("The divition is ",div(a,b))