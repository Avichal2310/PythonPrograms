'''
Write a program to input a number and check it to be armstrong number.
'''
print("Enter a number")
n=int(input())
sum=0
u=n
while u>0:
    digit=u%10
    sum=sum+digit**3
    u=u//10
if n==sum:
    print(n,"is a armstrong number")
else:
    print(n,"is not a armstrong number")
