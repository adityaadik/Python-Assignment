#Write a programe to print all prime numberas is an interval.

a=int(input("Enter the Starting intervel::"))
b=int(input("Enter the Ending number::"))
for n in range(a,b):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
        break
    if(flag==0):
        print(n)
