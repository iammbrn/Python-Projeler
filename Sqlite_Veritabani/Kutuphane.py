import sqlite3
import time



class Kitap():

    def __init__(self,isim,yazar,yayinevi,tur,baski,mevcut):

        self.isim=isim
        self.yazar=yazar
        self.yayinevi=yayinevi
        self.tur=tur
        self.baski=baski
        self.mevcut=mevcut

    def __str__(self):
        return "Kitap ismi:{}\nYazar:{}\nYayınevi:{}\nTür:{}\nBaskı:{}\nMevcut Adet:{}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski,self.mevcut)


class Kutuphane():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti=sqlite3.connect("Kütüphane.db")

        self.cursor=self.baglanti.cursor()

        sorgu="Create Table if not exists kitaplar (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Tür TEXT,Baskı INT,Mevcut_Adet INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiyi_kes(self):

        self.baglanti.close()

    def kitaplari_goster(self):

        self.cursor.execute("Select *From kitaplar")
        kitaplar=self.cursor.fetchall()
        if(len(kitaplar)!=0):
            print("Bilgiler")
            for i in kitaplar:
                kitap=Kitap(i[0],i[1],i[2],i[3],i[4],i[5])
                print(kitap)

        else:
            print("Kütüphanede kitap bulunmuyor...")

    def kitap_sorgula(self,isim):
        sorgu="Select *From kitaplar where İsim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if(len(kitaplar)!=0):
            kitap=Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4],kitaplar[0][5])
            print(kitap)
        else:
            print("Böyle bir kitap bulunmuyor.")

    def kitap_ekle(self,kitap):
        sorgu="Insert into kitaplar Values(?,?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski,kitap.mevcut))
        self.baglanti.commit()

    def kitap_sil(self,isim):
        sorgu="Delete From kitaplar where İsim=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def baski_yukselt(self,isim):
        sorgu="Select * from kitaplar where İsim=?"
        self.cursor.execute(sorgu,(isim,))

        kitaplar=self.cursor.fetchall()
        if(len(kitaplar)!=0):
            baski=kitaplar[0][4]
            baski+=1
            sorgu2="Update kitaplar set Baskı=? where İsim=?"
            self.cursor.execute(sorgu2,(baski,isim))
            self.baglanti.commit()

    def kitap_odunc_ver(self,kitap_isim):
        sorgu="Select * from kitaplar where İsim=?"
        self.cursor.execute(sorgu,(kitap_isim,))
        kitap=self.cursor.fetchall()
        if(len(kitap)!=0):
            mevcut=kitap[0][5]
            mevcut-=1
            sorgu2="Update kitaplar set Mevcut_Adet=? where İsim=?"
            self.cursor.execute(sorgu2,(mevcut,kitap_isim))
            self.baglanti.commit()

    def kitap_iade_et(self,kitap_isim):
        sorgu="Select * from kitaplar where İsim=?"
        self.cursor.execute(sorgu,(kitap_isim,))
        kitap=self.cursor.fetchall()
        if(len(kitap)!=0):
            mevcut=kitap[0][5]
            mevcut+=1
            sorgu2="Update kitaplar set Mevcut_Adet=? where İsim=?"
            self.cursor.execute(sorgu2,(mevcut,kitap_isim))
            self.baglanti.commit()





