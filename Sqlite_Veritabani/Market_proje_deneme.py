from Market import *

print("""***************************************

Market Programına Hoşgeldiniz.

İşlemler:

1. işlem ürünleri goster.

2. işlem ürün ekle.

3. işlem ürün sil.

4. işlem ürün ara.

q. işlem çıkmak için "q" ya basın

***************************************""")

market=Market()

while True:

    islem=input("Yapmak istediğiniz işlem:")

    if(islem.lower()=="q"):
        print("Program sonlandırılıyor...")
        time.sleep(2)
        print("Program sonlandı.")
        break

    elif(islem=="1"):
        print("Ürünler gösteriliyor...\n")
        time.sleep(2)
        market.urunleri_goster()

    elif(islem=="2"):
        print("***Eklencek ürün bilgileri***")
        isim=input("İsim:")
        fiyat=input("Fiyat:")
        urun=Urun(isim,fiyat)
        print("Ürün ekleniyor...")
        time.sleep(2)
        market.urun_ekle(urun)
        print("Ürün eklendi.")

    elif(islem=="3"):
        urun=input("Silinecek ürün:")
        cevap=input("Emin misiniz? (E/H):")

        if(cevap.lower()=="e"):
            print("Ürün siliniyor...")
            time.sleep(2)
            market.urun_sil(urun)
            print("Ürün silindi.")
        else:
            print("Ürün silme işlemi iptal ediliyor...")
            time.sleep(1)
            print("İşlem iptal edildi.")


    elif(islem=="4"):
        urun=input("Aranacak ürün:")
        print("Ürün aranıyor...\n")
        time.sleep(2)
        market.urun_sorgula(urun)

    else:
        print("Geçersiz işlem!!!")

