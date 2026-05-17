def qazanan(p):
    say={}
    qalib=""
    xal=-1
    for ad,eded in p:
        if ad in say:
            say[ad]+=eded
        else:
            say[ad]=eded
        if say[ad]>xal:
            qalib=ad
            xal=say[ad]
    return qalib
n=int(input())
l=[]
for i in range(n):
    k=input()
    ad,eded=k.split()
    eded=int(eded)
    l.append((ad,eded))
print(qazanan(l))