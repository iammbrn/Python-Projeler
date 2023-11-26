print("""******************************
Tam Bölenleri Bulma Programı
******************************""")


def Tam_Bol(sayi):
    TamBol_liste = list()
    TamBolmeyen_liste=list()
    for i in range(1,sayi+1):
        if(sayi%i==0):
            TamBol_liste.append(i)
        else:
            TamBolmeyen_liste.append(i)

    print("{}'yı tam bölenlerin listesi={}\n".format(sayi,TamBol_liste))
    print("{}'yı tam bölmeyenlerin listesi={}\n".format(sayi,TamBolmeyen_liste))
while True:
    sayi=input("Sayi:")
    if(sayi=="q"):
        print("Program sonlandırılıyor...")
        break
    else:
        sayi=int(sayi)
        Tam_Bol(sayi)