"""
WAP to input a string and check it to be palindrome.
"""
print("Enter a string : ")
s=input()
if s==s[::-1]:
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")
