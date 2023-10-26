import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A' : [1, 2, np.nan, 4],
    'B' : [5, np.nan, 7, 8],
    'C' : [9, 10, 11, np.nan]
})

# # 결측치 처리하는 방법 1
# df.fillna(df.mean(), inplace=True) # inplace=True 는 현제 데이터 프레임을 교체
# print(df)

# # 2
# for col in df.columns:
#     # print(col)
#     df[col] = np.where(pd.isnull(df[col]), np.mean(df[col]), df[col])
# print(df)

# 3
from sklearn.impute import SimpleImputer # 결측값 전용 처리 클래스 활용
i = SimpleImputer(strategy='mean') # median, most frequent
df = pd.DataFrame(i.fit_transform(df), columns=df.columns)
print(df)