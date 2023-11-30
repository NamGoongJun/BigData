"""
1) 생존자와 사망자 수를 구하시오.
2) 남성과 여성의 생존률을 구하시오.
3) 객실 등급별 생존자 수를 구하시오.
4) 나이대별 생존자 수를 구하시오. (10대 20대 이렇게)
"""
import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
print(titanic.info())
print(titanic.head())

# 1)
survived_people = titanic[titanic["survived"] == 1]["survived"].count()
dead_people = titanic[titanic["survived"] == 0]["survived"].count()
print(f"생존자 수 : {survived_people}명")
print(f"생존자 수 : {dead_people}명")

# 2)
male_survived = titanic[(titanic["survived"] == 1) & (titanic["sex"] == "male")]["survived"].count()
female_survived = titanic[(titanic["survived"] == 1) & (titanic["sex"] == "female")]["survived"].count()
male_count = titanic[(titanic["sex"] == "male")]["sex"].count()
female_count = titanic[(titanic["sex"] == "female")]["sex"].count()
print(male_count, female_count)
print(male_survived/male_count, female_survived/female_count)

# 3)
pclass_survived = titanic.groupby('pclass')['survived'].sum()
# pclass_survived = titanic[titanic['survived']==1].groupby(['pclass']).size()
print(pclass_survived)

# 4)
age_survived = titanic.groupby(pd.cut(titanic['age'], bins=range(0, 81, 10)))['survived'].sum()
print(age_survived)