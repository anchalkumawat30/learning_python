#use split() function
print("Use split() function :- ")
a = input("Enter a sting to split it : ")
print(a.split())
print()
#use split() function with seprator
print("use split() function with seprator :- ")
b = input("Enter a string with seprator to split it : ")
print(b.split(","))
print()
#use split() function with maxsplit 
# Maxsplit specifies the maximum number of split 
print("use split() function with maxsplit :- ")
c = input("Enter a string ")
d = int(input("Enter a number to split "))
print(c.split(" ",d))
print("\n")
#use join() function
print("Use of join() function :- ")
text = ["python","is","easy"]
print(" ".join(text))
print()
#use join() using "-"
print("use join() using (-)")
word = ['2026','09','05']
print("-".join(word))