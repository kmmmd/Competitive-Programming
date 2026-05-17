l=list(input())
a,b=map(int,input().split())
y=l[a-1:b]
y.reverse()
l[a-1:b]=y
l="".join(l)
print(l)