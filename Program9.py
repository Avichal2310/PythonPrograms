'''
Write a program to input a number and print the message based on number
                      NEGATIVE NUMBER=<0
                      LESS THAN 10=0 TO 9
                      LESS THAN 100=10 TO 99
                      LESS THAN 1000=100 TO 999
                      MORE THAN 1000=1000+
'''
print("Enter a number")
n=int(input())
if n<0:
    print(n,"is negative number")
elif n<=9:
    print(n,"is less than 10")
elif n<=99:
    print(n,"is less than 100")
elif n<=999:
    print(n,"is less than 1000")
elif n>=1000:
    print(n,"is greater than 1000")
