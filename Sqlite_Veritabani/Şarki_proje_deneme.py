

from Şarki import *

print("""***************************************

Şarkılar Programına Hoşgeldiniz.

İşlemler:

1. işlem şarkıları goster.

2. işlem  şarkı ekle.

3. işlem şarkı sil.

4. işlem şarkı ara.

q. işlem çıkmak için "q" ya basın

***************************************""")

sarki=Sarkılar()

while True:
    islem=input("Yapmak istediğiniz işlem:")

    if(islem=="q"):
        print("Program sonlandırılıyor...")
        time.sleep(2)
        print("Program sonlandı.")
        break

    elif(islem=="1"):
        print("Şarkılar gösteriliyor...")
        time.sleep(2)
        sarki.sarkilari_goster()

    elif(islem=="2"):
        isim=input("Şarkı ismi:")
        sanatci=input("Sanatçı:")
        album=input("Albüm:")
        prod_sirketi=input("Prodüksiyon şirketi:")
        sarki_suresi=input("Şarkı süresi:")

        muzik=Muzik(isim,sanatci,album,prod_sirketi,sarki_suresi)
        print("Şarkı Ekleniyor...")
        time.sleep(2)
        sarki.sarki_ekle(muzik)
        print("Şarkı eklendi.")

    elif(islem=="3"):
        isim=input("Silinecek şarkı ismi:")
        cevap=input("Emin misiniz? (E/H):")

        if(cevap=="E"):
            print("Şarkı siliniyor...")
            time.sleep(2)
            sarki.sarki_sil(isim)
            print("Şarkı silindi.")

        else:
            print("Şarkı silme işlemi iptal ediliyor...")
            time.sleep(1)
            print("İşlem iptal edildi.")

    elif(islem=="4"):
        isim=input("Sorgulanacak şarkı ismi:")
        print("Şarkı aranıyor...")
        time.sleep(2)
        sarki.sarki_ara(isim)

    else:
        print("Geçersiz işlem!!!")














