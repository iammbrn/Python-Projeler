def asal_bulma(sayilar):

    for i in sayilar:
        asal=True
        if(i<2):
            asal=False
        elif(i==2):
            print(i)

        else:
            for j in range(2,i):
                if(i%j==0):
                    asal=False
            if(asal):
                yield i

for sayi in asal_bulma(range(1,1001)):
    if(sayi>1000):
        break
    print(sayi)


def asal_mı(sayı):
    i = 2

    while i < sayı:
        if (sayı % i == 0):
            return False
        i += 1
    return True
def asal_generator():
    i = 2
    while True:
        if (asal_mı(i)):
            yield i
        i += 1


for sayı in asal_generator():
    if (sayı > 1000):
        break
    print(sayı)

