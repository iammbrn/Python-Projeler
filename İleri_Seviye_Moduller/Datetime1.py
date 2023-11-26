from datetime import datetime

#Şuan Fonksiyonu now()

print("Şuan :",datetime.now())

suan=datetime.now()

"""print("Yıl:",suan.year)

print("Ay:",suan.month)

print("Gün:",suan.day)

print("Saat:",suan.hour)

print("Dakika:",suan.minute)

print("Saniye:",suan.second)

print("Mikro saniye:",suan.microsecond)"""

# ctime() fonksiyonu

"""print(datetime.ctime(suan))"""

# strftime() fonksiyonu

# zaman bilgilerini türkçe yapma

import locale

locale.setlocale(locale.LC_ALL,"")

"""print("Yıl",datetime.strftime(suan,"%Y"))

print("Ay ismi",datetime.strftime(suan,"%B"))

print("Gün",datetime.strftime(suan,"%A"))

print("Saat",datetime.strftime(suan,"%X"))

print("Tarih",datetime.strftime(suan,"%D"))

print(datetime.strftime(suan,"%B %Y"))

print(datetime.strftime(suan,"%Y %B %A"))"""


#timestamp() ve fromtimestamp() fonksiyonları

"""saniye=datetime.timestamp(suan)

print(saniye)

suan2=datetime.fromtimestamp(saniye)

print(suan2)

suan3=datetime.fromtimestamp(0)

print(suan3)"""


tarih=datetime(2021,7,29)

print(suan-tarih)

