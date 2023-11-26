import time
class Dosya():

    def __init__(self):

        with open("Metin1.txt","r",encoding="utf-8") as file:

            dosya_icerigi = file.read()

            kelimeler=list()

            kelimeler=dosya_icerigi.split()

            self.sade_kelimeler=list()

            for i in kelimeler:

                i.strip("\n")
                i.strip(" ")
                i.strip(".")
                i.strip(",")
                self.sade_kelimeler.append(i)


    def tum_kelimeler(self):
        kelimeler_kumesi=set()

        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)

        print("Kelimeler Kümesi.....")

        for i in kelimeler_kumesi:
            print(i)
            print("********************")


    def kelimeler_adedi(self):

        sozluk=dict()

        for i in self.sade_kelimeler:
            if(i in sozluk):
                sozluk[i]+=1
            else:
                sozluk[i]=1

        for kelime,adet in sozluk.items():

            print("{} kelimesi {} defa geçiyor....".format(kelime,adet))

            print("--------------------------------------------------")

    def kelime(self,aranacak_kelime):
        kelime_adet=0
        for i in self.sade_kelimeler:
            if(not(aranacak_kelime in self.sade_kelimeler)):
                print("Aradığınız kelime bulunmuyor!!!")
                break

            elif(aranacak_kelime in self.sade_kelimeler):
                if(aranacak_kelime==i):
                    kelime_adet += 1

        print("Aradığınız kelime: {} kelimesi metinde {} adet bulunuyor.".format(aranacak_kelime,kelime_adet))






dosya = Dosya()

print("""**************************************************

Dosya işlemleri:

1. Kelimeler kümesi

2. Kelimeler frekansı(adedi)

3. Aranan kelime adedi

q Programı sonlandır.
**************************************************""")


while True:
    islem=input("İşlem:")

    if(islem=="q"):
        print("Program sonlandırılıyor...")
        time.sleep(1)
        print("Program sonlandı.")
        break

    elif(islem=="1"):
        dosya.tum_kelimeler()

    elif(islem=="2"):
        dosya.kelimeler_adedi()

    elif(islem=="3"):
        kelime1=input("Aranacak kelime:")
        dosya.kelime(kelime1)



