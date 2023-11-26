print("""********************
Kullanıcı girişi programı
********************""")

sys_kullanici_adi="Alfa"
sys_parola="12345"

giris_hakki=3

while True:
    kullanici_adi = input("Kullanıcı Adı Giriniz:")
    parola = input("Parola Giriniz:")

    if (sys_kullanici_adi == kullanici_adi and sys_parola != parola):
        print("Hatalı parola ")
        giris_hakki-=1
    elif (sys_kullanici_adi != kullanici_adi and sys_parola == parola):
        print("Hatalı kullanıcı adı")
        giris_hakki -=1
    elif (sys_kullanici_adi != kullanici_adi and sys_parola != parola):
        print("Hatalı kullanıcı adı ve parola")
        giris_hakki -=1
    else:
        print("Sisteme başarıyla giriş yapıldı :)")
        break
    if(giris_hakki==0):
        print("Giriş Hakkınız Bitti!!!")
        break


