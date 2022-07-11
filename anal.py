import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

#### attrtion(사직)을 하려는 사람들의 특성 찾아보기. / 사직하려는 사람 예측.


#### HR 데이터 가져오기.


hr_df = pd.read_excel('10.Mlearn\IBM_HR_archive\WA_Fn-UseC_-HR-Employee-Attrition.xlsx')
# print(hr_df)

# print(hr_df.describe())
# print(hr_df.index)

### 컬럼 name 확인.
# print(hr_df.columns)


import seaborn as sns
#### 숫자 데이터의 상관관계 확인. #####################################################
# NumericBV=hr_df[['DailyRate',
#         'DistanceFromHome', 'Education', 
#         'EnvironmentSatisfaction', 'HourlyRate',
#        'JobInvolvement', 'JobLevel', 'JobSatisfaction',
#         'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
#         'PercentSalaryHike', 'PerformanceRating',
#        'RelationshipSatisfaction', 'StockOptionLevel',
#        'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
#        'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
#        'YearsWithCurrManager']]
# NumericBV['Attrition']=hr_df['Attrition']

# NumericBVData = NumericBV.melt(id_vars=['Attrition'])
# NumericDataGD = sns.FacetGrid(NumericBVData, col='variable',sharex=False,sharey=False,dropna=True,size=5,col_wrap=5,  hue='Attrition' )
# histPlot=NumericDataGD.map(sns.kdeplot,'value' )
# NumericDataGD.add_legend()
# plt.show()


#####################################################################################
# import seaborn as sns 
#### 업무환경과의 상관관계.
# sns.barplot(data= hr_df, x=hr_df['Attrition'], y=hr_df['EnvironmentSatisfaction'])
# plt.show()
# #### 업무만족도와의 상관관계. 
# sns.barplot(data= hr_df, x=hr_df['Attrition'], y=hr_df['JobSatisfaction'])
# plt.show()
# #### 출장여부와의 상관관계. 
# sns.barplot(data=hr_df, x=hr_df['Attrition'], y=data_char['BusinessTravel'])
# plt.show()
#####################################################################################

### 컬럼 확인시 EmployeeCount, Over18, StandardHours, EmployeeNumber 는 추론에 아무런 데이터를 제공하지 않는다.

data_int = hr_df[['Age','DailyRate',
        'DistanceFromHome', 'Education', 
        'EnvironmentSatisfaction', 'HourlyRate',
       'JobInvolvement', 'JobLevel', 'JobSatisfaction',
        'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
        'PercentSalaryHike', 'PerformanceRating',
       'RelationshipSatisfaction', 'StockOptionLevel',
       'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
       'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
       'YearsWithCurrManager']]

# print(data_int)



data_char = hr_df[['Attrition','BusinessTravel','Department','EducationField','Gender','JobRole'
                   ,'MaritalStatus','OverTime']]
# print(data_char)



### 원핫 인코더(char 데이터 숫자로 변경) ##

from sklearn.preprocessing import OneHotEncoder

# ### 인코딩할 라벨 확인. ###################

for i in data_char:
    print(i)
    print(data_char[i].value_counts())
    print()
# ##########################################

### 원핫 인코딩.#############################

data_char_t = pd.get_dummies(data_char)
# print(data_char_t)


#############################################

# #### data 합치기.
data = data_int.join(data_char_t)
print(data)
#############################################################################################################
## data의 분석에서 컬럼의 영향력 파악분석

# scale_columns = ['Age','DailyRate',
#         'DistanceFromHome', 'Education', 
#         'EnvironmentSatisfaction', 'HourlyRate',
#        'JobInvolvement', 'JobLevel', 'JobSatisfaction',
#         'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
#         'PercentSalaryHike', 'PerformanceRating',
#        'RelationshipSatisfaction', 'StockOptionLevel',
#        'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
#        'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
#        'YearsWithCurrManager']

# corr =data[scale_columns].corr(method='pearson')
# show_cols = ['Age','DailyRate','DistanceFromHome', 'Education', 
#         'EnvironmentSatisfaction', 'HourlyRate',
#        'JobInvolvement', 'JobLevel', 'JobSatisfaction',
#         'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
#         'PercentSalaryHike', 'PerformanceRating',
#        'RelationshipSatisfaction', 'StockOptionLevel',
#        'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
#        'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
#        'YearsWithCurrManager']

# hm = sns.heatmap(corr.values,
#                  cbar = True,
#                  annot = True,
#                  square = True,
#                  fmt='.2f',
#                  annot_kws = {'size':15},
#                  yticklabels=show_cols,
#                  xticklabels=show_cols
#                  )
# plt.tight_layout()
# plt.xticks(rotation=50)
# plt.show()
#############################################################################################################


#### 핫 맵으로 알 수 있는 것들.

## 나이=Age, 성과도=PerformanceRating, 팀원수 = NumCompaniesWorked, 기본급=MonthlyIncome, 근속년수=YearsAtCompany, 
## 업무 지속기간 =YearsInCurrentRole, 마지막진급한 해=YearsSinceLastPromotion, 현 담당자와의 업무기간=YearsWithCurrManager, 직급=JobLevel 등이 
## 퇴직의사와 영향이 큰 것을 알 수 있다.




#### 숫자형 정규화, 표준화
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
data_scaled = ss.fit_transform(data)
# print(data_scaled)



### 데이터에 영향을 주는 인자  확인. :영향력이 너무 높거나, 너무 낮은 것을 확인.
### 첫번째 컬럼 vif, 두번째 컬럼 : 컬럼명 출력.
data_v = data[data.columns.difference(['Attrition'])]
from statsmodels.stats.outliers_influence import variance_inflation_factor 
vif = pd.DataFrame()
vif['VIF factor'] = [variance_inflation_factor(data_v.values,i) for i in range(data_v.shape[1])]
vif['features'] = data_v.columns
print(vif.round(1))

### 인자 확인에서 알 수 있는 것들.
## 성과도=PerformanceRating, 팀원수 = NumCompaniesWorked, 기본급=MonthlyIncome, 근속년수=YearsAtCompany, 
## 업무 지속기간 =YearsInCurrentRole, 마지막진급한 해=YearsSinceLastPromotion, 현 담당자와의 업무기간=YearsWithCurrManager, 직급=JobLevel 등이 
## heatmap에서와 같이 가장 큰 영향을 미친다는 것을 알 수 있다.


#### label 선택.
label = hr_df['Attrition'].to_numpy()
# print(label)


#### 데이터 나누기.

from sklearn.model_selection import train_test_split

train_data, test_data, train_label, test_label = \
    train_test_split(data,label,test_size = 0.2,random_state=42)


# print('훈련용 데이터: ',train_data)
# print('훈련용 라벨: ',train_label)
print("="*60)
# print(test_data)
# print(test_label)


#### 알고리즘 선택 및 훈련.

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier  ### 앙상블 부스팅 중 최적화 부스팅 방식.
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

#### 알고리즘 선택.

dt = DecisionTreeClassifier()
lr = LogisticRegression()
rfc = RandomForestClassifier()

### 알고리즘 훈련.

dt.fit(train_data,train_label)
# lr.fit(train_data,train_label)
rfc.fit(train_data,train_label)

### 예측.

dtr = dt.predict(test_data[:20])
# lrr = lr.predict(test_data[:10])
rfcr = rfc.predict(test_data[:20])

print('dt의 결과값 : ',dtr)
# print('lr의 결과값 : ',lrr)
print('rfc의 결과값 : ',rfcr)

### 예측 정확도
print("="*60)

dtr_score1 = dt.score(train_data,train_label)
dtr_score2 = dt.score(test_data,test_label)
print('dtr 훈련 정확도 : ',dtr_score1)
print('dtr 테스트 정확도 : ',dtr_score2)
print("="*60)
# lrr_score1 = dt.score(train_data,train_label)
# lrr_score2 = dt.score(test_data,test_label)
# print('lrr 훈련 정확도 : ',lrr_score1)
# print('lrr 테스트 정확도 : ',lrr_score2)
print("="*60)
rfcr_score1 = dt.score(train_data,train_label)
rfcr_score2 = dt.score(test_data,test_label)
print('rfcr 훈련 정확도 : ',rfcr_score1)
print('rfcr 테스트 정확도 : ',rfcr_score2)
print("="*60)


#### XGB 용 작업.

###라벨 Yes : 1 , No : 0으로 변환.
xgb_label = hr_df['Attrition'].map({'Yes':1, 'No':0})
# print(xgb_label)

###데이터 나누기 (다른 것과 비교하기 위해 똑같이 옵션 주기.)
train_data, test_data, train_label, test_label = \
    train_test_split(data,xgb_label,test_size = 0.2,random_state=42)
    
###XGB 선택하기.   
xgb = XGBClassifier()

###XGB 알고리즘 훈련.
xgb.fit(train_data,train_label)

###XGB 예측.
xgbr = xgb.predict(test_data[:20])
print('xgb의 결과값(Yes:1, No:0) : ',xgbr)

###XGB 정확도 확인.
xgb_score1 = xgb.score(train_data,train_label)
xgb_score2 = xgb.score(test_data,test_label)
print('xgb 훈련 정확도 : ',xgb_score1)
print('xgb 테스트 정확도 : ',xgb_score2)
print("="*60)
