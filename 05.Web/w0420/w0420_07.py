from unittest import skip
import requests
from bs4 import BeautifulSoup
import re

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
for i in range(1,3):

    url="http://browse.auction.co.kr/search?keyword=tv&itemno=&nickname=&frm=hometab&dom=auction&isSuggestion=No&retry=&Fwk=tv&acode=SRP_SU_0100&arraycategory=&encKeyword=tv&k=32&p="+str(i)
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")

    #상품명:
    #금액:
    #후기평점: 4.5 이상
    #후기: 1000개 이상
    #구매수: 100개 이상

    #/html/body/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/span/a/span[4]/text()
    #//*[@id="section--inner_content_body_container"]/div[4]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/span[2]/strong
    #/html/body/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[1]/div[2]/div[2]/div[2]/ul/li[2]/span[1]/text()[2]
    #//*[@id="section--inner_content_body_container"]/div[2]/div[2]/div/div/div[1]
    items = soup.find_all("div",{"class":re.compile("component component--item_card type--")})

    for item in items:
        item_detaile = item.find("div",{"class":"section--itemcard_info"})
        item_name = item_detaile.find("span",{"class":"text--title"}).get_text() #제품이름
        item_price = item_detaile.find("strong",{"class":"text--price_seller"}).get_text()  #제품가격
        item_attpre = item_detaile.find("li",{"class":"item awards"}) #후기평점 앞
        item_buy_count = item_detaile.find("li",{"class":"item buycnt"}) #구매수 앞
        
        item_url = item.find("div",{"class":"itemcard"})
        item_url = item_url.find("div",{"class":"section--itemcard"})
        item_url = item_url.find("div",{"class":"section--itemcard_img"})
        
        #후기평점 없는 것은 통과
        if  not item_attpre:
            continue
        
        else:
            item_att = item_attpre.find("span",{"class":"for-a11y"}).get_text()
            item_att = float(item_att[5:-1])
            #후기 평점 있는 것은 당연히 후기 평점 개수도 있음
            item_attpre_cnt = item_detaile.find("li",{"class":"item reviewcnt"})
            item_attpre_cnt = item_attpre_cnt.find("span",{"class":"text--reviewcnt"}).get_text()
            item_attpre_cnt = (item_attpre_cnt[3:])
            item_attpre_cnt = int(item_attpre_cnt.replace(",",""))

        #구매수가 없으면 통과
        if not item_buy_count:
            continue
        else:
            item_buy_count = item_buy_count.find("span",{"class":"text--buycnt"}).get_text()
            item_buy_count = (item_buy_count[3:])
            item_buy_count = int(item_buy_count.replace(",",""))
            item_url = item_url.a["href"] #링크... 왜 이딴 곳에 있는거냐...
        if item_att <4.5 or item_attpre_cnt <1000 or item_buy_count < 100:
            continue

        print("제품 이름: {}".format(item_name))
        print("제품 가격: {}원".format(item_price))
        print("후기평점 : {} 점".format(item_att))
        print("후기 수: {}개".format(item_attpre_cnt))
        print("구매 개수: {}개".format(item_buy_count))
        print("바로가기 링크 :{}".format(item_url))
        print("="*70)

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

