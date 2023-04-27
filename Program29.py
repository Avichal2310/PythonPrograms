'''
Write a program  all armstrong numbers between 1 and 1000.
'''
for n in range(1,1001):
    sum=0
    u=n
    while u>0:
        digit=u%10
        sum=sum+digit**3
        u=u//10
    if n==sum:
        print(n)
