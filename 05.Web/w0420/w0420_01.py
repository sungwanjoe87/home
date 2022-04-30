import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
url = "https://corners.gmarket.co.kr/Bestsellers"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")


# //*[@id="gBestWrap"]/div(id:topPlusItems/div[3]/div[2]/ul/li[1] 
goods = soup.find("div",{"id":"topPlusItems"})
bestlists = goods.find_next_sibling("div").find_all("li") 

for i,bestlist in enumerate(bestlists):
    print("{}번 제품 : {} ".format(i+1,bestlist.find("a",{"class":"itemname"}).get_text()))