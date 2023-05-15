"""
WAP to input two numbers and print the greater one. If both are equal then print “equal”
"""
print("Enter two numbers : ")
a,b=map(int,input().split())
if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print("Equal")
