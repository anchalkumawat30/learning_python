#First Non-Repeating Character: Find the first character in a string that doesn't repeat anywhere else.
def non_repeating(s):
    for char in s :
        count = 0
        for ch in s : 
            if ch == char:
                count += 1
            
        if count == 1:
            print(char)
            return char
                
    print ("none")
    return None
       
s = input ("Enter a string : ")
non_repeating(s)