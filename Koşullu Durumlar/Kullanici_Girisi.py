print("""********************
Kullanıcı Girişi
********************""")

sys_kullanici_adi="Alfa"
sys_parola="12345"

kullanici_adi=input("Kullanıcı Adı Giriniz:")
parola=input("Parola Giriniz:")

if(sys_kullanici_adi==kullanici_adi and sys_parola!=parola):
    print("Hatalı parola lütfen tekrar deneyin!")
elif(sys_kullanici_adi!=kullanici_adi and sys_parola==parola):
    print("Hatalı kullanıcı adı lütfen tekrar deneyin!")
elif(sys_kullanici_adi!=kullanici_adi and sys_parola!=parola):
    print("Hatalı kullanıcı adı ve parola lütfen tekrar deneyin! ")
else:
    print("Sisteme başarıyla giriş yapıldı :)")