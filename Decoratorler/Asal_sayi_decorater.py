def fonksiyon(func):

    def wrapper(sayilar):

        print("Mükemmel sayilar...")

        for sayi in sayilar:
            toplam=0
            for i in range(1,sayi):
                if(sayi%i==0):
                    toplam+=i
            if(toplam==sayi):
                print(sayi)

        func(sayilar)
    return wrapper



@fonksiyon
def asal_bulma(sayilar):
    print("Asal sayilar....")
    for sayi in sayilar:
        if(sayi<2):
            continue
        elif(sayi==2):
            print(sayi)
        else:
            asal=True
            for i in range(2,sayi):
                if(sayi%i==0):
                    asal=False
                    break
            if(asal):
                print(sayi)
asal_bulma((range(1,1001)))



