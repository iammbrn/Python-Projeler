import sqlite3
import time

class Urun():

    def __init__(self,isim,fiyat):

        self.isim=isim
        self.fiyat=fiyat

    def __str__(self):

        return "Ürün ismi:{}\nFiyat:{}\n".format(self.isim,self.fiyat)

class Market():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti=sqlite3.connect("Market.db")
        self.cursor=self.baglanti.cursor()

        sorgu="Create Table if not exists Urunler (İsim TEXT,Fiyat INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def urunleri_goster(self):
        sorgu="Select * From Urunler"
        self.cursor.execute(sorgu)
        liste=self.cursor.fetchall()

        if(len(liste)!=0):
            for i in liste:
                urun=Urun(i[0],i[1])
                print(urun)

            print("Bu ürünler mevcut.")
        else:
            print("Market'te ürün bulunmuyor.")

    def urun_ekle(self,urun):

        sorgu="Insert into Urunler Values(?,?)"
        self.cursor.execute(sorgu,(urun.isim,urun.fiyat))
        self.baglanti.commit()

    def urun_sil(self,urun_isim):

        sorgu="Delete from Urunler where İsim=?"
        self.cursor.execute(sorgu,(urun_isim,))
        self.baglanti.commit()

    def urun_sorgula(self,urun_isim):

        sorgu="Select * from Urunler where İsim=?"
        self.cursor.execute(sorgu,(urun_isim,))
        urunler=self.cursor.fetchall()

        if(len(urunler)!=0):
            urun=Urun(urunler[0][0],urunler[0][1])
            print(urun)
            print("Ürün mevcut.")

        else:
            print("Böyle bir ürün bulunmuyor.")

