#Write a python programme to find the factorial of number
num=int(input("Enter the Number::"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial=",fact)
