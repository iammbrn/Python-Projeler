print("""******************************
Atm Makinesi Programı

Giriş yap parola ile

İşlemler:

1. Bakiye Sorgulama

2. Para Yatırma

3. Para Çekme

Kart iadesi için 'q' ya basın
******************************""")

Bakiye=1000

kart_parola="12345"
giris_hakki=3
a = 0

while True:
    if(a == 0):
        for i in range(giris_hakki):
            parola = input("Parola giriniz:")
            if (kart_parola == parola):
                print("Hoşgeldiniz :)")
                a += 1
                break
            elif (kart_parola != parola):
                giris_hakki -= 1
                if(giris_hakki==0):
                    print("Parola giris hakkiniz bitmiş ve kartiniza guvenlik acısından el konulmustur. Kartinizi almak icin kurumumuza ugrayabilirsiniz.")
                    break
                print("Parola yanlıs lutfen tekrar deneyiniz! {} hakkiniz kaldı!".format(giris_hakki))
    if(giris_hakki==0):
        break
    islem=input("Yapmak istediğiniz işlemi seçin:")
    if(islem=="1"):
        print("Bakiyeniz {} tl dir.".format(Bakiye))
    elif(islem=="2"):
        miktar = int(input("Miktarı giriniz:"))
        Bakiye+=miktar
    elif(islem=="3"):
        miktar = int(input("Miktarı giriniz:"))
        if(miktar>Bakiye):
            print("Bakiye yetersiz")
            continue
        print("Hesabinizdan {} tl cekilmistir.".format(miktar))
        Bakiye -= miktar
    elif(islem == "q"):
        print("Lutfen kartinizi alin!")
        break
    else:
        print("Gecersiz islem!!!")





