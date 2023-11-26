print("""******************************
Ebob ve Ekok Bulma Programı
******************************""")


Ebob=0
Ekok=0
Ebob_Ekok_Liste = list()
def Ebob_Ekok(x,y):
    if(x>y):
        for i in range(1,x+1):
            if(x%i==0 and y%i==0):
                Ebob=i
                Ekok=(x*y)//Ebob

        print("{} ve {} nin ebobu = {} ekoku = {}".format(x, y, Ebob,Ekok))
        tuple = (Ebob, Ekok)
        Ebob_Ekok_Liste.append(tuple)
    else:
        for i in range(1,y+1):
            if(x%i==0 and y%i==0):
                Ebob=i
                Ekok=(x*y)//Ebob
        print("{} ve {} nin ebobu = {} ekoku = {}".format(x, y, Ebob, Ekok))
        tuple = (Ebob, Ekok)
        Ebob_Ekok_Liste.append(tuple)

while True:
    x=input("x:")
    if(x=="q"):
        print("Program sonlandırılıyor...")
        break

    else:
        x=int(x)
        y=int(input("y:"))
        Ebob_Ekok(x,y)
print("Verilen değerlerin ebob ve ekok değerlerinin  liste hali={}".format(Ebob_Ekok_Liste))

