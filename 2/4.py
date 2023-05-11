# 2.4 加载 Excel 文件(需要安装 openpyxl 依赖)

import pandas as pd

url = '2/data.xlsx'

f'''
1. sheetname 可以是名字的字符串。也可以是指向数据表位置的整数（从 0 开始编号）
   还可以是 array, 如 [0, 1, 2, 'Monthly Sales'], 即一次加载多张表。将返回一个字典: {'name': pandas DateFrame}
2. 行从 0 开始编号
'''
dataframe = pd.read_excel(url, sheet_name=0, header=0)

print(dataframe.head(2))