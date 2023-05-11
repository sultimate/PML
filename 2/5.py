# 2.5 加载 json 文件

import pandas as pd

url = '2/data.json'

'''
orient 可取 split、records、index、columns、values.
columns: 文件中, 数据是按列存储的。如 {"name": {"id1": "Tom", "id2": "Jimmy"}, "age": {"id1": 10, "id2": 20}}
'''

dataframe = pd.read_json(url, orient = 'columns')

print(dataframe.head(2))

# 还有一个有用的工具 json_normalise, 能将半结构化的 json 转换为 pd.DF