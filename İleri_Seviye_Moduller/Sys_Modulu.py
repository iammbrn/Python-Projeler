import sys

#print(dir(sys))

"""a=int(input("a:"))
b=int(input("b:"))

# exit() fonksiyonu aniden programı sonlandırır sonraki kodlar çalışmaz.
sys.exit()

c=int(input("c:"))"""

# stdin : Kullanıcıdan input almayı sağlar.
# stdout: Çıktı vermeyi yani (print) sağlar.
# stderr: Hata mesajlarını çıktı olarak verir.

"""sys.stderr.write("Bu bir hata mesajıdır!!!\n")
sys.stderr.flush() # anında ekrana yazdırmak için kullanılır.

sys.stdout.write("Bu normal bir çıktıdır.\n")"""

# argv fonksiyonu eklenen bütün parametreleri başta dosya ismi olmak üzere liste olarak tutar.
# sys.argv çalıştırmak için ya cmd kullanılır yada pycharmdaki terminal (alt + f12).

"""# python dosya ismini ilk eleman olarak diğer değerleri de sırayla basar.
for i in sys.argv:
    print(i)"""

"""# python dosya ismini ilk eleman olarak diğer değerleri de sırayla alarak listeler.
print(sys.argv)"""

def kok_bulma(a,b,c):
    delta=b**2- 4*a*c
    if(delta<0):
        print("Reel kök yoktur.")
    elif(delta==0):
        x1=x2=-b/2*a
        return (x1,x2)
    else:
        x1=(-b - (delta**1/2))/2*a
        x2=(-b + (delta**1/2))/2*a
        return (x1,x2)

if len(sys.argv)==4:
    print("Kök bulma kökler=",kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen doğru değerler girin!")
    sys.stderr.flush()







