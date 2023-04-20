'''
Write a program to input a string and print count of alphabets, digits and 
special characters in that string.
'''
print("Enter a string")
string=input()
alphabets=digits=special=0
for ch in string:
    if ch.isalpha():
        alphabets=alphabets+1
    elif  ch.isdigit():
        digits=digits+1
    else:
        special=special+1        
print("Total Number of Alphabets in this string are",alphabets)
print("Total Number of Digits in this string are",digits)
print("Total Number of Special Characters in this string are",special)
