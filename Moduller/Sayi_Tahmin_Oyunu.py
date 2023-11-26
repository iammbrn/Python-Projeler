import random
import time

print("""*************************

Sayı Tahmin Oyunu

1 ile 40 arasında sayıyı tahmin edin.

*************************""")

rastgele_sayi=random.randint(1,40)

tahmin_Hakki=7

while True:
    tahmin=int(input("Tahmininiz:"))

    if(tahmin==rastgele_sayi):
        print("Kontrol Ediliyor...")
        time.sleep(1)
        print("Tebrikler doğru tahmin ettiniz sayimiz=",rastgele_sayi)
        break
    elif(tahmin>rastgele_sayi):
        print("Kontrol Ediliyor...")
        time.sleep(1)
        print("Lütfen daha küçük bir sayı tahmin edin.")
        tahmin_Hakki-=1
    else:
        print("Kontrol Ediliyor...")
        time.sleep(1)
        print("Lütfen daha büyük bir sayı tahmin edin.")
        tahmin_Hakki-=1
    if(tahmin_Hakki==0):
        print("Tahmin hakkınız bitti!!!")
        print("Sayımız=",rastgele_sayi)
        break