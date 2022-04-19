import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
url = "https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

#평균 평점
# float(get_text)

table = soup.find("table",{"class":"viewList"})
# print(cartoons)
cartoons = table.find_all("tr")
cartoons=cartoons[1:]
total_rates = 0
for i, cartoon in enumerate(cartoons):
    ctext = cartoon.find("td",{"class":"title"}).a.get_text()
    curl = cartoon.find("td",{"class":"title"}).a["href"]
    rate = cartoon.find("strong").get_text()
    total_rates += float(rate)
    print()
    print("{}번 : {}".format(i+1,ctext))
    print("바로가기 링크 : {}".format("https://comic.naver.com"+curl))
    print("-"*90)
    print("별점 : {}점".format(rate))
print()
print("-"*90)
print("전체 점수 : {}".format(round(total_rates,2)))
print("평균 점수 : {}".format(total_rates/len(cartoons)))

