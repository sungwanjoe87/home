from unittest import skip
import requests
from bs4 import BeautifulSoup
import re

# headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
# for i in range(1,3):

#     url=""+str(i)
#     res = requests.get(url,headers=headers)
#     soup = BeautifulSoup(res.text,"lxml")


# # sub()함수는 string에서 pattern과 일치하는 문자들을 지정한 형태로 교체
# # re.sub(r'[패턴-정규표현식]','해당부분을 교체할 내용','지정된 문자-(여기서는 rate)')
# # re.sub()안의 ^는 NOT을 의미한다. (시작하는~ 이 아님!!) 
rate = "후기평점 4.8점"
re_rate = re.sub(r'[^0-9.]','',rate) #  [^\d.]와 같음   \d는 모든 십진 숫자와 같음.
print(re_rate)

text="123abc456"
re_text = re.sub(r'[^0-9]','',text)
print(re_text)

# 0~9의 숫자가 들어가 있는가 확인해서 True, False 반환.
re.compile("[0-9]")
# rate = rate[5:8]
# print(rate)

