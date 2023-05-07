"""
Write a program to input the principal amount,rate of interest and number of years to deposit the amount in a
bank.Calculate the interest for given period based on simple interest and compound interest.Show the output
in the following format:
The simple interest will be {si} and compound interest will be {ci} for the amount {pa} with the rate {rate}
for the period {period}.
"""
print("Enter principal amount,rate of interest and number of years to deposit amount in bank : ")
pa,rate,period=map(int,input().split())
si=pa*rate*period/100
ci=pa*(1+rate/100)**period-pa
print(f"The simple interest will be {si} and compound interest will be {ci} for the amount {pa} with the rate {rate} "
      f"for the period {period}")
