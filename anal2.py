import pandas as pd
pd.set_option('display.max_columns',None)
import cufflinks as cf
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False
import seaborn as sns 


#### Attrition(사직)을 하려는 사람들의 특성 찾아보기. / 사직하려는 사람 예측.


#### 1.HR 데이터 가져오기.

hr_df = pd.read_excel('10.Mlearn\IBM_HR_archive\WA_Fn-UseC_-HR-Employee-Attrition.xlsx')
print(hr_df)
print('row숫자, col숫자 : ',hr_df.shape)
print(hr_df.head())

### col 특성 확인.
print(hr_df.describe())

####  2-1.데이터 null 값 확인.  ## int로 된 col은 null 없음 확인, 그외 col 9개는 카테고리형.

print('<0이 찍히면 없음, 0외의 숫자는 null 있음>\n',hr_df.isnull().sum())


### 사직의향자 숫자 파악.  ## 1470명 중 사직의향자 237명#########################################
print('<사직의향이 있는 사람: YES, 없는 사람 : NO> \n ' ,hr_df['Attrition'].value_counts())
#################################################################################################


# ### 그래프로 확인.##############################################################################

data = hr_df['Attrition'].value_counts()
labels = hr_df['Attrition'].value_counts().index

plt.pie(data,labels=labels, autopct='%.f%%')
plt.title('퇴직의향')
plt.show()

##################################################################################################

#### heatmap 상관관계 확인.#########################################################################
### 직급(=JobLevel)이 가장 중요해 보이며,
### 총업무년수(=TotalWorkingYears)는 직급과 월기본급(=MonthlyIncome)과 양의 상관관계를 가짐.
### 회사근속년수(=YearsAtCompany)는 업무지속년도(=YearsInCurrentRole)과 현담당자와 업무기간(=YearsWithCurrentManager)과 약간의 양의 상관관계를 가짐.

plt.figure(figsize=(13,9))
sns.heatmap(hr_df.corr(),vmax=0.8,linewidths=0.1, cmap='coolwarm', annot=True)
plt.show()
#####################################################################################################




#### 2-2. col 9개 카테고리형 확인####################################################################
## label이 될 퇴직의향. 출장빈도(=BusinessTravel), 부서(=Department), 전공(=EducationField),
## 성별(=Gender), 직책(=JobRole), 혼인상태(=MaritalStatus), 18세이상(=Over18), 야근(=OverTime)
## 등 총 9개가 카테고리형인 것을 확인 할 수 있다.
categorical_features = hr_df.select_dtypes(include=[object]).columns
print(categorical_features)
#####################################################################################################

#### 1).출장빈도(=BusinessTravel)와의 사직의향 상관관계 확인.
## 출장빈도 = 가끔 : 1043 , 자주 : 277, 없음 : 150
print(hr_df['BusinessTravel'].value_counts()) 

# ### 그래프로 확인. ################################

ax = sns.countplot(x='BusinessTravel', data=hr_df,
                   order = hr_df['BusinessTravel'].value_counts().index, 
                   hue='Attrition')

# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 30, height, ha = 'center', size = 12)
plt.title('사직의향과 출장빈도의 상관관계')
plt.xticks(rotation=45)
plt.show()


#### 2).부서(=Department)와의 사직의향 상관관계 확인.
## 부서 = 개발부(=Research & Development) : 961명 / 영업부(=Sales) : 446명 / 인사관리부(=Human Resources) : 63명.
print(hr_df['Department'].value_counts()) 

# ### 그래프로 확인. ################################

ax = sns.countplot(x='Department', data=hr_df,
                   order = hr_df['Department'].value_counts().index, 
                   hue='Attrition')

# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 30, height, ha = 'center', size = 12)
plt.title('사직의향과 부서의 상관관계')
plt.xticks(rotation=45)
plt.show()

#### 3).전공(=EducationField)과의 퇴직의향 상관관계 확인.
## 전공 = 생명과학(=Life Sciences) : 606명 / 의학(=Medical) : 464명 / 마케팅(=Marketing) : 159명
##        공학(=Technical Degree) : 132명 / 그외(=Other) : 82명 / 인사관리(=Human Resources) : 27명
print(hr_df['EducationField'].value_counts()) 

### 그래프로 확인. ################################

ax = sns.countplot(x='EducationField', data=hr_df,
                   order = hr_df['EducationField'].value_counts().index, 
                   hue='Attrition')

# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 30, height, ha = 'center', size = 12)
plt.title('사직의향과 전공의 상관관계')
plt.xticks(rotation=45)
plt.show()



#### 4).성별(=Gender)과의 퇴직의향 상관관계 확인.
## 남 : 882명 / 여 : 588명
print(hr_df['Gender'].value_counts()) 

# ### 그래프로 확인. ################################

ax = sns.countplot(x='Gender', data=hr_df,
                   order = hr_df['Gender'].value_counts().index, 
                   hue='Attrition')

# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 30, height, ha = 'center', size = 12)
plt.title('성별과 퇴직의향의 상관관계')
plt.xticks(rotation=45) 
plt.show()



#### 5).직책(=JobRole)과의 퇴직의향 상관관계 확인.
## 직책 = 판매담당(=Sales Executive) : 326명 / 분석담당(=Research Scientist) : 292명 / 
##        연구담당(=Laboratory Technician) : 259명 / 생산관리(=Manufacturing Director) : 145명 /
##        헬스케어보조(=Healthcare Representative) : 131명 / 관리자(=Manager) : 102명 / 
##        판매보조(=Sales Representative) : 83명 / 분석관리자(=Research Director) 80명 /
##        인사담당(=Human Resources) : 52명
print(hr_df['JobRole'].value_counts()) 

# ### 그래프로 확인. ################################

ax = sns.countplot(x='JobRole', data=hr_df,
                   order = hr_df['JobRole'].value_counts().index, 
                   hue='Attrition')

# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 30, height, ha = 'center', size = 12)
plt.title('직책과 퇴직의향의 상관관계')
plt.xticks(rotation=45)
plt.show()



#### 6).혼인상태(=MaritalStatus)와 퇴직의향 상관관계 확인.
## 혼인상태 = 결혼 : 673명 / 독신 : 470명 / 이혼 : 327명
print(hr_df['MaritalStatus'].value_counts()) 

# ### 그래프로 확인. ################################

ax = sns.countplot(x='MaritalStatus', data=hr_df,
                   order = hr_df['MaritalStatus'].value_counts().index, 
                   hue='Attrition')

# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 30, height, ha = 'center', size = 12)
plt.title('혼인상태와 퇴직의향의 상관관계')
plt.xticks(rotation=45)
plt.show()




#### 7).야근(=OverTime)과의 퇴직의향 상관관계 확인.
## 야근이 있다 : 416명 / 야근이 없다 : 1054명
print(hr_df['OverTime'].value_counts()) 

# ### 그래프로 확인. ################################

ax = sns.countplot(x='OverTime', data=hr_df,
                   order = hr_df['OverTime'].value_counts().index, 
                   hue='Attrition')

# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 30, height, ha = 'center', size = 12)
plt.title('야근과 퇴직의향의 상관관계')
plt.xticks(rotation=45)
plt.show()


#### 그래프로 알 수 있는 사실.######################################################################

## 1. 출장이 잦은 임직원일수록 퇴직의향이 높은 것을 알 수 있음.
## 2. 판매담당이나 판매보조에 있는 판매부서가 연구부서보다 퇴직의향이 높다.
## 3. 여성보다 남성들이 퇴직의향이 더 높다.
## 4. 남성의 야근 비율이 더 많다.
#####################################################################################################

##### 2-3. col 26개 숫자형 확인 ###########################################################################

#['사번(=EmployeeNumber'), 나이(='Age'), 일급(='DailyRate'), 출퇴근거리(='DistanceFromHome'), 
# 최종학위(='Education'), 고용상태체크(='EmployeeCount'), 업무환경 만족도(='EnvironmentSatisfaction'), 
#  시급(='HourlyRate'), 업무집중도(='JobInvolvement'), 직책(='JobLevel'), 
#  업무만족도(='JobSatisfaction'), 월기본급(='MonthlyIncome'), 월실수령액(='MonthlyRate'), 
#  팀원숫자(='NumCompaniesWorked'), 급여상승율(='PercentSalaryHike'), 업무평가(='PerformanceRating'),
#  대인관계만족도(='RelationshipSatisfaction'), 업무기준시간(='StandardHours'), 
#  스톡옵션급수(='StockOptionLevel'), 업무년차(='TotalWorkingYears'), 연수기간(='TrainingTimesLastYear'),
#  워라밸(='WorkLifeBalance'), 근속년수(='YearsAtCompany'), 업무지속년도(='YearsInCurrentRole'), 
#  마지막진급년도(='YearsSinceLastPromotion'), 현재담당자와의 업무년도(='YearsWithCurrManager')]

numberical_features = [feature for feature in hr_df.columns if hr_df[feature].dtype !='O']
print(numberical_features)
## 중간 값 확인.
print(hr_df['Age'].nunique())

#### 1) 나이 분포 확인.
## 나이의 대부분은 약 25~ 40세 사이가 가장 많이 분포되어 있다.
## 43세가 중간.
sns.displot(hr_df['Age'])
plt.title('연령분포도')
plt.show()

#### 2) 최종학위와 퇴직의향과의 상관관계 분석.##########################################
# 4년제졸    572명
# 석사      398명
# 전문대졸    282명
# 고졸이하    170명
# 박사       48명


edu_map = {1 :'고졸이하', 2: '전문대졸', 3 :'4년제졸', 4 :'석사', 5: '박사'}
print(hr_df['Education'].map(edu_map).value_counts())


# ### 그래프로 확인 
ax = sns.countplot(x=hr_df['Education'].map(edu_map), 
                   hue='Attrition', data=hr_df)
# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 30, height, ha = 'center', size = 12)
plt.title('최종학위와 퇴직의향의 상관관계')
plt.show()
#########################################################################################
### 

#### 3) 업무환경만족도와 퇴직의향과의 상관관계 분석.
# 보통        287명
# 만족        453명
# 매우만족   446명
# 불만족     284명

st_map = {1 :'불만족', 2: '보통', 3 :'만족', 4 :'매우만족'}
print(hr_df['EnvironmentSatisfaction'].map(st_map).value_counts())


# ### 그래프로 확인 
ax = sns.countplot(x=hr_df['EnvironmentSatisfaction'].map(st_map), 
                   hue='Attrition', data=hr_df)
# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 10, height, ha = 'center', size = 12)
plt.title('업무환경만족도와 퇴직의향의 상관관계')
plt.show()
#########################################################################################
### 

#### 4) 업무집중도와 퇴직의향과의 상관관계 분석.
# 좋음          868명
# 보통          375명
# 매우좋음      144명
# 나쁨           83명
con_map = {1 :'나쁨', 2: '보통', 3 :'좋음', 4 :'매우좋음'}
print(hr_df['JobInvolvement'].map(con_map).value_counts())


# ### 그래프로 확인 
ax = sns.countplot(x=hr_df['JobInvolvement'].map(con_map), 
                   hue='Attrition', data=hr_df)
# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 10, height, ha = 'center', size = 12)
plt.title('업무집중도와 퇴직의향의 상관관계')
plt.show()
#########################################################################################
### 


#### 그래프로 알 수 있는 사실.######################################################################

## 1. 업무환경만족도에서 매우만족~보통이 퇴직의향이 없는 것과 상관이 별로 없는 것으로 보인다.
## 2. 업무집중도는 대부분이 좋은 것으로 보인다.
#####################################################################################################

#### 5) 월기본급 분포도.
### 3-5.월기본급분포-1

sns.displot(hr_df['MonthlyIncome'])
plt.title('월기본급 분포')
plt.show()

### 3-5.월기본급분포-2

plt.figure(figsize=(6,5))
sns.boxplot(hr_df['MonthlyIncome'])
plt.title('월기본급 분포')
plt.show()


#########################################################################################

#### 6) 직급과 퇴직의향의 상관관계
# 사원    543명
# 대리    534명
# 과장    218명
# 차장    106명
# 부장     69명

level_map = {1 :'사원', 2: '대리', 3 :'과장', 4 :'차장', 5:'부장'}
print(hr_df['JobLevel'].map(level_map).value_counts())


# ### 그래프로 확인 
ax = sns.countplot(x=hr_df['JobLevel'].map(level_map), 
                   hue='Attrition', data=hr_df)
# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 10, height, ha = 'center', size = 12)
plt.title('직급과 퇴직의향의 상관관계')
plt.show()



#########################################################################################

#### 7) 스톡옵션등급과 퇴직의향의 상관관계


level_map = {0 :'낮음', 1: '약간낮음', 2 :'중간', 3 :'높음'}
print(hr_df['StockOptionLevel'].map(level_map).value_counts())


# ### 그래프로 확인 
ax = sns.countplot(x=hr_df['StockOptionLevel'].map(level_map), 
                   hue='Attrition', data=hr_df)
# countplot에 값 표시
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., 
            height + 10, height, ha = 'center', size = 12)
plt.title('스톡옵션등급과 퇴직의향의 상관관계')
plt.show()

#########################################################################################

#### 그래프로 알 수 있는 사실.######################################################################

## 1. 월기본급의 중간 값은 약 5100을 가지는 것으로 보인다.
## 2. 사원급이 가장 많이 퇴직의향을 가진 것을 알 수 있다.
## 3. 스톡옵션이 낮음(거의 없음)이 퇴직의향이 약간 높음을 알 수 있다.
#####################################################################################################



### 이외 필요 없는 컬럼 날리기 
hr_df.drop(['EmployeeCount','EmployeeNumber','StandardHours','Over18'],axis=1, inplace=True)
# print(hr_df)

#### 3.데이터 분석 준비!

### 3-1.카테고리형 컬럼 인코딩 (8개)
categorical_features = hr_df.select_dtypes(include=[object]).columns
# print('카테고리형 컬럼 : \n',hr_df[categorical_features].head())


### 1)label 퇴직의향(=Attrition) 숫자로 변경.
hr_df['Attrition'] = hr_df['Attrition'].replace({'No':0,'Yes':1})

### 2)data의 YES or NO 인 야근(=Overtime), 성별(=Gender) 숫자로 변경.
hr_df['OverTime'] = hr_df['OverTime'].map({'No':0,'Yes':1})
hr_df['Gender'] = hr_df['Gender'].map({'Male':0,'Female':1})

### 3)그외 모두 숫자로 변경.
##출장빈도(=BusinessTravel), 부서(=Department), 전공(=EducationField), 직책(=JobRole), 혼인상태(=MaritalStatus)
cat_cols = ['BusinessTravel','Department','EducationField','JobRole','MaritalStatus']
for col in cat_cols:
    map_dict = {k:i for i, k in enumerate(hr_df[col].value_counts().index,0)}
    hr_df[col] = hr_df[col].map(map_dict)
        
# print(hr_df) ### 컬럼 확인.

hr_df.corr()['Attrition'][:-1].sort_values(ascending=False)
print("변경 후 컬럼 확인 : ",hr_df)

#### 4)상관관계 재확인. heatmap 사용
# plt.figure(figsize=(13,9))
# sns.heatmap(hr_df.corr(),vmax=0.8,linewidth=0.1,cmap='coolwarm',annot=True)
# plt.show()


#### 4.분석하기.
from sklearn.ensemble import ExtraTreesClassifier ##앙상블 패키지 중 익스트림 랜덤 트리

data = hr_df.drop('Attrition',axis=1)
label = hr_df['Attrition']
# print(data)
# print(label)

#### 1)상관관계 높은 col 추려내기
et = ExtraTreesClassifier()
et.fit(data,label)

# ### 2)랜덤트리에서 자동제공되는 중요도.
feat_importance = et.feature_importances_

# ### 그래프로 확인. 중요도를 적용하여 각 데이터 컬럼에 넣기.

plt.figure(figsize=(11,9))
feat_imp = pd.Series(et.feature_importances_, index=data.columns)
feat_imp.nlargest(20).plot(kind='barh')
plt.title('상관관계확인')
plt.show()


#### 그래프로 알 수 있는 사실.######################################################################

## 1. 야근, 특근, 잔업 등 아무튼 그렇게 불리는 (=OverTime)이 퇴직의향과 상관관계가 큼을 알 수 있다.
## 2. 나이가 두번째 상관관계를 가지고 있었다.
## 3. 그외 직무근속년수와 월기본급, 직무환경만족도 등의 순서대로 상관관계를 가지고 있었다.
#####################################################################################################


### min_max 스캐일링. (스탠다드스캐일링과 비슷함.)

from sklearn.preprocessing import MinMaxScaler

mm = MinMaxScaler()

data_scaled = mm.fit_transform(data)

# ### 5-1 스캐일링 후 재 분석.

et.fit(data_scaled,label)

# feature_importance_1 = pd.Series(et.feature_importances_, index=data.columns)
# print(feature_importance_1)

# plt.figure(figsize=(10,9))
# feature_importance_1.nlargest(20).plot(kind='barh')
# plt.title('정규화 후 상관관계확인')
# plt.show()

#### 정규화 후에도 큰 변화는 없다. ##################################################################

####5. 머신러닝
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


####5-1 데이터 나누기.

train_data, test_data, train_label, test_label = \
    train_test_split(data_scaled,label,test_size=0.25,random_state=42)
# print(train_data)
# print(test_data)

### 5-2. 알고리즘 선택.

log_clf = LogisticRegression()
svc_clf = SVC()
knn_clf = KNeighborsClassifier()
dt_clf = DecisionTreeClassifier()
rf_clf = RandomForestClassifier()

### 5-3. 5개 알고리즘의 스코어 체크.
# 정확도 스코어 체크 및 테스트데이터로 예측  ## 테스트시의 정확도.
from sklearn.metrics import accuracy_score
print("="*60)
for clf in [log_clf, svc_clf, knn_clf, dt_clf, rf_clf]:
    clf.fit(train_data, train_label)
    
    predict1 = clf.predict(train_data)
    predict2 = clf.predict(test_data)
    predict2_1 = clf.predict(test_data[:5])
    
    print(clf.__class__.__name__,"의 훈련 정확도 :", accuracy_score(train_label,predict1))
    print(clf.__class__.__name__,"의 테스트 정확도 :", accuracy_score(test_label,predict2),"\n예측테스트(5개)(0:NO / 1:YES) : ",predict2_1)
    print("="*60)
    
# #### 6. 정확도 올리기. (ADABOOST, XGBOOST, Hyperparameter Tuning)


### 6-1. Adaboost 사용.
from sklearn.ensemble import AdaBoostClassifier
from xgboost import XGBClassifier

boost = AdaBoostClassifier(base_estimator = DecisionTreeClassifier(max_depth=1), n_estimators=500, algorithm='SAMME',learning_rate=0.01)
boost.fit(train_data,train_label)
predictions = boost.predict(test_data)
print("AdaBoost정확도:",accuracy_score(test_label,predictions))


print("훈련시 정확도:",boost.score(train_data,train_label))
print("테스트시 정확도:",boost.score(test_data,test_label))
print("Ada_예측(0:NO / 1:YES)",boost.predict(test_data[:5]))
print("="*60)

### 6-2. XGboost 사용.

xgb = XGBClassifier()

xgb.fit(train_data,train_label)
print("훈련시 정확도:",xgb.score(train_data,train_label))
print("테스트시 정확도:",xgb.score(test_data,test_label))
print("XGB_예측(0:NO / 1:YES)",xgb.predict(test_data[:5]))
print("="*60)

### 6-3. Hyperparameter Tuning 사용.
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score

### 최적 값 찾기. (RamdomForest)

n_estimators = [int(x) for x in np.linspace(100,1200,12)]
max_depth = [int(x) for x in np.linspace(5,30,1)]
criterion = ['gini','entropy']
min_samples_split = [2,5,7,10]
min_samples_leaf = [2,5,8]

random_grid = dict(n_estimators=n_estimators, max_depth=max_depth, criterion=criterion,
                  min_samples_split=min_samples_split,min_samples_leaf=min_samples_leaf)
# print(random_grid) ### 각 param 전체 보기.
print("="*100)

rf_clf = RandomForestClassifier()
rf_random = RandomizedSearchCV(rf_clf, param_distributions=random_grid, cv=5, n_iter=10,
                               random_state=42, n_jobs=-1,verbose=1,)

rf_random.fit(train_data, train_label)

print('RandomForest예측 정확도 : ',rf_random.best_score_)
print("RandomForest적정 params : ",rf_random.best_params_)


### 최적 값 찾기. (XGBoost)
n_estimators = [int(x) for x in np.linspace(100,1000,10)]
max_depth = [int(x) for x in np.linspace(6,30,5)]
learning_rate = [0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.01]
min_child_weight = list(range(1,10))

xg_grid = dict(n_estimators=n_estimators, max_depth=max_depth, learning_rate=learning_rate, 
               min_child_weight=min_child_weight)
# print(xg_grid) ### 각 param 전체 보기.
print("="*100)

xgb = XGBClassifier()
xgb_random = RandomizedSearchCV(xgb, param_distributions=xg_grid, cv=5, random_state=42,
                               n_iter=10,scoring="accuracy",n_jobs=-1,verbose=1)
xgb_random.fit(train_data, train_label)

print("XGB최적화 예측 정확도: ",xgb_random.best_score_)
print("XGB최적화 적정 params: ",xgb_random.best_params_)
print("="*100)
xgb_f = XGBClassifier(n_estimators= 600, min_child_weight=7,max_depth=24, learning_rate=0.004)

xgb_f.fit(train_data,train_label)

xgb_final_train_score = xgb_f.score(train_data,train_label)
xgb_final_test_score = xgb_f.score(test_data,test_label)
xgb_final_result = xgb_f.predict(test_data[:10])

print('xgb 최적 훈련 정확도 :',xgb_final_train_score)
print('xgb 최적 테스트 정확도 :',xgb_final_test_score)
print('xgb 최적 예측 (0:계속 근무 / 1: 때려칠 것임) :',xgb_final_result)


#### 최종 ##################################################################

# xgb 최적 훈련 정확도 : 0.9001814882032668
# xgb 최적 테스트 정확도 : 0.8559782608695652
# xgb 최적 예측 (0:계속 근무 / 1: 때려칠 것임) : [0 0 0 0 0 0 0 0 0 0]

############################################################################