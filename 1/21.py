# 1.21 生成随机数

import numpy as np

# 设置随机数种子
np.random.seed(0)

# 生成 3 个 0 到 1.0 之间的随机浮点数
print(np.random.random(3))
# 生成 3 个 1 到 10 之间的随机整数
print(np.random.randint(0, 11, 3))

# 从均值是 0，标准差是 1.0 的正态分布中抽取 3 个数
print(np.random.normal(0, 1, 3))
# 从均值是 0，散布程度是 1.0 的 logistic（逻辑）分布中抽取 3 个数
print(np.random.logistic(0, 1, 3))
# 从大于或等于 1.0，小于 2.0 的范围中抽取 3 个数
print(np.random.uniform(1, 2, 3))