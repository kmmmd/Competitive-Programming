def rum(n): #100% TRUE !!!
    n=''.join(n)
    values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbols=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    eded=0
    i=0
    length=len(n)
    while i<length:
        for j in range(len(symbols)):
            if n.find(symbols[j],i)==i:
                eded+=values[j]
                i+=len(symbols[j])
                break
    return eded
def eded(m):
    values = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
    symbols = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    roma= []
    i = 0
    while m>0:
        while m>=values[i]:
            roma.append(symbols[i])
            m-=values[i]
        i += 1
    return ''.join(roma)
setir = input()
daxil= list(setir)
uz=len(daxil)
a=[]
b=[]
for i in range(uz):
    if daxil[i]!="+":
        a.append(daxil[i])
    else:
        breqemi=i+1
        break
for i in range(breqemi,uz):
    b.append(daxil[i])
cem=rum(a)+rum(b)
print(eded(cem))  
