'''
s=input("Enter String:")
z=set(s)
for i in z:
    print(i,s.count(i))
'''

s=input("Enter String:")
s=s.upper()
d={}
l=[]
for i in s:
    if i not in l:
        l.append(i)
for i in l:
    d[i]=s.count(i)
print(d)
