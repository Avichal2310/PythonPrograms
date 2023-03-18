'''
Write a program to input principal amount, rate of interest and no. of years to 
deposit amount in a bank.How much total amount bank will return after completion
of the period?(In compound interest)
Hint=use formula (p*(1+r/100)**t)-p and p+i
'''
print("Enter the principal amount")
p=int(input())
print("Enter the rate of interest")
r=int(input())
print("Enter the number of years")
t=int(input())
i=(p*(1+r/100)**t)-p
print("Amount deposited in bank is",i)
result=p+i
print("Total amount bank will return after completion of period is",result)
