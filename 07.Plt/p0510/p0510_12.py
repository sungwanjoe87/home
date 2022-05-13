from cProfile import label
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15
matplotlib.rcParams['axes.unicode_minus'] = False
import re

df = pd.read_excel('인구통계.xls', usecols='a,b,e,f,k,l,q,r,w,x')
print(df.info())
df = df.drop([0,], axis= 0)
print(df)
def cut(txt):
    txt = re.sub(r'[^가-힣]','',txt)
    return txt


print(df['행정구역'])
df['행정구역'] = df['행정구역'].astype(str).apply(cut)
print(df)

print(df.sort_values('2018년_총인구수'))

df2 = df.sort_values('2018년_총인구수')

x = df2['행정구역']
y = df2['2018년_총인구수']//1000
z1 = df2['2018년_남자 인구수']//1000
z2 =  df2['2018년_여자 인구수']//1000
# plt.bar(x,y)
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()

plt.barh(x,z1,label='2018년 남자인구수')
plt.barh(x,-z2,label='2018년 여자인구수')
plt.legend()
plt.show()
