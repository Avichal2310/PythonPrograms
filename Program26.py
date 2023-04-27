'''
Write a program that prints the first n terms of the Fibonacci sequence.
'''
print("Enter a number of terms in seqeunce")
n=int(input())
a,b=0,1
for s in range(n):
    print(a,end=' ')
    a,b=b,a+b
