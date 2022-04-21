from csv import writer
import re
import requests
from bs4 import BeautifulSoup
import csv #csv파일 라이브러리
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

# https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1
url="https://www.melon.com/chart/index.htm"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

filename = "멜론 차트top100.csv"
f = open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)


#//*[@id="frm"]/div/table/tbody

songall = soup.find("div",{"id":"tb_list"}).tbody
musics = songall.find_all("tr")
# print(musics)


for music in musics:

    columns = music.find_all("td") 
    if len(columns)<=1:
        continue
    
    data =[]
    # print(columns)

    for column in columns: 
        data.append(column.get_text().strip().replace("\t","").replace(" ","").replace(""))

    writer.writerow(data)
f.close()