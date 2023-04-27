'''
Write a program to input two numbers.If first number is bigger than second
number, interchange them and print all armstrong numbers in given range.
'''
print("Enter two numbers")
n1=int(input())
n2=int(input())
if n1>n2:
    t=n1
    n1=n2
for n in range(n1,n2+1):
    sum=0
    u=n
    while u>0:
        digit=u%10
        sum=sum+digit**3
        u=u//10
    if n==sum:
        print(n)
