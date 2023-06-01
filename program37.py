"""
WAP to show the sum of following series:
                   x+x**2+x**n
"""
print("Enter value of x with power of x :")
x,n=map(int,input().split())
sum=0
i=1
while i<=n:
        term=x**i
        sum+=term
        i+=1
print("Sum of the following series : ", sum)
