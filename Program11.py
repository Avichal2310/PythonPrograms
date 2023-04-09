'''
Write a program to input a year and check it to be a leap year.
Hint=A year divisible by 4 but not divisible by 100 or divisible by 400 is a 
leap year.
'''
print("Enter a year")
y=int(input())
if y%4==0 and y%100!=0 or y%400==0:
    print(y,"is a leap year")
else:
    print(y,"is not a leap year")
