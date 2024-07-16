# 该脚本的作用：用来向数据库导入商品/金融期货/期权行情数据
import pandas as pd
import os, pymysql, re
import datetime as dt



# 1、导入上期所和上海国际能源的商品期货/期权行情数据
# #打开数据库连接
# db = pymysql.connect(host = 'localhost', user = 'root', passwd='09221017ZB', port= 3306, db='python_mysql', charset='utf8')
# #使用cursor()方法创建一个游标对象cursor
# cursor = db.cursor()

# path1 = "C:\\Users\\29433\\Desktop\\上期所\\"
# for file_name1 in os.listdir(path1):
#     df1 = pd.read_excel(path1 + file_name1, sheet_name="所内合约行情报表")
#     df1["code"] = df1["code"].str.upper()
#     df1["date"] = df1["date"].map(lambda x: dt.datetime.strptime(str(x), "%Y%m%d").date())
    
#     # 由于pandas中的特殊值和mysql中的特殊值可能不匹配，无法直接修改，需要借助以下方式修改
#     df1 = df1.where((df1.applymap(lambda x: True if str(x)!="nan" else False)), "zhaobo")
#     df1 = df1.where((df1.applymap(lambda x: True if str(x)!="zhaobo" else False)), None)

#     sql1 = "INSERT INTO chinese_commodity_derivatives_trading_data (`code`, `date`, `open`, `high`, `low`, `close`, `settle`, `volume`, `turnover`, `open_interest`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     # cursor.executemany(sql1, df1.values.tolist())
#     # db.commit()
#     try:
#         cursor.executemany(sql1, df1.values.tolist())
#         db.commit()
#     except:
#         db.rollback()
#         print("error!")

# #关闭数据库连接
# cursor.close()
# db.close()



# 2、导入大商所的商品期货/期权行情数据
# # 打开数据库连接
# db = pymysql.connect(host = 'localhost', user = 'root', passwd='09221017ZB', port= 3306, db='python_mysql', charset='utf8')
# # 使用cursor()方法创建一个游标对象cursor
# cursor = db.cursor()

# path1 = "C:\\Users\\29433\\Desktop\\大商\\2023_opt\\"
# for file_name1 in os.listdir(path1):
#     df1 = pd.read_excel(path1 + file_name1, sheet_name=file_name1[0:len(file_name1)-5])
#     df1 = df1.loc[:, ["合约名称", "交易日期", "开盘价", "最高价", "最低价", "收盘价", "结算价", "成交量", "成交额（万元）", "持仓量"]]
#     df1.columns = ["code", "date", "open", "high", "low", "close", "settle", "volume", "turnover", "open_interest"]
    
#     df1["code"] = df1["code"].str.upper()
#     df1["date"] = df1["date"].map(lambda x: dt.datetime.strptime(str(x), "%Y%m%d").date())

#     sql1 = "INSERT INTO chinese_commodity_derivatives_trading_data (`code`, `date`, `open`, `high`, `low`, `close`, `settle`, `volume`, `turnover`, `open_interest`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     # # cursor.executemany(sql1, df1.values.tolist())
#     # # db.commit()
#     try:
#         cursor.executemany(sql1, df1.values.tolist())
#         db.commit()
#     except:
#         db.rollback()
#         print("error!")

# #关闭数据库连接
# cursor.close()
# db.close()



# 3、导入郑商所的商品期货/期权行情数据
# # 打开数据库连接
# db = pymysql.connect(host = 'localhost', user = 'root', passwd='09221017ZB', port= 3306, db='python_mysql', charset='utf8')
# # 使用cursor()方法创建一个游标对象cursor
# cursor = db.cursor()

# path1 = "C:\\Users\\29433\\Desktop\\郑商\\"
# for file_name1 in os.listdir(path1):
#     df1 = pd.read_csv(path1 + file_name1, delimiter="|")
#     df1 = df1.loc[:, ["合约代码", "交易日期", "今开盘", "最高价", "最低价", "今收盘", "今结算", "成交量(手)", "成交额(万元)", "持仓量"]]
#     df1 = df1.replace("\s+", "", regex=True) # 去除掉df1中的空格字符
#     df1.columns = ["code", "date", "open", "high", "low", "close", "settle", "volume", "turnover", "open_interest"]
    
    
#     df1["code"] = df1["code"].str.upper()
#     df1[["open", "high", "low", "close", "settle", "volume", "turnover", "open_interest"]] = df1[["open", "high", "low", "close", "settle", "volume", "turnover", "open_interest"]].apply(pd.to_numeric)
#     df1["date"] = df1["date"].map(lambda x: dt.datetime.strptime(str(x), "%Y-%m-%d").date())
#     
#     sql1 = "INSERT INTO chinese_commodity_derivatives_trading_data (`code`, `date`, `open`, `high`, `low`, `close`, `settle`, `volume`, `turnover`, `open_interest`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     # # cursor.executemany(sql1, df1.values.tolist())
#     # # db.commit()
#     try:
#         cursor.executemany(sql1, df1.values.tolist())
#         db.commit()
#     except:
#         db.rollback()
#         print("error!")

# #关闭数据库连接
# cursor.close()
# db.close()



# 4、导入大商所的商品期货/期权行情数据
# # 打开数据库连接
# db = pymysql.connect(host = 'localhost', user = 'root', passwd='09221017ZB', port= 3306, db='python_mysql', charset='utf8')
# # 使用cursor()方法创建一个游标对象cursor
# cursor = db.cursor()

# path1 = "C:\\Users\\29433\\Desktop\\广州期货交易所\\"
# for file_name1 in os.listdir(path1):
#     df1 = pd.read_csv(path1 + file_name1)
#     df1 = df1.loc[:, ["合约代码", "交易日期", "开盘价", "最高价", "最低价", "收盘价", "结算价", "成交量", "成交额", "持仓量"]]
#     df1.columns = ["code", "date", "open", "high", "low", "close", "settle", "volume", "turnover", "open_interest"]
    
#     df1["code"] = df1["code"].str.upper()
#     df1["date"] = df1["date"].map(lambda x: dt.datetime.strptime(str(x), "%Y%m%d").date())
    
#     # 因为pandas中的nan值无法一次性彻底转化为none值，所以用一个字符串作为过渡值
#     df1 = df1.where((df1.applymap(lambda x: True if not pd.isna(x) else False)), "zhaobo")
#     df1 = df1.where((df1.applymap(lambda x: True if str(x) != "zhaobo" else False)), None)

#     sql1 = "INSERT INTO chinese_commodity_derivatives_trading_data (`code`, `date`, `open`, `high`, `low`, `close`, `settle`, `volume`, `turnover`, `open_interest`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     # # cursor.executemany(sql1, df1.values.tolist())
#     # # db.commit()
#     try:
#         cursor.executemany(sql1, df1.values.tolist())
#         db.commit()
#     except:
#         db.rollback()
#         print("error!")

# #关闭数据库连接
# cursor.close()
# db.close()



# 5、导入金融期货/期权行情数据
# # 打开数据库连接
# db = pymysql.connect(host = 'localhost', user = 'root', passwd='09221017ZB', port= 3306, db='python_mysql', charset='utf8')
# # 使用cursor()方法创建一个游标对象cursor
# cursor = db.cursor()

# path1 = "C:\\Users\\29433\\Desktop\\金融\\"
# for file_name1 in os.listdir(path1):
#     df1 = pd.read_csv(path1 + file_name1, encoding='ANSI')
#     df1 = df1.loc[:, ["合约代码", "今开盘", "最高价", "最低价", "今收盘", "今结算", "成交量", "成交金额", "持仓量"]]
#     df1 = df1.replace("\s+", "", regex=True) # 去除掉df1中的空格字符
#     # df1["合约代码"] = df1["合约代码"].str.replace("-", "", regex=True) # 去除掉df1["合约代码"]中的"-"字符
#     date1 = file_name1[0:8]
#     df1.insert(1, "交易日期", date1)
#     df1.columns = ["code", "date", "open", "high", "low", "close", "settle", "volume", "turnover", "open_interest"]
    
#     # 由于pandas中的特殊值和mysql中的特殊值可能不匹配，无法直接修改，需要借助以下方式修改
#     df1 = df1.where((df1.applymap(lambda x: True if str(x)!="nan" else False)), "zhaobo")
#     df1 = df1.where((df1.applymap(lambda x: True if str(x)!="zhaobo" else False)), None)
    
#     df1["code"] = df1["code"].str.upper()
#     df1["date"] = df1["date"].map(lambda x: dt.datetime.strptime(str(x), "%Y%m%d").date())
    
#     sql1 = "INSERT INTO chinese_financial_derivatives_trading_data (`code`, `date`, `open`, `high`, `low`, `close`, `settle`, `volume`, `turnover`, `open_interest`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     # cursor.executemany(sql1, df1.values.tolist())
#     # db.commit()
#     try:
#         cursor.executemany(sql1, df1.values.tolist())
#         db.commit()
#     except:
#         db.rollback()
#         print("error!")

# #关闭数据库连接
# cursor.close()
# db.close()