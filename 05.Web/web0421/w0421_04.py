from csv import writer
import re
import requests
from bs4 import BeautifulSoup
import csv #csv파일 라이브러리
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

# https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1
url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
#코스피 위치 //*[@id="contentarea"]/div[3]/table[1]/tbody

# csv파일 생성 및 저장. 
filename = "시가총액1-200.csv"
# newline="" 자동 엔터키 생략. utf-8-sig타입으로 저장하여 엑셀 한글 인코딩
f = open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

#상단 제목 입력
#csv파일은 list 타입만 저장가능
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE"
#문자를 분기할 타입을 기준으로 list타입으로 변환
title = title.split("\t")
writer.writerow(title)

data_rows = soup.find("table",{"class":"type_2"}).tbody.find_all("tr")
#tr 안의 td 모두 가져오기 위해 for문 돌림
for row in data_rows:
    #각 row마다 td를 가지고 옴.list타입 1
    columns = row.find_all("td") 
    #td가 1개 인 것(데이터가 없는 것)은 skip td가 13인 것(데이터)만 가지고 옴.
    if len(columns)<=1:
        continue
    #td가 13개인 것만 존재, 데이터 읽어오기.
    #엑셀파일,CSV 파일은 저장시 list 타입만 저장가능
    data =[]

    for column in columns: 
        data.append(column.get_text().strip())
    writer.writerow(data)
f.close()