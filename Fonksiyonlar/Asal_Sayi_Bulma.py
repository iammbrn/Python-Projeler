"""
Asal Sayilar 1'e ve kendisinden başka sayıya bölünmeyen sayilardir.
"""
print("""*************************
Asal Sayı Bulma Programı
*************************""")

def Asal_Sayi(x):
    if(x==2):
        print("{} sayisi asal sayidir.\n".format(x))
    elif(x>2):
        for i in range(2,x):
            asal=True
            if(x%i==0):
                asal=False
                print("{} sayisi asal sayi değildir.\n".format(x))
                break

        if(asal):
            print("{} sayisi asal sayidir.\n".format(x))

    else:
        print("{} sayisi asal sayi değildir.\n".format(x))

while True:
    x = input("x:")
    if(x=="q"):
        print("Program sonlandırılıyor...\n")
        break
    else:
        Asal_Sayi(int(x))


print("""*************************
Asal Sayı Bulma Programı 2
*************************""")

def asal_bulma(sayi):
    if(sayi==1):
        return False
    elif(sayi==2):
        return True
    else:
        for i in range(2,sayi):
            if(sayi%i==0):
                return False
        return True

while True:
    sayi=input("sayi:")
    if(sayi=="q"):
        print("Program sonlandırılıyor...\n")
        break
    else:
        sayi=int(sayi)

        if(asal_bulma(sayi)):
            print(sayi,"Asal bir sayidir.")
        else:
            print(sayi, "Asal bir sayi değildir.")


