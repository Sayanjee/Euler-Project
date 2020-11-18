Sayan=600851475143
arrS=[]
for i in range(2,Sayan):
    if Sayan%i == 0:
        for j in range(2,i//2):
            if i%j==0:
                break
            else:
                arrS.append(i)
                print(i)
                break
