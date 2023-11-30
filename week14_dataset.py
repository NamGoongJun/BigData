"""
1) 생존자와 사망자 수를 구하시오.
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