n=int(input()) #30%
kok=int(n**(0.5))
kibrit=12
k=n-1
for i in range(3):
    if k>0:
        if i==0 or i==1:
            kibrit+=8
        else:
            kibrit+=5
        k-=1
if n>4:
    say=8
    for i in range(3):
        if k>0:
            k-=1
            if i==0 or i==1:
                say+=5
            else:
                say+=3
    s=n-(int(n/4)*4)
    kibrit+=say*(int(n/4)-1)
    for i in range(s):
        if i==0:
            kibrit+=8
        elif i==1 or i==2:
            kibrit+=5
        else:
            kibrit+=3
print(kibrit) 
