import pandas as pd 
from pandas import DataFrame 
from matplotlib import font_manager

flist = font_manager.findSystemFonts()
print(flist)

#폰트 리스트 만들기.

font_list = []

for v in flist:
    try:
        fprop =font_manager.FontProperties(fname=v)
        font_list.append({"name": fprop.get_name(), "file": fprop.get_file()})
    except:
        continue

df = DataFrame(font_list)

df.to_excel('font_list.xlsx')

print(df)