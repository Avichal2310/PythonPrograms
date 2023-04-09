''' 
WAP to input a number from user and check it to be a prime number.
'''
print("Enter a number")
n=int(input())
cut=False
for m in range(2,n):
    if n%m==0:
        cut=True
        break
if cut==False:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")    
