
def Cift_bulma(sayi):
    if(sayi%2==0):
        return sayi
    else:
        raise ValueError("Sayi çift değil!")
def Us_alma(sayi):
    return sayi**2

print(Cift_bulma(122))


for i in range(1,21):
    try:
        print(Us_alma(Cift_bulma(i)))

    except ValueError:
        print("Hata!")

    except SyntaxError:
        print("Syntax Hatası")

    except ZeroDivisionError:
        print("a/b ise b=0 olamaz")
    finally:
        print("Program başarılı")