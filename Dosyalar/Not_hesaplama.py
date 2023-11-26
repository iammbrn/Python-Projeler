with open("Geçenler.txt","a",encoding="utf-8") as file4:
    pass

with open("Kalanlar.txt", "a", encoding="utf-8") as file3:
    pass

def not_hesapla(satir):

    liste=satir.split(",")
    isim=liste[0]
    vize1=int(liste[1])
    vize2=int(liste[2])
    final=int(liste[3])

    ortalama=vize1 * 30/100 + vize2 * 30/100 + final * 40/100

    if(ortalama>=95):
        harf_notu="AA"
    elif(ortalama>=90):
        harf_notu="BA"
    elif(ortalama>=85):
        harf_notu="BB"
    elif(ortalama>=80):
        harf_notu="CB"
    elif(ortalama>=75):
        harf_notu="CC"
    elif(ortalama>=70):
        harf_notu="DB"
    elif(ortalama>=65):
        harf_notu="DD"
    elif(ortalama>=60):
        harf_notu="FD"
    else:
        harf_notu="FF"
        with open("Kalanlar.txt", "a", encoding="utf-8") as file3:
            file3.write(isim+"------->"+harf_notu+"\n")

    if(ortalama>=60):
        with open("Geçenler.txt","a",encoding="utf-8") as file4:
            file4.write(isim+"------->"+harf_notu+"\n")

    return isim+"------->"+harf_notu+"\n"





with open("Notlar.txt","r",encoding="utf-8") as file:
    eklenecekler_listesi = list()
    for i in file:
        eklenecekler_listesi.append(not_hesapla(i))

    with open("Sonuclar.txt","w",encoding="utf-8") as file2:
        for i in eklenecekler_listesi:
            file2.write(i)






