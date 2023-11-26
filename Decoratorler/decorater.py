def decorater(fonk):

    def wrapper(sayilar):
        tek_sayilarin_top=0
        tek_sayilarin_sayisi=0
        çift_sayilarin_top=0
        çift_sayilarin_sayisi=0

        for i in sayilar:

            if(i%2==0):
                çift_sayilarin_top+=i
                çift_sayilarin_sayisi+=1

            else:
                tek_sayilarin_top+=i
                tek_sayilarin_sayisi+=1


        print("Teklerin ortalaması:",tek_sayilarin_top/tek_sayilarin_sayisi)
        print("Çiftlerin ortalaması:",çift_sayilarin_top/çift_sayilarin_sayisi)

        fonk(sayilar)


    return wrapper

@decorater
def ort_bul(sayilar):
    toplam=0
    for i in sayilar:
        toplam+=i
    ort=toplam/len(sayilar)
    print("Genel ortalam:",ort)

ort_bul([1,2,3,4,34,60,63,32,100,105])