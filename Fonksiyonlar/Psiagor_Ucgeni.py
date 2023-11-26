print("""******************************
Pisagor Üçgeni Bulma Programı

işlemler:

a=(b**2+c**2)**0.5

ve a==int(a)

******************************""")

Pisgor_ucgeni_liste=list()

def Pisagor_ucgen_bulma(x,y,z):

    if(x>y and x>z):
        if(x==(y**2+z**2)**0.5):
            if(x==int(x)):
                print("{} {} {} üçgeni pisagor üçgenidir.".format(x, y, z))
                Pisgor_ucgeni_liste.append((x,y,z))
        else:
            print("{} {} {} üçgeni pisagor üçgeni değildir.".format(x, y, z))

    elif(y>x and y>z):
        if(y==(x**2+z**2)**0.5):
            if(y==int(y)):
                print("{} {} {} üçgeni pisagor üçgenidir.".format(x,y,z))
                Pisgor_ucgeni_liste.append((x, y, z))
        else:
            print("{} {} {} üçgeni pisagor üçgeni değildir.".format(x, y, z))
    elif(z>x and z>y):
        if(z==(x**2+y**2)**0.5):
            if(z==int(z)):
                print("{} {} {} üçgeni pisagor üçgenidir.".format(x,y,z))
                Pisgor_ucgeni_liste.append((x, y, z))
        else:
            print("{} {} {} üçgeni pisagor üçgeni değildir.".format(x, y, z))



while True:
    x=input("x:")
    if(x=="q"):
        print("Pisagor üçgenleri listemiz=",Pisgor_ucgeni_liste)
        print("Program Sonlandırılıyor...\n")
        break
    else:
        x=int(x)
        y=int(input("y:"))
        z=int(input("z:"))
        Pisagor_ucgen_bulma(x,y,z)




print("""******************************
Pisagor Üçgeni Bulma Programı 2
******************************""")


def pisagor_bulma():
    pisagor_listesi = list()
    for i in range(1, 101):
        for j in range(1, 101):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)):
                pisagor_listesi.append((i, j, int(c)))

    return pisagor_listesi


for i in pisagor_bulma():
    print(i)
