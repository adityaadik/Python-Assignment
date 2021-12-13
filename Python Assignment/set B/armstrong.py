num=int(input("Enter the Number:"))
sum=0
num1=num
while(num1>0):
    d=num1%10
num1=int(num1/10)
 sum=sum+d*d*d
if(num==sum):
    print("Number is Armstrong::")
else:
    print("Number is not Armstrong::")
    
