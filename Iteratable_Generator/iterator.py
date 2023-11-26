class kuvvet3():

    def __init__(self,max):
        self.max=max
        self.kuvvet=0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.kuvvet<=self.max):
            sonuc=pow(3,self.kuvvet)
            self.kuvvet+=1
            return sonuc
        else:
            raise StopIteration

kuvvet=kuvvet3(3)

iterator=iter(kuvvet)

print(next(iterator))

print(next(iterator))
print("Kalanlar")
for i in kuvvet: # 1 ve 3 değerlerini yukarıda kulandığımız için burada kullanamıyoruz.
    print(i)


print("Yeniden tanımlama")
kuvvet=kuvvet3(3)
for i in kuvvet:
    print(i)
print("değer varmı?")
for i in kuvvet: # kuvvet iterator ını kullandığımız için değer dönmeyecek.
    print(i)
print("değer yok hepsi kullanıldı.")

class kuvvet3():

    def __init__(self,max):
        self.max=max
        self.kuvvet=0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.kuvvet<=self.max):
            sonuc=pow(3,self.kuvvet)
            self.kuvvet+=1
            return sonuc
        else:
            self.kuvvet=0
            raise StopIteration
        
kuvvet=kuvvet3(3)
print("Birinci")
for i in kuvvet:
    print(i)
print("İkinci")
for i in kuvvet:
    print(i)