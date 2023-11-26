import os

""" print(dir(os))  içinddeki fonksiyonları gösterir"""

# getcwd() fonksiyonu adres bilgisi

"""print(os.getcwd())"""

# chdir() fonksiyonu adres değiştirme

"""os.chdir("c:/Users/Baran Bey/Desktop")
print(os.getcwd())

#listdir() verilen adresteki dosyaları listeleme yapar

for i in os.listdir():
    print(i)"""

# mkdir() fonksiyonu bulunduğun dosya altına klasor oluşturmanı sağlar.
print(os.getcwd())


"""os.mkdir("klasor1") # klasor1 oluşturdu"""

# makedirs("x/y") x'i oluşturur ve onu altına y klasorunu oluşturur.

"""os.makedirs("klasor2/klasor3") #klasor2 altında klasor3 oluşturuldu."""

# rmdir("x/y") y' yi siler

"""os.rmdir("klasor1") #klasor1 silindi."""

"""os.rmdir("klasor2/klasor3") #klasor3 silindi."""

# removedirs("x/y") x ve altındaki bütün klasorleri siler.

"""os.removedirs("klasor2/klasor3") #klasor2 ve altındaki klasor3 silindi."""

# rename("x","y") x dosyasının isminini y ile değiştirir.

"""os.rename("test12.txt","test1.txt") # test12.txt dosyası test1.txt olarak değiştirildi."""

# stat("x") x dosyasının bütün özelliklerini verir.
# st_mtime dosyanın değiştirilme zamanını saniye cinsinden verir.

"""from datetime import datetime
# dosyanın değiştirlme zamanını dattime fonksiyonuyla saniyeyi zaman çevirerek bulduk.
print(datetime.fromtimestamp(os.stat("test1.txt").st_mtime))"""

# walk("C:/Users/Baran Bey/Desktop") verilen adresteki bütün dosya ve klasörleri verir.
print(os.walk("C:/Users/Baran Bey/Desktop"))

"""for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users/Baran Bey/Desktop"):
    print("Klasör yolu:",klasor_yolu)
    print("Klasör ismi:",klasor_isimleri)
    print("Dosya ismi:",dosya_isimleri)
    print("*"*50)"""
# sadece txt dosyalarını almak istersek aşağıdaki gibi alabiliriz.
for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users/Baran Bey/Desktop"):
    for i in dosya_isimleri:
        if(i.endswith(".txt")):
            print(i)







