


with open("kisi_bilgiler.txt","r+",encoding="utf-8") as file:
    isim=list()
    telefon=list()
    eposta=list()
    liste=list()
    for i in file:
        liste=i.split(",")
        for j in range(0,len(liste)):
            if(j==0):
                isim.append(liste[0]+"\n")
            elif(j==1):
                telefon.append(liste[1]+"\n")
            elif(j==2):
                eposta.append(liste[2])

    print("""****************************************
    Dosya işlemleri:
    
    1. işlem guncelle
        
        1. işlem isim güncelle
        2. işlem telefon güncelle
        3. işlem e-posta  güncelle
        
    
    2. işlem ekle
    
    3. işlem sil
    
    q. işlem programı sonlandır(q)
    ****************************************""")

    while True:
        islem=input("islem:")
        if(islem=="q"):
            print("Program sonlandırılıyor...")
            break

        elif(islem=="1"):
            islem1=input("islem1:")
            if(islem1=="1"):
                for i in range(0,len(isim)):
                    yeni= input("Yeni isim:")
                    if (yeni != "q"):
                        a=int(input("Güncellencek isim indeksi:"))
                        with open("kisi_bilgiler.txt", "w", encoding="utf-8") as file:
                            for j in range(0,len(isim)):
                                if(j==a):
                                    file.write(yeni + "," + telefon[j].strip("\n") + "," + eposta[j])
                                else:
                                    file.write(isim[j].strip("\n") + "," + telefon[j].strip("\n") + "," + eposta[j])
                            isim[a]=yeni+"\n"
                    else:
                        break
            elif(islem1=="2"):
                for i in telefon:
                    yeni= input("Yeni:")
                    if (yeni != "q"):
                        a=int(input("Güncellencek isim indeksi:"))
                        with open("kisi_bilgiler.txt", "w", encoding="utf-8") as file:
                            for j in range(0,len(isim)):
                                if(j==a):
                                    file.write(isim[j].strip("\n") + "," + yeni+ "," + eposta[j])
                                else:
                                    file.write(isim[j].strip("\n") + "," + telefon[j].strip("\n") + "," + eposta[j])
                            telefon[a]=yeni+"\n"
                    else:
                        break
            elif(islem1=="3"):
                for i in eposta:
                    yeni= input("Yeni:")
                    if (yeni != "q"):
                        a=int(input("Güncellencek isim indeksi:"))
                        with open("kisi_bilgiler.txt", "w", encoding="utf-8") as file:
                            for j in range(0,len(isim)):
                                if(j==a):
                                    file.write(isim[j].strip("\n") + "," + telefon[j].strip("\n") + "," + yeni)
                                else:
                                    file.write(isim[j].strip("\n") + "," + telefon[j].strip("\n") + "," + eposta[j])
                            eposta[a]=yeni+"\n"
                    else:
                        break
        elif(islem=="2"):
            yeni_kisi=input("Yeni Kişi:")
            liste.append(yeni_kisi+"\n")
            file.write(liste[-1])
            for i in range(1):
                liste1=liste[-1].split(",")
                isim.append(liste1[0])
                telefon.append(liste1[1])
                eposta.append(liste1[2])

        elif(islem=="3"):
            a = int(input("Silinecek indeks:"))
            isim.pop(a)
            telefon.pop(a)
            eposta.pop(a)
            with open("kisi_bilgiler.txt","w",encoding="utf-8") as file:
                for i in range(0,len(isim)):
                    file.write(isim[i].strip("\n")+","+telefon[i].strip("\n")+","+eposta[i])


    with open("Ad_Soyad.txt","w",encoding="utf-8") as file1:
        for i in isim:
            file1.write(i)

    with open("Telefon.txt","w",encoding="utf-8") as file2:
        for i in telefon:
            file2.write(i)
    with open("E_posta.txt","w",encoding="utf-8") as file3:
        for i in eposta:
            file3.write(i)






