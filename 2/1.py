# 2.1 加载预置的样本数据集

# 样本
from sklearn import datasets

# 加载手写数字数据集
digits = datasets.load_digits()

# 创建特征矩阵
feature = digits.data
# 查看第一个样本数据
print(feature[0])

# 创建目标向量
target = digits.target
print(target)

'''
1. load_boston: 是一个用于研究回归算法的优质数据集，包含 503 个波士顿房价的观察值。
2. load_iris: 是一个用于研究分类算法的优质数据集，包含 150 个鸢尾花尺寸的观察值。
3. load_digits: 是一个用于研究图像分类算法的优质数据集，包含 1797 个手写数字图片的观察值。
'''