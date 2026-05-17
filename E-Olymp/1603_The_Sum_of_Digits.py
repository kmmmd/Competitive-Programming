a=int(input())
a=abs(a)
s=0
while a>0:
    x=a%10
    s=s+x
    a=a//10
print(s)