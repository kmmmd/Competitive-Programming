#17 saniye
m,n=map(int,input().split())
netice=[]
l = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    for j in range(1,n):
        if i>0:
            l[i][0]=l[i-1][0]+l[i][0]
            break
        else:
            l[i][j]=l[i][j]+l[i][j-1]
for i in range(1,m):
    for j in range(1,n):
        l[i][j]=l[i-1][j]+l[i][j-1]-l[i-1][j-1]+l[i][j]
for setir in l:
    print(" ".join(map(str,setir)))




#easy wayyyy 14 san vaxt limiti asir
m, n = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
s = [[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        s[i][j] = l[i][j]
        if i > 0:
            s[i][j] += s[i-1][j]
        if j > 0:
            s[i][j] += s[i][j-1]
        if i > 0 and j > 0:
            s[i][j] -= s[i-1][j-1]
for row in s:
    print(" ".join(map(str, row)))
