import requests

from bs4 import BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=ankara"

response = requests.get(url)

"""content response içeriğini aliır"""
html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

#print(soup.prettify())

#print(soup.find_all("div")) #

# div etiketli dosyalar.
"""for i in soup.find_all("div"):
    print(i)
    print("*"*100)"""

#div etiketli dosyaların class isimleri.
"""for i in soup.find_all("div"):
    print(i.get("class"))
    print("*"*100)"""

#div etiketli dosyaların içindeki yazılar.
"""for i in soup.find_all("div"):
    print(i.text)
    print("*"*100)"""


print(soup.find_all("div",{"class":"bubbles"}))

