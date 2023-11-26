from Kutuphane import*

print("""***************************************

Kütüphane Programına Hoşgeldiniz.

İşlemler:

1. işlem kitapları goster.

2. işlem kitapları sorgula.

3. işlem kitap ekle.

4. işlem kitap sil.

5. işlem baskı yükselt.

6. işlem kitap ödünç ver.

7. işlem kitap iade et.

q. işlem çıkmak için "q" ya basın

***************************************""")
kutuphane=Kutuphane()

while True:
    islem=input("işlem:")
    if(islem=="q"):
        print("Program sonlandırılıyor...")
        time.sleep(1)
        print("Program sonlandı.")
        break

    elif(islem=="1"):
        kutuphane.kitaplari_goster()

    elif(islem=="2"):
        isim=input("Sorgulanan kitap ismi:")
        print("Kitap sorgulanıyor...")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)
        print("Kitap bulundu.")


    elif(islem=="3"):
        isim=input("Kitap ismi:")
        yazar=input("Yazar:")
        yayinevi=input("Yayınevi:")
        tur=input("Tür:")
        baski=int(input("Baskı:"))
        mevcut=int(input("Mevcut Adet:"))
        yeni_kitap=Kitap(isim,yazar,yayinevi,tur,baski,mevcut)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi.")

    elif(islem=="4"):
        isim=input("Silinecek kitap ismi:")
        cevap = input("Emin misiniz ? (E/H) :")
        if(cevap=="E"):
            print("Kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi.")
        else:
            print("İşlem iptal ediliyor...")
            time.sleep(1)
            print("İşlem iptal edildi.")

    elif(islem=="5"):
        isim=input("Hangi kitabın baskısı?:")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baskı yükseltildi.")

    elif(islem=="6"):
        isim=input("Ödünç alınacak kitap ismi:")
        print("Ödünç veriliyor...")
        time.sleep(2)
        kutuphane.kitap_odunc_ver(isim)
        print("Kitap ödünç verildi.")
    elif(islem=="7"):
        isim=input("İade alınacak kitap ismi:")
        print("İade ediliyor...")
        time.sleep(2)
        kutuphane.kitap_iade_et(isim)
        print("Kitap iade edildi.")
    else:
        print("Geçersiz işlem!!!")

















