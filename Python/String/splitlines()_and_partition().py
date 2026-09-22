# use of splitlines() and partition(), rpartition() function
# splitlines() function
print("Use os splitlines() function :- ")
text = "Hello \nPython \nWorld "
print(text.splitlines())
print()
# partition() function
print("Use os partition() function :- ")
text1 = "Anchal is a good girl "
print(text1.partition("is"))
print(text1.partition(" a "))
print()
# rpartition() function
print("Use os rpartition() function :- ")
text2 = "Apple-Banana-orange"
print(text2.rpartition("-"))