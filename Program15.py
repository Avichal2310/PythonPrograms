'''
WAP to print all the numbers between 1 and 100.If you find a number that  is 
divisible by 5 and 7 then skip that number.
'''
n=1
while n<=100:
    if n%5==0 and n%7==0:
        n=n+1
        continue
    print(n)
    n=n+1
