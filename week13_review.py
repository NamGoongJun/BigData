import numpy as np
import seaborn as sns
import pandas as pd

a1 = np.ones(5)
a2 = np.array([1, 1, 1, 1, 1])
a3 = np.arange(5) * 0 + 1
a4 = np.zeros(5) + 1
a5 = np.linspace(1, 1, 5)
a6 = np.full(5, 1)
print(a1, a2, a3, a4, a5, a6)
titanic = sns.load_dataset('titanic')

print(titanic.isnull())

# print(type(titanic))
# print(titanic.describe())
# print(titanic.info())
# print(titanic)