from unittest import skip
import requests
from bs4 import BeautifulSoup
import re

url="http://browse.auction.co.kr/search?keyword=tv&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=tv&acode=SRP_SU_0100&arraycategory=&encKeyword=tv"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

#상품명:
#금액:
#후기평점: 4.5 이상
#후기: 1000개 이상
#구매수: 100개 이상

items = soup.find_all("div",{"class":"component component--item_card type--general"})

item_detaile = items[0].find("div",{"class":"section--itemcard_info"})
item_name = item_detaile.find("span",{"class":"text--title"})
print(item_name)

