import random

import time


class Bilgisayar():

    def __init__(self,Markalar=["MSI","Apple","Asus","Abc"],Marka="Bilgi Yok",Ramlar = ["8 GB ","16 GB","32 GB"],Ram = "Bilgi Yok",Ekran_kartlari = ["2 GB","4 GB","6 GB"],Ekran_karti = "Bilgi Yok",Sdd_ler = ["256 GB","512 GB","1 TB"],Sdd = "Bilgi Yok", Fiyat=0):

        self.Markalar = Markalar
        self.Marka = Marka
        self.Ramlar = Ramlar
        self.Ram = Ram
        self.Ekran_kartlari = Ekran_kartlari
        self.Ekran_karti = Ekran_karti
        self.Sdd_ler = Sdd_ler
        self.Sdd = Sdd
        self.Fiyat = Fiyat




    def Marka_sec(self):
        Rastgele = random.randint(0,len(self.Markalar)-1)
        self.Marka=self.Markalar[Rastgele]
        print("Marka:",self.Marka)

    def Ram_sec(self):
        rastgele=random.randint(0,len(self.Ramlar)-1)
        self.Ram=self.Ramlar[rastgele]
        print("Ram:",self.Ram)

    def Ekran_karti_sec(self):
        rastgele=random.randint(0,len(self.Ekran_kartlari)-1)
        self.Ekran_karti=self.Ekran_kartlari[rastgele]
        print("Ekran Kartı:",self.Ekran_karti)

    def Sdd_sec(self):
        rastgele=random.randint(0,len(self.Sdd_ler)-1)
        self.Sdd=self.Sdd_ler[rastgele]
        print("SDD:",self.Sdd)

    def Fiyat_belirleme(self):

        if(self.Marka=="Apple"):
            if(self.Ram == "32 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "100.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "90.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd,self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "90.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd,self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "90.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))


        elif(self.Marka=="MSI"):
            if (self.Ram == "32 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "90.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "30.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))

        elif(self.Marka=="Asus"):
            if (self.Ram == "32 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "80.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "32 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "70.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "50.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "16 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "30.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "60.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "6 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "4 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "30.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "1 TB"):
                self.Fiyat = "40.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "512 GB"):
                self.Fiyat = "30.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
            elif (self.Ram == "8 GB" and self.Ekran_karti == "2 GB" and self.Sdd == "256 GB"):
                self.Fiyat = "20.000 Tl"
                print("{} {} Ram {} Ekran kartı {} SDD Fiyat:{}".format(self.Marka,self.Ram,self.Ekran_karti,self.Sdd, self.Fiyat))
        else:
            self.Fiyat="15.000 Tl - 25.000 Tl arası "
            print("{} Fiyat:{}".format(self.Marka,self.Fiyat))


    def Bilgileri_goster(self):

        print("\n\n***************\nMarka:{}\nRam:{}\nEkran kartı:{}\nSDD:{}\nFiyat:{}\n***************".format(self.Marka, self.Ram, self.Ekran_karti,self.Sdd, self.Fiyat))



Laptop=Bilgisayar()

print("Bilgisayar secme programı\nİşlemler:\n1.Marka seç\n2.Ram seç\n3.Ekran kartı seç\n4.SDD seç\n5.Fiyat Guncelle\n6.Bilgiler")


while True:
    islem=input("islem gir:")

    if(islem=="q"):
        print("Programı sonlandır.")
        time.sleep(1)
        print("Program sonlandı.")
        break

    elif(islem=="1"):
        print("Marka seçiliyor...")
        time.sleep(1)
        Laptop.Marka_sec()

    elif(islem=="2"):
        print("RAM seçiliyor...")
        time.sleep(1)
        Laptop.Ram_sec()

    elif(islem=="3"):
        print("Ekran kartı seçiliyor...")
        time.sleep(1)
        Laptop.Ekran_karti_sec()

    elif(islem=="4"):
        print("SDD seçiliyor...")
        time.sleep(1)
        Laptop.Sdd_sec()

    elif(islem=="5"):
        print("Fiyat Belirleniyor...")
        time.sleep(1)
        Laptop.Fiyat_belirleme()

    elif(islem=="6"):
        print("Sonuç gösteriliyor...")
        time.sleep(1)
        Laptop.Bilgileri_goster()
    else:
        print("Geçersiz işlem!!!")









