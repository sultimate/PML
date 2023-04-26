# 1.4 在向量或矩阵中选择一个元素

import numpy as np

vector = np.array([1, 2, 3, 4, 5, 6])

print(vector[2])
print(vector[:])    # 选择一个向量的所有元素
print(vector[:3])   # 从第1个，到第3个（包含）
print(vector[3:])   # 第3个之后的（不含），所有元素
print(vector[-1])   # 最后一个元素

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix[1, 1])
print(matrix[:2, :])    # 前面控制行，后面控制列。选择1、2行的所有列。选择的结果还是 matrix
print(matrix[:, 1:2])   # 选择第2列的所有行