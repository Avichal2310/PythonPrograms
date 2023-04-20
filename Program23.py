'''
Write a program to input a string and print alphabets, digits and special 
characters.
'''
print("Enter a string")
string=input()
a=[]
d=[]
s=[]
for ch in string:
    if ch.isalpha():
        a.append(ch)
    elif  ch.isdigit():
        d.append(ch)
    else:
        s.append(ch)
print("Alphabets are",a)
print("Digits are",d)
print("Special Characters are",s)
