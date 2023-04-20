'''
Write a program to input a number and print sum of its digits.
'''
print("Enter a number")
n=int(input())
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print("Sum of number is",sum)
