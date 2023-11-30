import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

titanic = sns.load_dataset('titanic') # 데이터 로딩
# print(titanic.info())
titanic = titanic.drop(['who', 'deck', 'embark_town', 'alive', 'class', 'adult_male', 'alone'], axis=1) # 불필요한 열 제거
titanic = titanic.dropna() # 결측치가 있는 행 제거
# 수치 데이터가 아닌 피쳐를 숫자로 변환
titanic['sex'] = titanic['sex'].map({'male' : 0, 'female' : 1})
titanic['embarked'] = titanic['embarked'].map({'S' : 0, 'C' : 1, 'Q' : 2})
# 특성, 타켓 분리
X = titanic.drop('survived', axis=1)
y = titanic['survived']

# 훈련, 테스트 셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=1)
# 모델 생성
model = LogisticRegression(solver='liblinear') # 로지스틱 회귀 모델 적용
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"정확도 : {accuracy_score(y_test, y_pred)}")