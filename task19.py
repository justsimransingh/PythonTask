num=int(input("Enter the number:"))
sum=0
while(num>0):
    d=num%10
    sum+=d
    num//=10
print("Sum of the digits",sum)
