class kare():

    def __init__(self,max):
        self.max=max
        self.sayi=0

    def __iter__(self):
        return self

    def __next__(self):
            if(self.sayi<=self.max):
                sonuc=pow(self.sayi,2)
                self.sayi+=1
                return sonuc
            else:
                raise StopIteration
kareler=kare(10)
for i in kareler:
    print(i)

print("Kareler2")
kareler2=kare(5)

for i in kareler2:
    print(i)

#for i in kareler2: """ herhangi bir değer üretmedi çünkü iterator üste bir kere kullanıldı artık kullanılamaz. tekrar kullanabilmek tekrar tanımlamak lazım"""
#   print(i)


print("istediğimiz kadar iterator kullanbilme")
class kare():

    def __init__(self,max):
        self.max=max
        self.sayi=0

    def __iter__(self):
        return self

    def __next__(self):
            if(self.sayi<=self.max):
                sonuc=pow(self.sayi,2)
                self.sayi+=1
                return sonuc
            else:
                self.sayi=0
                raise StopIteration

kareler2=kare(5)

for i in kareler2:
    print(i)
print("************")
for i in kareler2:
    print(i)

print("************")

for i in kareler2:
    print(i)