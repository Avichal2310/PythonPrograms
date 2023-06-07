"""
Write a program to input a number and check it to be an armstrong number. If we break digits of a number, make
cube of each digit and make sum of those cubes. If the sum is equal to real number then it is called
armstrong number. Example:
                    153=1**3+5**3+3**3=1+125+27=153
"""
print("Enter a number : ")
n=int(input())
sum=0
u=n
while u>0:
    digit=u%10
    sum+=digit**3
    u//=10

if n==sum:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")
