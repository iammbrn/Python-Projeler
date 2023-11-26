"""
2. Dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem: ax^2 + bx + c

Delta Hesaplama= b ** 2 - 4 * a * c

Birnci Kök= (-b - Delta** 0.5) / (2*a)
İkinci Kök= (-b + Delta** 0.5) / (2*a)

"""

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

Delta=b ** 2 - 4 * a * c

x1=int((-b - Delta** 0.5) / (2*a))
x2=int((-b + Delta** 0.5) / (2*a))

print("Birinci Kök x1={}\nİkinci Kök x2={}\n".format(x1,x2))