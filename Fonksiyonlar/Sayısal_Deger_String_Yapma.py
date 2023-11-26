print("*"*30)
print("Sayiların Okunuşu Programı")
print("*"*30)

birler=["","Bir ","İki ","Üç ","Dört ","Beş ","Altı ","Yedi ","Sekiz ","Dokuz "]
onlar=["","On ","Yirmi ","Otuz ","Kırk ","Elli ","Altmış ","Yetmiş ","Seksen ","Doksan "]
yuzler=["","Yüz ","İki Yüz ","Üç Yüz ","Dört Yüz ","Beş Yüz ","Altı Yüz ","Yedi Yüz ","Sekiz Yüz ","Dokuz Yüz "]


Okunus_listesi=list()
def okunus(sayi):
    birinci=sayi%10
    ikinci=(sayi//10)%10
    ucuncu=sayi//100
    Okunus_listesi.append((yuzler[ucuncu],onlar[ikinci],birler[birinci]))
    print("{} Sayisinin okunuşu {}{}{}'dir.".format(sayi,yuzler[ucuncu],onlar[ikinci],birler[birinci]))


while True:
    sayi=input("Sayi:")
    if(sayi=="q"):
        print("Okunuş listemiz=",Okunus_listesi)
        print("Program sonlandırılıyor...")
        break
    else:
        sayi=int(sayi)
        okunus(sayi)
