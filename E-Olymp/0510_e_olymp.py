import math
n, k=map(int, input().split())
if n==0:
    print(0)
else:
    time=max(4,math.ceil((2*n)/k)*2)
    print(time)
