a,b=map(int,input().split())
x=0
while (a+x)%b!=0 or (b+x)%a!=0:
    x+=1
print(x)
#     42/100

import math
def funk(a,b):
    if a==b:
        return 0
    ortaq=math.gcd(a,b)
    a//=ortaq
    b//=ortaq
    if a==1:
        x=ortaq*(b-1)
    elif b%a==0:
        x=b-a
    else:
        x=ortaq*((a-1)*b-a)
        
    return x
a,b=map(int,input().split())
if a>b:
    c=a
    a=b
    b=c
print(funk(a,b))

# 100 PERCENT TRUE!!!!