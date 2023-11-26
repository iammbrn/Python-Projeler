print("""********************
Hesap Makinesi Programı
      
İşlemler:
      
1. Toplama işlemi
      
2. Çıkarma işlemi
      
3. Çarpma işlemi
      
4. Bölme işlemi
********************""")

a=int(input("Birinci sayiyi girin:"))
b=int(input("Ikinci sayiyi girin:"))

işlem=int(input("işlem:"))

if(işlem==1):
    print("Girilen iki sayinin toplamı=",a+b)
elif(işlem==2):
    print("Girilen iki sayinin farki=",a-b)
elif(işlem==3):
    print("Girilen iki sayinin çarpimi=",a*b)
elif(işlem==4):
    print("Girilen iki sayinin bölümü=",a/b)
else:
    print("Geçersiz işlem!!!")


