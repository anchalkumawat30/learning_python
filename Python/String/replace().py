#use replace() function
print("use replace() function")
a = input("Enter a string : ")
b = input("Enter what you want to replace : ")
c = input("Enter with who you want to replace : ")
print(a.replace(b,c))
print("")
# use replace() function with count 
print("use replace() function with count ")
text = "apple apple apple"
print(text.replace("apple","Banana",2))