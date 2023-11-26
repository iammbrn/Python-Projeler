



sayi=int(input("Faktöryeli alınacak sayiyi giriniz:"))
faktoriyel=1
for i in range(sayi,1,-1):
        faktoriyel*=i
print("{}! faktoriyel={}".format(sayi,faktoriyel))



while True:
    sayi=input("Faktöryeli alınacak sayiyi giriniz:")
    if(sayi=="q"):
        print("Program sonlandırılıyor...")
        break
    else:
        sayi=int(sayi)
        faktoriyel = 1
        for i in range(2,sayi+1):
            faktoriyel*=i
        print("{}! faktoriyel={}".format(sayi, faktoriyel))