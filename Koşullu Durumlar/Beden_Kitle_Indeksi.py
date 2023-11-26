print("""********************
Beden Kitle İndeksi programı

Beden kitle indeksi=kilo/(boy**2)

BKİ 18.5'in altındaysa ----> Zayıf
BKİ 18.5 ile 25 arasındaysa ----> Normal
BKİ 25 ile 30 arasındaysa ----> Fazla Kilolu
BKİ 30'un üzerindeyse ----> Obez
********************""")

kilo=int(input("Kilo="))
boy=float(input("Boy="))

Bki=kilo/(boy**2)

if(Bki<18.5):
    print("Zayıf")
elif(18.5<=Bki and Bki<=25):
    print("Normal")
elif(25<=Bki and Bki<=30):
    print("Fazla kilolu")
elif(Bki>30):
    print("Obez")