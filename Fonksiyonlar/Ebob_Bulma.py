print("""******************************
Ebob Bulma Programı
******************************""")

"""def Ebob_bulma(x,y):
    ebob=0
    if(x>y):
        for i in range(1,y+1):
            if(x%i==0 and y%i==0):
                ebob=i
        print("{} ve {} nin ebobu={}".format(x,y,ebob))
    else:
        for i in range(1,x+1):
            if(x%i==0 and y%i==0):
                ebob=i
        print("{} ve {} nin ebobu={}".format(x,y,ebob))

    
x=int(input("x:"))
y=int(input("y:"))

Ebob_bulma(x,y)"""

def Ebob_bulma(x, y):
    ebob = 0
    if (x > y):
        for i in range(1, y + 1):
            if (x % i == 0 and y % i == 0):
                ebob = i
        print("{} ve {} nin ebobu = {}".format(x, y, ebob))
    else:
        for i in range(1, x + 1):
            if (x % i == 0 and y % i == 0):
                ebob = i
        print("{} ve {} nin ebobu = {}".format(x, y, ebob))

while True:
    x = input("x:")
    y = input("y:")
    if(x=="q" and y=="q"):
        print("Program sonlandırılıyor...")
        break
    else:
        x=int(x)
        y=int(y)
        Ebob_bulma(x, y)

