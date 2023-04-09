'''
Write a program to print 6 leap years starting from year 2000.
'''
count=0
y=2000
while count!=6:
    if y%4==0 and y%100!=0 or y%400==0:
        print(y)
        count=count+1
    y=y+1
