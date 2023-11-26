import time
import sqlite3

class Muzik():

    def __init__(self,isim,sanatci,album,prod_sirketi,sarki_suresi):
        self.isim=isim
        self.sanatci=sanatci
        self.album=album
        self.prod_sirketi=prod_sirketi
        self.sarki_suresi=sarki_suresi

    def __str__(self):
        return "Şarkı ismi:{}\nSanatçı:{}\nAlbüm:{}\nProdüksiyon ekibi:{}\nŞarkı süresi:{}\n".format(self.isim,self.sanatci,self.album,self.prod_sirketi,self.sarki_suresi)



class Sarkılar():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti=sqlite3.connect("Şarkılar.db")
        self.cursor=self.baglanti.cursor()

        sorgu="Create Table if not exists sarkilar (İsim TEXT,Sanatçı TEXT,Albüm TEXT,Prodüksiyon Şirketi TEXT,Şarkı Süresi TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def sarkilari_goster(self):
        sorgu="Select * From sarkilar"
        self.cursor.execute(sorgu)
        liste=self.cursor.fetchall()
        if(len(liste)!=0):
            for i in liste:
                sarki=Muzik(i[0],i[1],i[2],i[3],i[4])
                print(sarki)
        else:
            print("Listede Şarkı Bulunmuyor.")


    def sarki_ekle(self,sarki):
        sorgu="Insert into sarkilar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.album,sarki.prod_sirketi,sarki.sarki_suresi))
        self.baglanti.commit()


    def sarki_sil(self,isim):
        sorgu="Delete from sarkilar where İsim=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def sarki_ara(self,isim):

        sorgu="Select *From sarkilar where İsim=?"
        self.cursor.execute(sorgu,(isim,))
        liste=self.cursor.fetchall()

        if(len(liste)!=0):
            muzik=Muzik(liste[0][0],liste[0][1],liste[0][2],liste[0][3],liste[0][4])
            print(muzik)

        else:
            print("Böyle bir şarkı bulunmuyor.")


