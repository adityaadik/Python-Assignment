#Write a python program to find armstrong number in an interval.

a=int(input("Starting number::"))
b=int(input("Ending number::"))
for i in range(a,b):
    n=i
    s=0
    while(n>0):
        d=n%10
    n=int(n/10)
    s=st(d*d*d)
    if(s==i):
        print(i)
