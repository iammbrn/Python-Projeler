import random


class hayvan():

    def __init__(self, isim="Bilgi yok", hayvanlar=["At", "Kopek", "Kus"], cins="Bilgi yok", cinsler=["Erkek","Dişi"], ayak=0, ayak_sayisi=[2, 4]):
        self.isim = isim
        self.hayvanlar = hayvanlar
        self.cins = cins
        self.cinsler = cinsler
        self.ayak = ayak
        self.ayak_sayisi = ayak_sayisi


class hayvanlar(hayvan):

    def __init__(self, isim="Bilgi yok", hayvanlar=["At", "Kopek", "Kus"], cins="Bilgi yok", cinsler=["Erkek", "Dişi"],ayak=0, ayak_sayisi=[2, 4], hareket_tipi="Bilgi yok"):
        super().__init__(isim, hayvanlar, cins, cinsler, ayak, ayak_sayisi)
        self.hareket_tipi = hareket_tipi

    def bilgileri_goster(self):
        print("""
        ********************
        Hayvan Sınıfı:

        İsim:{}

        Cins:{}

        Ayak sayısı:{}

        Hareket tipi:{}
        ********************""".format(self.isim, self.cins, self.ayak, self.hareket_tipi))

    def hayvan_sec(self):
        rastgele = random.randint(0, len(self.hayvanlar) - 1)
        self.isim = self.hayvanlar[rastgele]

    def cins_sec(self):
        rastgele = random.randint(0, len(self.cinsler) - 1)
        self.cins = self.cinsler[rastgele]

    def ayak_bul(self):
        if (self.isim == "Kopek" or self.isim == "At"):
            self.ayak = 4
        elif (self.isim == "Kus"):
            self.ayak = 2

    def hareket(self):
        if (self.isim == "Kopek" or self.isim == "At"):
            self.hareket_tipi = "Yürüme"
        elif (self.isim == "Kus"):
            self.hareket_tipi = "Uçma"

    def __len__(self):
        return len(self.ayak)

    def __str__(self):
        return "Hayvan: {}\nCins: {}\nAyak Sayısı: {}\nHareket Tipi: {}".format(self.isim, self.cins, self.ayak,self.hareket_tipi)

    def __del__(self):
        print("Seçilen obje siliniyor...")


hayvan1 = hayvanlar()

print("""
İşlemler:

1.işlem: Hayvan_sec

2.işlem: Cins_sec

3.işlem: Ayak sayısını bul

4.işlem: Hareket tipi

5.işlem: Bilgileri göster

6.işlem: Str metodu

7.işlem: Del metodu""")

while True:
    islem = input("islem sec:")
    if (islem == "q"):
        print("Programı sonlandırılıyor...")
        break
    elif (islem == "1"):
        hayvan1.hayvan_sec()
    elif (islem == "2"):
        hayvan1.cins_sec()
    elif (islem == "3"):
        hayvan1.ayak_bul()
    elif (islem == "4"):
        hayvan1.hareket()
    elif (islem == "5"):
        hayvan1.bilgileri_goster()
    elif (islem == "6"):
        print(hayvan1)
    elif (islem == "7"):
        del hayvan1
    else:
        print("Geçersiz işlem!!!")



