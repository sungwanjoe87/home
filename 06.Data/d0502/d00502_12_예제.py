import pandas as pd
#평가용 함수.
def result(score):
    # A,B,C,D,F 평가
    if score >= 90:
        temp = 'A'
    elif score >= 80:
        temp = 'B' 
    elif score >= 70:
        temp = 'C' 
    elif score >= 60:
        temp = 'D'
    else:
        temp = 'F'     
                
    return temp


df = pd.read_excel('score.xlsx',index_col='지원번호')

# 1. 평가
# 사회점수평가 컬럼추가
# 90이상 A
# 80이상 B
# 70이상 C
# 60이상 D

#컬럼 추가.
df['사회점수평가'] = 'F'

#'사회점수평가'에 사회점수를 함수로 돌려 나온 등급 넣기.
df['사회점수평가'] = df['사회'].apply(result)

print(df)

# 2. 컬럼순서 변경
# 사회점수, 사회점수평가 컬럼순서를 변경하시오.

#컬럼명을 리스트 형으로 변환
cols = list(df.columns)
print(cols)
#컬럼 순서 변경 
df = df[cols[0:8] + [cols[-1]] + [cols[-2]]]
print(df)



# 3.국어,영어,수학,과학,사회 
# 합계, 평균 컬럼을 만들고

df['합계'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']

df['평균'] = df['합계']/5
print(df)

# 4. 평균에 따른 평균평가  컬럼추가

df['평균평가'] = 'F'

print(df)

#평균에 대한 평가 넣기.

df['평균평가'] = df['평균'].apply(result)
print(df)
