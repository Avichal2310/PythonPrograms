'''
Write a program to input marks for Hindi,English,Sanskrit,Science and Maths.
Calculate average marks.Show the grade of the student based on following rules:-
                       Grade A+ for average >=90
                       Grade A for average >=80
                       Grade B+ for average >=70
                       Grade B for average >=60
                       Grade C for average >=50
                       Grade F for others
'''
print("Enter marks for Hindi")
h=int(input())
print("Enter marks for English")
e=int(input())
print("Enter marks for Sanskrit")
s=int(input())
print("Enter marks for Science")
c=int(input())
print("Enter marks for Maths")
m=int(input())
average=(h+e+s+c+m)/5
print("Average marks are",average)
if average>=90:
    print("Grade is A+")
elif average>=80:
    print("Grade is A")
elif average>=70:
    print("Grade is B+")
elif average>=60:
    print("Grade is B")
elif average>=50:
    print("Grade is C")
else:
    print("Grade is F")
