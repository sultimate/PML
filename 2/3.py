# 2.3 加载 CSV（逗号分隔符：Comma-Separated Values）文件

import pandas as pd

# url = 'https://tinyurl.com/simulated_data'
url = '2/data.csv' # 根据执行命令的相对路径
# url = 'data.csv'

# 加载数据集
dataframe = pd.read_csv(url)

# 查看头两行
print(dataframe.head(2))

'''
加载 CSV 数据前：
1. 首先浏览文件内容：了解数据集结构，以及加载时需要设置什么参数
2. 默认 CSV 的分隔符是逗号, 但也可以是其他分隔符, 如制表符。sep 参数设置加载时的分隔符
3. csv 文件格式固定, 一般为: 文件第一行为数据列头。header 参数指定是否存在数据头这一行，以及设定它的位置. 
   如果没有, 则设置 header = None.
'''