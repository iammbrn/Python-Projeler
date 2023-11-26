import requests

from bs4 import BeautifulSoup

url= "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"

response= requests.get(url)

html_icerigi= response.content

soup= BeautifulSoup(html_icerigi,"html.parser")

"""for i in soup.find_all("h3",{"class":"lister-item-header"}):
    print(i.text)"""

Basliklar=soup.find_all("h3",{"class":"lister-item-header"})

Reytingler=soup.find_all("div",{"class":"ratings-bar"})

puan=float(input("Min puan:"))


for baslik,rating in zip(Basliklar,Reytingler):
    baslik=baslik.text
    rating=rating.text
    baslik=baslik.strip()
    baslik=baslik.replace("\n","")
    rating=rating.strip()
    rating=rating.replace("\n","")

    if(puan<float(rating)):
        print("Film ismi:{} Film reytingi:<{}".format(baslik,rating))



