import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
url = "https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

#평균 평점
# float(get_text)

table = soup.find("table",{"class":"viewList"})
cartoons = table.find_all("tr")
# print(cartoons)
cartoons=cartoons[1:]
for i, cartoon in enumerate(cartoons):
    ctext = cartoon.find("td",{"class":"title"}).a.get_text()
    curl = cartoon.find
    print("{}번 : {}".format(i+1,ctext))
