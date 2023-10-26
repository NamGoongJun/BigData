import numpy as np

def info(x):
    print(f"배열의 차원(rank)은 {x.ndim}차원 입니다.")
    print(f"배열의 shpae는 {x.shape}입니다.")
    print(f"원소의 개수는 {x.size}개 입니다.")


np_1d = np.arange(1, 20, 2)
print(np_1d)
info(np_1d)
np_1d = np_1d.reshape(1, 2, 5) # 면, 행, 열
print(np_1d)
info(np_1d)