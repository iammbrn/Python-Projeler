import time
import random


class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Baran"],kanal="Baran"):

        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_ac(self):
        if(self.tv_durum=="Açık"):
            print("Tv zaten açık.")
        else:
            print("Tv açılıyor...")
            time.sleep(1)
            self.tv_durum="Açık"

    def tv_kapat(self):
        if(self.tv_durum=="Kapalı"):
            print("Tv zaten kapalı")
        else:
            print("Tv kapatılıyor...")
            time.sleep(1)
            self.tv_durum="Kapalı"

    def tv_ses_ayarlari(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış : çıkış=")

            if(cevap=="<"):
                if(self.tv_ses!=0):
                    self.tv_ses-=1
                    print("Ses=",self.tv_ses)
            elif(cevap==">"):
                if(self.tv_ses<30):
                    self.tv_ses+=1
                    print("Ses=",self.tv_ses)
            else:
                print("Ses güncellendi=",self.tv_ses)
                break


    def kanal_ekleme(self,Kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(Kanal_ismi)
        print("Kanal eklendi.")


    def kanal_silme(self,kanal_ismi):
        print("Kanal siliniyor...")
        time.sleep(1)
        self.kanal_listesi.remove(kanal_ismi)
        if(kanal_ismi==self.kanal):
            self.kanal="Bu kanal silindi"
        print("Kanal silindi")


    def rastgele_kanal_seçme(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Aktif kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):

        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal:{}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)



kumanda=Kumanda()


print("""

Televizyon Uygulaması


1. Tv Aç

2. Tv Kapat

3. Ses Ayarları

4. Kanal Ekle

5. Kanal Silme

6. Kanal Sayısını Öğrenme

7. Rastgele Kanala Geçme

8. Televizyon Bilgileri

Çıkmak için 'q' ya basın.
""")

while True:
    islem=input("islem:")

    if(islem=="q"):
        print("Program sonlandırılıyor...")
        break

    elif(islem=="1"):
        kumanda.tv_ac()

    elif(islem=="2"):
        kumanda.tv_kapat()

    elif(islem=="3"):
        kumanda.tv_ses_ayarlari()

    elif(islem=="4"):
        kanal_isimleri=input("Kanal isimlerini ',' ile ayırarak girin:")

        kanal_listesi=kanal_isimleri.split(",")

        for  eklenecekler in kanal_listesi:
            kumanda.kanal_ekleme(eklenecekler)

    elif(islem=="5"):
        kanal_isimleri=input("Kanal isimlerini ',' ile ayırarak girin:")

        kanal_listesi=kanal_isimleri.split(",")

        for silinecekler in kanal_listesi:
            kumanda.kanal_silme(silinecekler)
    elif(islem=="6"):
        print("Kanal sayısı=",len(kumanda))

    elif(islem=="7"):
        kumanda.rastgele_kanal_seçme()

    elif(islem=="8"):
        print(kumanda)

    else:
        print("Geçersiz işlem!!!")


