import pandas as pd
# ファイルと文字コードの指定
test_data = pd.read_csv('test.csv', encoding="UTF-8")
print (test_data)
print ("---------------------------------")

# データ型の判別
print (type(test_data))
print ("---------------------------------")

# 最大表示行を制限
pd.set_option('display.max_rows', 2)
print (test_data)
print ("---------------------------------")

# 設定のリセット
pd.reset_option('display.max_rows')
print (test_data)
print ("---------------------------------")

# 最大表示列を制限
pd.set_option('display.max_columns', 2)
print (test_data)
print ("---------------------------------")

# 設定のリセット
pd.reset_option('display.max_columns')
print (test_data)
print ("---------------------------------")

# 初めの（２）行を取り出すデフォルトは５
print(test_data.head(2))
print ("---------------------------------")

# 最後の（３）行を取り出す
print (test_data.tail(3))
print ("---------------------------------")

# ランダムに（４）行を取り出す
print (test_data.sample(4))
print ("---------------------------------")

# 行数、列数、列名、各データ型、使用しているメモリー数
# non-nullは欠損値の有無つまり無し
#  0   Name        8 non-null      object
#  1   Age         8 non-null      int64 
#  2   Gender      8 non-null      object
#  3   Occupation  8 non-null      object
#  4   Income      8 non-null      int64 
print (test_data.info())
print ("---------------------------------")

# 平均値、標準偏差、最大値、最小値など
# count   8.000000       8.000000
# mean   35.000000   79375.000000
# std     6.524678   20255.069912
# min    27.000000   55000.000000
# 25%    30.250000   67500.000000
# 50%    34.000000   77500.000000
# 75%    39.750000   86250.000000
# max    45.000000  120000.000000
print (test_data.describe())
print ("---------------------------------")

# 小数点以下を四捨五入
#         Age    Income
# count   8.0       8.0
# mean   35.0   79375.0
# std     7.0   20255.0
# min    27.0   55000.0
# 25%    30.0   67500.0
# 50%    34.0   77500.0
# 75%    40.0   86250.0
# max    45.0  120000.0
print (test_data.describe().round(0))
print ("---------------------------------")