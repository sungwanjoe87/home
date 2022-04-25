import re
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}

for page in range(4):
    url="https://www.genie.co.kr/chart/top200?ditc=D&ymd=20220421&hh=15&rtm=Y&pg={}".format(page+1)
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")


    #//*[@id="body-content"]/div[6]/div/table/tbody/tr[1]/td[5]/a[3]


    musics = soup.find("table",{"class":"list-wrap"}).tbody
    musics = musics.find_all("tr",{"class":"list"})



    for i, music in enumerate(musics):
        musicdetaile = music.find("td",{"class":"info"})
        musictitle = musicdetaile.find("a",{"class":"albumtitle ellipsis"})
        artist = musicdetaile.find("a",{"class":"artist ellipsis"})
        img_url = musics[0].find("a",{"class":"cover"}).img["src"] #내부 a 속성 중에 첫번째 속성
        
        print("음악제목 : {} ".format(musictitle.get_text()))
        print("가수 :{} ".format(artist.get_text()))
        if img_url.startswith("//"):
            print("링크 : {} ".format("https:"+img_url))
        else:
            print("링크 : {} ".format(img_url))
        ("="*90)
        
        #이미지 다운로드
        
        img_url_res = requests.get(img_url)
        img_url_res.raise_for_status() #에러시 종료
        with open("img_{}_{}.jpg".format(page+1,(i+1)),"wb") as f:
            f.write(img_url_res.content)