'''
WAP to print all the numbers between 1 and 100.If you find a number that  is 
divisible by 5 and 7 stop the printing.
'''
n=1
while n<=100:
    if n%5==0 and n%7==0:
        break
    print(n)
    n=n+1
