'''
WAP to input two numbers and print all prime numbers in range.
'''
print("Enter two numbers")
n1=int(input())
n2=int(input())
for n in range(n1,n2+1):
    cut=False
    for m in range(2,n):
        if n%m==0:
            cut=True
            break
    if cut==False: print(n)
