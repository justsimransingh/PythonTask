num=int(input("Enter the integer:"))
x=num
print("Divisors of",num,"are:")
for i in range(2,x):
    if num%i==0:
        print(i)
