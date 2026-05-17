n=int(input())
kok=int(n**(1/2))
s=2*kok*(kok+1)
for i in range(n-kok**2):
    if i==0 or i==kok:
        s+=3
    else:
        s+=2
print(s)
