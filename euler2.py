arrSayan=[]
arrBan=[]
a=1
b=2
while (a<4000000):
    arrSayan.append(a)
    temp = a
    a = b
    b = a + temp
for i in arrSayan:
    if i%2==0:
        arrBan.append(i)
        
        
print(sum(arrBan))
