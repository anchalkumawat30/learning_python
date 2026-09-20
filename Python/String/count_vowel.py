#Vowel Counter: Write a function that takes a string and returns the number of vowels (a, e, i, o, u) inside it, ignoring case.
def str1(s):
    count = 0
    s = s.lower()
    for char in s :
        if char in "aeiou":
            count +=1
    print("The count is ", count)
    return count 
            
s = input("Enter a string: ")
str1(s)
print(s)