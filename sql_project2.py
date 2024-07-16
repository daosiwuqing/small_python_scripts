# 该脚本的作用：向数据库导入大宗商品基本面数据
import pandas as pd
import os, pymysql



# 打开数据库连接
db = pymysql.connect(host = 'localhost', user = 'root', passwd='09221017ZB', port= 3306, db='python_mysql', charset='utf8')
# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor() 


# # 1、向数据库导入周度数据
# path = "C:\\Users\\29433\\Desktop\\农产品基础数据（周度）.xlsx"

# f = pd.ExcelFile(path)
# df = pd.DataFrame(columns=["日期", "产量", "毛利润", "库存"])
# for i in f.sheet_names:
#     df1 = pd.read_excel(path, sheet_name=i)
#     df1["日期"] = df1["日期"].dt.strftime("%Y%m%d")
#     df1["品种"] = i
#     df1["数据源"]= "百川盈孚"
#     df = df.append(df1, ignore_index=True, sort=False)
# df = df[-(df["产量"].isnull()==True | (df["毛利润"].isnull()==True) | (df["库存"].isnull()==True))]

# # 因为pandas中的nan值无法一次性彻底转化为none值，所以用一个字符串作为过渡值
# df = df.where((df.applymap(lambda x: True if not pd.isna(x) else False)), "zhaobo")
# df = df.where((df.applymap(lambda x: True if str(x) != "zhaobo" else False)), None)

# sql = "INSERT INTO chinese_commodity_fundamental_data_weekly (`date`, `yield(Ton)`, `gross_profit(Yuan/Ton)`, `inventory(Ton)`, `variety`, `data_source`) VALUES (%s, %s, %s, %s, %s, %s)"
# data1 = df.values.tolist()
# try:
#     cursor.executemany(sql, data1)
#     db.commit()
# except:
#     db.rollback()
#     print("error!")


# # 2、向数据库导入月度数据
# path = "C:\\Users\\29433\\Desktop\\农产品基础数据（月度）.xlsx"

# f = pd.ExcelFile(path)
# df = pd.DataFrame(columns=["日期", "产量", "开工率", "进口量", "出口量", "消费量"])
# for i in f.sheet_names:
#     df1 = pd.read_excel(path, sheet_name=i)
#     df1["日期"] = df1["日期"].dt.strftime("%Y%m")
#     df1["品种"] = i
#     df1["数据源"]= "百川盈孚"
#     df = df.append(df1, ignore_index=True, sort=False)
# df = df[-(df["产量"].isnull()==True | (df["开工率"].isnull()==True) | (df["进口量"].isnull()==True) | (df["出口量"].isnull()==True) | (df["消费量"].isnull()==True))]

# # 因为pandas中的nan值无法一次性彻底转化为none值，所以用一个字符串作为过渡值
# df = df.where((df.applymap(lambda x: True if not pd.isna(x) else False)), "zhaobo")
# df = df.where((df.applymap(lambda x: True if str(x) != "zhaobo" else False)), None)

# sql = "INSERT INTO chinese_commodity_fundamental_data_monthly (`date`, `yield(Ton)`, `capacity_utilization`, `import(Ton)`, `export(Ton)`, `consumption(Ton)`, `variety`, `data_source`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# data1 = df.values.tolist()
# try:
#     cursor.executemany(sql, data1)
#     db.commit()
# except:
#     db.rollback()
#     print("error!")


# # 3、向数据库导入年度数据
# path = "C:\\Users\\29433\\Desktop\\农产品基础数据（年度）.xlsx"
    
# f = pd.ExcelFile(path)
# df = pd.DataFrame(columns=["日期", "产能"])
# for i in f.sheet_names:
#     df1 = pd.read_excel(path, sheet_name=i)
#     df1["日期"] = df1["日期"].dt.strftime("%Y")
#     df1["品种"] = i
#     df1["数据源"]= "百川盈孚"
#     df = pd.concat([df, df1])
# df = df[-(df["产能"].isnull()==True)]
    
# sql = "INSERT INTO chinese_commodity_fundamental_data_yearly (`date`, `deliverability(Ton)`, `variety`, `data_source`) VALUES (%s, %s, %s, %s)"
# data1 = df.values.tolist()
# try:
#     cursor.executemany(sql, data1)
#     db.commit()
# except:
#     db.rollback()
#     print("error!")


# 关闭数据库连接
cursor.close()
db.close()


