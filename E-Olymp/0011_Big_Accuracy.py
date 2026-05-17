m,n,k=map(int,input().split())
tambolme=m//n
qaliq=m%n
kesr=str(tambolme)+"."
for i in range(k):
    qaliq*=10
    kesrd=qaliq//n
    kesr+=str(kesrd)
    qaliq%=n
print(kesr)
