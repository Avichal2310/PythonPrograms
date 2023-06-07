"""
Write a program to input two numbers and print all armstrong numbers in given range of values.
"""
print("Enter two numbers : ")
n,m=map(int, input().split())
for b in range(n,m+1):
    sum=0
    u=b
    while u>0:
        digit=u%10
        sum+=digit**3
        u//=10
    if b==sum:
        print(b)
