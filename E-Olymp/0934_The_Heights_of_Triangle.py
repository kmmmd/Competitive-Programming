a,b,c=map(int,input().split())
p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))**0.5
ha=2*s/a
hb=2*s/b
hc=2*s/c
print(ha,hb,hc)
