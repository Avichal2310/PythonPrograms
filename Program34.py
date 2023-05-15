"""
WAP to input marks of five subjects. Calculate the average and print the grade based on following
conditions
A+ for average >=80
A for average >=70
B+ for average>=60
B for average>=50
F for others
"""
print("Enter marks of any five subjects : ")
a,b,c,d,e=map(int,input().split())
average=(a+b+c+d+e)/5
print("Average marks are",average)
if average>=80:
    print("Grade is A+")
elif average>=70:
    print("Grade is A")
elif average>=60:
    print("Grade is B+")
elif average>=50:
    print("Grade is B")
else:
    print("Grade is F")
