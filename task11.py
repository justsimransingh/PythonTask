r=int(input("Enter the range upto which you want to print series:"))
x,y,a=0,1,0
print(x,y,sep="\n")
while(a<r):
    z=x+y
    print(z)
    x,y=y,z
    a+=1
