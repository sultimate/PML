# 1.17 计算两个向量的内积

import numpy as np

alpha = np.array([1, 2, 3])
beta = np.array([4, 5, 6])

print(np.dot(alpha, beta))
print(alpha @ beta)