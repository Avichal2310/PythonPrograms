"""
WAP to show the sum of following series:
            1+x/2+x**2/3+x**3/4+x**n-1/n
"""
print("Enter value of x with power of x :")
x,n=map(int,input().split())
sum=0
for i in range(n):
    term=x**i/(i+1)
    sum+=term
print("Sum of the series:", sum)
