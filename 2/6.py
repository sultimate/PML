# 2.6 查询 SQL（Structured Query Language）数据库

import pandas as pd
from sqlalchemy import create_engine

database_connection = create_engine('sqlite:///2/data.db')

dataframe = pd.read_sql_query('select * from people', database_connection)

print(dataframe.head(2))