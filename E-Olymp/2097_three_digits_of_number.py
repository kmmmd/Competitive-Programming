a,b=map(int,input().split())
if 100<=a<=b<=999 :
    for i in range(a,b+1):
        c=i//100
        d=i%10
        k=(i//10)%10
        if c!=k and k!=d and c!=d:
            print(i)