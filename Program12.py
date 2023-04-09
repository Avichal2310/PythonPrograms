'''
Write a program to input shopping amount of a person along with his/her gender.
Calculate the discount based on the following rules:-
                Shopping amount>=20000 and female
                Discount=30%
                Shopping amount>=20000 and male 
                Discount=20%
                Shopping amount>=10000 and female
                Discount=15%
                Shopping amount>=10000 and male
                Discount=10%
                0 Discount for others.
'''
print("Enter shopping amount")
s=int(input())
print("Enter your gender male or female")
g=input()
if s>=20000 and g=='female':
    discount=s*30/100
elif s>=20000 and g=='male':
    discount=s*20/100
elif s>=10000 and g=='female':
    discount=s*15/100
elif s>=10000 and g== 'male':
    discount=s*10/100
else:
    discount=0
    
print("Your discount is ",discount)
print("Your payable amount is",s-discount)
