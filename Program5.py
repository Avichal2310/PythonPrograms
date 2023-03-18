'''
If a book is purchased of $300 and sold for $425 then how much profit is gained 
and in what percentage?

Hint=use formula profit=sp-cp and profit/cp*100
'''
print("Enter the cost price")
cp=int(input())
print("Enter the selling price")
sp=int(input())
p=sp-cp
print("Profit is",p)
result=p/cp*100
print("Profit percentage is",result)
