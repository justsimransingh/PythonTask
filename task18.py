num=int(input("Enter three digit number:"))
l=[]
while(num>0):
    x=num%10
    num=num//10
    l.append(x)
print("All possible combinations can be:")
r=range(3)
for i in r:
    for j in r:
        for k in r:
            if (i!=j and k!=i and k!=j):
                print(l[i],l[j],l[k],sep="")
