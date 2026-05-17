a=int(input())
s=1
for i in range(a):
    if a>0:
        x=a%10
        a=a//10
        s=s*x
print(s)
