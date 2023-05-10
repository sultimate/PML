'''
2.1 生成一个仿真数据集：有三个方法非常有用
 1. 常用 make_regression 生成适合做线性回归的仿真数据集
 2. 用 make_classification 生成适合做分类的数据集
 3. 用 make_blobs 生成适合做聚类处理的数据集
其中：
 1. n_informative 确定用于生成目标向量的特征数量；若 n_informative 的值，比总的特征数 n_features 小，
    则生成的数据集将包含多余的特征。这些特征可用特征选择技术识别。
 2. 利用 weights 参数，生成不均衡的数据集。如 weights = [.25, .75], 在数据集中, 25% 的观察值属于第一个分类, 75% 属于第二个分类。
 3. centers 参数决定要生成多少个聚类。
'''

from sklearn.datasets import make_regression

# 生成特征矩阵、目标向量、模型的系数
features, target, coefficients = make_regression(n_samples = 100,
                                                 n_features = 3,
                                                 n_informative = 3,
                                                 n_targets = 1,
                                                 noise = 0.0,
                                                 coef = True,
                                                 random_state = 1)

print(features[:3])
print(target[:3])

from sklearn.datasets import make_classification

features, target = make_classification(n_samples = 100,
                                       n_features = 3,
                                       n_informative = 3,
                                       n_redundant = 0,
                                       n_classes = 2,
                                       weights = [.25, .75],
                                       random_state = 1)

print(features[:3])
print(target[:3])

from sklearn.datasets import make_blobs

features, target = make_blobs(n_samples = 100,
                              n_features = 2,
                              centers = 3,
                              cluster_std = 0.5,
                              shuffle = True,
                              random_state = 1)

print(features[:3])
print(target[:3])

# 将 make_blobs 生成的聚类，可视化
import matplotlib.pyplot as plt

# 查看散点图
plt.scatter(features[:,0], features[:,1], c=target)
plt.show()