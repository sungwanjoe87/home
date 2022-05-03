import requests
from bs4 import BeautifulSoup
import re
import csv

# 2020년 ~ 2022년까지 for문
for i in range(2020,2023):
    url="http://www.statiz.co.kr/salary.php?opt=0&sopt={}&te=".format(i)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")

    # csv파일 저장
    filename="{}년연봉.csv".format(i)
    f=open(filename,"w",encoding="utf-8-sig",newline="")
    writer =csv.writer(f)

    # 상단제목 저장
    title="선수,연도,팀,연봉(만원),WAR(승리기여도)".split(" ")
    writer.writerow(title)

    table = soup.find("table",{"class":"table table-striped"})
    # print(table)
    players = table.find_all("tr")
    # 첫번째 tr의 th 제외 후 다음 tr의 td부터 입력 
    players = players[1:]
    for i,player in enumerate(players):
        # if i==0:
        #     continue
        s_tds = player.find_all("td")
        name = s_tds[0].get_text()
        year = s_tds[1].get_text()
        team = s_tds[2].get_text()
        salary = s_tds[3].get_text()
        war = s_tds[4].get_text()
        print('선수이름  :',name)
        print('출전연도  :',year)
        print('소속구단  :',team)
        print('선수연봉  :',salary)
        print('승리기여도:',war)
        print("-"*10)
        
        # csv파일 저장
        data=[name,year,team,int(re.sub(r'[,]','',salary)),war]
        # data 리스트 저장
        writer.writerow(data)