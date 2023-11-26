metin = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


class Metin():

    def __init__(self):

        self.frekans = dict()

    def Frekans(self, metin):

        for i in metin:
            if (i in self.frekans):
                self.frekans[i] += 1
            else:
                self.frekans[i] = 1

        for i, j in self.frekans.items():
            print(i, ":", j)

    def Siir(self):

        with open("Siir1.txt.", "r", encoding="utf-8") as file:
            Bas_harfler = list()
            for i in file:
                Bas_harfler += i[0]
        for i in Bas_harfler:
            print(i,end="")

    def Mail(self):

        with open("mailler.txt","r",encoding="utf-8") as file:
            for i in file:
                i=i[:-1]
                if(i.endswith(".com") and i.find("@")!=-1):
                    print(i)

    def Sirala_isim(self):

        isim=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
        soyisim=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

        liste=list(zip(isim,soyisim))

        liste.sort()

        for i,j in liste:

            print(i,j)



nesne = Metin()

# nesne.Frekans(metin)

# nesne.Siir()

# nesne.Mail()

nesne.Sirala_isim()