'''
Write a program that checks whether a given number is a palindrome or not.
'''
print("Enter a number")
n=int(input())
reverse=0
x=n
while n>0:
    reverse=(reverse*10)+n%10
    n=n//10
if x==reverse:
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")
