a=int(input())
a=str(a)
c=list(map(str,list(a)))
d=c[ : :-1]
if c==d:
    print('Yes')
else:
    print('No')