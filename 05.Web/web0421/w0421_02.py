import re
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
#2017부터 2021년까지
for year in range(2017,2022):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"lxml")

    #파일 
    moives_search = soup.find("div",{"id":"morColl"}).find("div",{"class":"coll_cont"})
    moives = moives_search.find("ol",{"class":"type_plural list_exact movie_list"})
    moives = moives.find_all("li")
    images = soup.find_all("img",{"class":"thumb_img"})


    #//*[@id="morColl"]/div[2]/div/ol/li[1]/div[2]/dl[4]
    for i, moive in enumerate(moives):
        moive_detaile = moive.find("div",{"class":"wrap_cont cont_type2"})
        moive_title = moive_detaile.find("div",{"class":"info_tit"})
        moive_title = moive_title.a.get_text()
        moive_score = moive_detaile.find("dl",{"class":"dl_comm star_comp_s"})
        moive_score = moive_score.find("dd",{"class":"score"}).em.get_text()
        moive_count = moive_detaile.find("dl",{"class":"dl_comm star_comp_s"})
        moive_count = moive_detaile.dl.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
        moive_img_url = moive.find("div",{"class":re.compile("^wrap_thumb")}).a
        moive_img_url = moive_img_url.find("img",{"class":"thumb_img"})["src"]
        moive_link = moive.find("div",{"class":"info_tit"}).a["href"]
        if moive_count:
            
            print("제목        : {}" .format(moive_title))
            print("평점        : {}" .format(moive_score))
            print("누적관객 수  : {} ".format(moive_count.dd.get_text()))
            print("포스터 URL   : {} " .format(moive_img_url))
            print("영화검색 링크 : {}".format("https://search.daum.net/search"+moive_link))
            print("="*90)
        #이미지 링크를 가지고 requests함수 다시 실행.
        img_res = requests.get(moive_img_url)
        img_res.raise_for_status()
        
        #영화 포스터 이미지 링크 저장.
        # with open("aaa.html","w",encoding="utf-8") 문자저장= 이름, 생성, 인코딩
        with open("{}_{}.jpg".format(year,i+1),"wb") as f:
            #requests = status.code-상태, text-글자, content-파일
            f.write(img_res.content)


        #상위 5개 이미지URL만 출력    
        if i>=4:
            break
f.close()
        
        
    # for i, image in enumerate(images):
    #     img_url = image["src"]
    #     #startswith 함수: 해당문자로 사직하는지 확인.
    #     if img_url.startswith("//"):
    #         img_url = "https:"+img_url

    #     print(img_url)
        
    #     #상위 5개 이미지URL만 출력    
    #     if i>=5:
    #         break
        

            
        
    #년도별 2017 - 2021 5개
    # 제목
    # 평점
    # 누적
    # 링크
    # 파일 저장까지.

