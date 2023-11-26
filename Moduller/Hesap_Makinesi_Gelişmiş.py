import math
import time

def toplama(x,y):
    return x+y

def cıkarma(x,y):
    return x-y

def carpma(x,y):
    return x*y

def bolme(x,y):
    if(y!=0):
        return int(x/y)
    else:
        print("Hata:sıfıra bölme hatası")

def karekok(x):
    return int(math.sqrt(x))

def usalma(x,y):
    return int(math.pow(x,y))

def faktoriyel(x):
    return math.factorial(x)

print("Hesap Makinesi İşlemleri:")
print("1. İşlem Toplama ")
print("2. İşlem  Çıkarma")
print("3. İşlem  Çarpma")
print("4. İşlem  Bölme")
print("5. İşlem Karekök")
print("6. İşlem Üslü Sayı")
print("7. İşlem Faktöriyel")

while True:
    islem=input("islem:")

    if(islem=="of"):
        print("Program sonlandırılıyor...")
        time.sleep(1)
        print("Program sonlandı.")
        break
    elif(islem=="1"):
        print("Toplama")
        x = int(input("x:"))
        y = int(input("y:"))
        print("{}+{} Toplamları={}".format(x,y,toplama(x,y)))
    elif(islem=="2"):
        print("Çıkarma")
        x = int(input("x:"))
        y = int(input("y:"))
        print("{}-{} Farkları={}".format(x,y,cıkarma(x,y)))
    elif(islem=="3"):
        print("Çarpma")
        x = int(input("x:"))
        y = int(input("y:"))
        print("{}x{} Çarpımları={}".format(x,y,carpma(x,y)))
    elif(islem=="4"):
        print("Bölme")
        x = int(input("x:"))
        y = int(input("y:"))
        print("{}/{} Bölümü={}".format(x,y,bolme(x,y)))
    elif(islem=="5"):
        print("Karekök alma")
        x = int(input("x:"))
        print("{} Karekökü ={}".format(x,karekok(x)))
    elif(islem=="6"):
        print("Üs alma")
        x = int(input("x:"))
        y = int(input("y:"))
        print("{}^{} Üssü={}".format(x,y,usalma(x,y)))
    elif(islem=="7"):
        print("Faktoriyel bulma")
        x = int(input("x:"))
        print("{}! Faktoriyel={}".format(x,faktoriyel(x)))
    else:
        print("Hata: Bilinmeyen komut lütfen başka bir komut girin!!!")
