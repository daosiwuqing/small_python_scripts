# 该脚本的作用：用来记录一些常用的数据处理方法



# 1、pymysql的常用方法
# import pymysql
# db = pymysql.connect(host = 'localhost', user = 'root', passwd='09221017ZB', port= 3306, db='python_mysql', charset='utf8') #连接数据库
# cursor = db.cursor() #使用cursor()方法创建一个游标对象cursor

# sql1 = "select * from python_mysql.chinese_commodity_futures_data where code like '" + variety_code + "%' and length(code) <=" + str(n) + ";"

# cursor.execute(sql1) #使用execute()方法执行sql

# cursor.execute(sql1, list1) #使用插入语句时，此种方式一次只能插入一行数据

# list2 = df1.values.tolist() #把dataframe数据形式改造成列表嵌套的数据形式，方便进行批量插入多行数据
# cursor.executemany(sql1, list2) #使用插入语句时，此种方式可以批量插入多行数据，但list2要是列表嵌套的数据形式

# db.commit() #确认执行sql语句
# db.rollback() #回滚，取消此次所有sql语句的执行结果


# data1 = pd.dataframe(cursor.fetchall(), columns=["code", "date", "open", "high", "low", "close", "settle", "volume", "turnover", "open_interest"]) #从游标cursor中取出数据并加上表头，使用fetchone()方法获取单条数据；使用fetchall()方法获取所有数据

# cursor.close() #关闭游标
# db.close() #关闭数据库



# 2、pandas和numpy的常用方法
# import pandas as pd
# import numpy as np
# df1 = df1.where((df1.applymap(lambda x: true if str(x)!="--" else false)), none) #该语句可以一次性修改dataframe中所有不符合条件的值，在python向sql中插入数据时，常用来处理特殊值


# cols1 = [x for i, x in enumerate(df.columns) if df.iat[0,i]==0] #利用enumerate对某行进行遍历，将含有特殊数值的列放入cols中
# df1 = df1.drop(cols1, axis=1) #用drop方法删除含有特定数值的列


# df1 = df1[-(df1[col_name1].isnull()==True | (df1[col_name2]==string1) & (df1[col_name3]<>string2))] #该方法是一种常用且简单的根据多列值筛选行的方式


# df1 = df1.filter(regex=regex1, axis=1) #用filter方法通过正则表达式选取行名或列名符合要求的数据


# df1 = df1.query("col_name.str.contains(regex1, regex=True)", engine="python") #用query方法通过正则表达式选取某列中含有特定字符的行，col_name是df1的某列名，regex1是正则表达式字符串


# log_r1 = np.log(df1/df1.shift(1)) #计算对数收益率（日）
# annual_r1 = np.exp(log_r1.mean()*250) - 1 #年化收益率
# std1 = np.sqrt(log_r1.var()*250) #计算收益率的标准差


# df1 = pd.read_csv(path1, encoding="gb18030") #读取二进制数据格式的csv文件


# df1.col_name.str.extract(regex1) #根据正则表达式提取某一列中的子字符串
# df1.replace(regex1, replace_str1, regex=True, inplace=True) #根据正则表达式把df1中特定字符替换为repalce_str1，inplace=True表示要替换源数据
# df1.col_name.str.replace(regex1, replace_str1, regex=True)  #根据正则表达式把df1某列中特定字符替换为repalce_str1


# df1["date"].dt.isocalendar().week #标记所对应的日期属于当年的第几个星期


# 用滚动函数滚动计算df中的数据
# #一，只滚动计算单列
# def func1(self, x, y):
#     return (self.mean() - self.std()) * x / y
# df1.col_name2 = df1.col_name1.rolling(window=period1).apply(func=func1, args=(10, 5)) # 常用来根据时间序列数据计算指标
# #二、滚动计算多列
# def func1(df1, window1):
    # return value1, value2
# df2[["new_col_name1", "new_col_name2"]] = [func1(df, window1) for df in df2.rolling(window1)]


# 用重采样函数处理df中的数据
# df2 = df1.resample("5T", on=col_name1).agg({
#     "open" : "first",
#     "high" : "max",
#     "low" : "min",
#     "close" : "last",
#     "volume" : "sum",
#     "turnover" : "sum",
#     "open_interest" : "last"
# }) # 30S表示30秒，5T表示5分钟，常用来对时间序列数据进行降频或升频



# 3、csv中的常用方法
# import csv
# with open(path1, "a", newline="") as csvfile1:#可以实现向csv文件中按行写入数据
#    writer1 = csv.writer(csvfile1, delimiter=",", quotechar="\"")
#    writer1.writerow(list1) #此处的list是指列表类型的数据
#    writer1.writerows(df1.values.tolist())


# import io
# df1 = pd.read_csv(io.StringIO(text1)) #把字符串转化为dataframe数据



# 4、datetime中的常用方法
# import datetime as dt
# date_time1 = dt.datetime.strptime("2021/09/21 15:00:00", "%Y/%m/%d %H:%M:%S") #字符型日期时间转化为datetime型日期时间
# date1 = date_time1.date() #提取datetime型日期时间中的日期，日期的数据类型为date
# time1 = date_time1.time() #提取datetime型日期时间中的时间，时间的数据类型为time
# str_date_time1 = date_time1.strftime("%Y-%m-%d %H:%M:%S") #把datetime型日期时间转化为字符型日期时间
# str_date1 = date1.strftime("%Y-%m-%d") #把date型日期转化为字符型日期
# str_time1 = time1.strftime("%H:%M:%S") #把time型时间转化为字符型时间


# df1["date"] = df1["date"].apply(lambda x: dt.datetime.strptime(x, "%d/%m/%Y %H:%M:%S")) #把df中字符型日期时间的列数据修改为datetime型日期时间的列数据



# 5、自定义包的调用方法
# import sys
# sys.path.append(path1) #path1是package1的路径
# from package1 import cal_index1 as c1 #package1为.py文件，cal_index为class



# 6、openpyxl中的常用方法
# import openpyxl
# workbook1 = openpyxl.load_workbook(path1) #打开指定路径下的excel文件
# workbook1[table_name].insert_rows(idx = 2, amount = 1) #向excel文件中指定表（table_name）插入行
# workbook1[table_name].cell(row = 2, column = 1).value = value1 #向excel文件中指定表（table_name）中的指定单元格赋值
# max_column1 = workbook[table_name].max_column #获取excel文件中指定表（table_name）已经使用的最大列数
# workbook1.save(path1) #保存指定路径下的excel文件



# 7、zipfile中的常用方法
# import zipfile as zp
# with zp.ZipFile(path1) as zf1:
#     content1 = zf1.read(filename1) #此时输出的content1为二进制数据
#     text1 = content1.decode(encoding = "utf-8")



# 8、threading的常用方法
# import threading as th
# t1 = th.Thread(target=Class1().func1, args=("zhaobo1", 3)) #创建thread实例,args指的是func1中的参数
# t2 = th.Thread(target=Class1().func1, args=("zhaobo2", 5))
# t1.start() #启动线程运行
# t2.start()
# t1.join() #等待所有线程执行完毕
# t2.join()



# 9、py2neo的常用方法
# from py2neo import *
# #登录图数据库，name是数据库的名称，Neo4j企业版能直接创建多个数据库，但社区版需要稍微复杂一些的操作实现
# graph = Graph("http://localhost:7474", user="neo4j", password="09221017ZB", name="industrynet")

# node1 = Node("label1", attribute1="attribute1")
# node2 = Node("label1", "label2", attribute2="attribute2", attribute3="attribute3")
# graph.create(node1) #创建节点1
# graph.create(node2) #创建节点2

# relation1 = Relationship(node2, 'belong to', node1)
# relation2 = Relationship(node2, 'belong to', node1, attribute4="attribute4")
# graph.create(relation1) #创建关系1
# graph.create(relation2) #创建关系2

# graph.delete(relation2) # 有关系的节点想要删除需要通过删除关系来删除节点


# 查询节点并添加新属性
# matcher = NodeMatcher(graph)
# node1 = matcher.match("label1").where(attibute1="attribute1").first()
# node1.setdefault("attibute2", default = "attribute2")
# graph.push(node1)


#在Neo4j管理终端上向Neo4j的数据库导入csv文件数据，分三步走，"file:///"指的是Neo4j安装路径中import文件夹，tmp为临时变量
# #一、node1文件，格式：node1_id,attribute1...
# LOAD CSV WITH HEADERS FROM 'file:///node1.csv' AS row 
# MERGE (tmp:node1 {code: row.node1_id}) ON CREATE SET 
# tmp.name = row.name
# #二、node2文件，格式：node2_id,attribute1...
# LOAD CSV WITH HEADERS FROM 'file:///node2.csv' AS row 
# MERGE (tmp:node2 {code: row.node2_id}) ON CREATE SET 
# tmp.name = row.name
# #三、node1与node2的关系文件，格式：node1_id,node2_id
# LOAD CSV WITH HEADERS FROM 'file:///n1_n2_relation.csv' AS row
# MATCH (tmp1:node1 {code: row.node1_id})
# MATCH (tmp2:node2 {code: row.node2_id})
# MERGE (tmp1)-[:up_down_stream]-(tmp2)


#在Neo4j管理终端查询数据
# MATCH (n1:node1) - [r1:relation1] - (n2:node2)
# WHERE (n1.attribute1="attribute1") AND (n1.attribute2 contains "string1")
# RETURN n1, n2


# 使用MERGE语句创建或更新节点，匹配属性attribute1为"attribute1"的node1节点，如果找到了就更新其属性attribute2为"attribute2"，如果没有找到就创建一个新的属性attribute2并设置为"attribute2"
# MERGE (n1:node1 {attribute1:"attribute1"})
# ON CREATE SET n1.attribute2 = "attribute2"
# ON MATCH SET n1.attribute2 = "attribute2"



# 10、re的常用方法
# import re
# string_list1 = re.findall(pattern=regex1, string=filename1) # 该函数根据正则表达式匹配目标字符串内容,返回值是匹配到的内容列表，如果正则表达式有子组，则只能获取到子组对应的内容
# string3 = re.sub(pattern=regex1, replace=string1, string=string2) # 该函数使用一个字符串替换正则表达式匹配到的内容。返回值是替换后的字符串



# 11、os的常用方法
# import os
# path = os.getcwd() # 获取终端的绝对路径



# 12、matplotlib的常用方法
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# import datetime as dt

# # 1)matplotlib中使用某个字体文件
# # 1.1)获取字体文件真正的名称
# # font = fm.FontProperties(fname="C:/Users/29433/AppData/Local/Microsoft/Windows/Fonts/FZHTJW.TTF")
# # print(font.get_name())
# # 1.2)设置全局字体
# fm.fontManager.addfont('C:/Users/29433/AppData/Local/Microsoft/Windows/Fonts/FZHTJW.TTF')
# mpl.rcParams['font.sans-serif'] = 'FZHei-B01S' # 此处需要用字体文件真正的名称
# # 1.3)用fontproperties参数的一类方法
# font_properties = fm.FontProperties(family='FZHei-B01S', size=16, stretch=0) # 用来设置字体的属性
# # 1.4)用prop参数和fontdict参数的一类方法
# fontdict = {'family':'FZHei-B01S', 'size':6}

# mpl.rcParams["axes.unicode_minus"] = False # 解决负号无法显示的问题

# df1 = pd.read_excel("D:\\LearningAndWorking\\工作\\日常工作\\专题研究\\月度\\持仓龙虎榜分析\\M_result.xlsx", sheet_name="前20名合计")
# # 创建图形和主y轴
# fig, axs = plt.subplots(2, 2, figsize=(13, 7))
# # x_date = [dt.datetime.strptime(d, "%Y/%m/%d") for d in df1.date]
# x_date = df1.date

# ax1_1 = axs[0, 0]
# # 创建左侧的第一个y轴
# y1 = df1["long_volume"]
# ax1_1.set_title(label='图标题', fontproperties=font_properties) # 添加图表标题
# ax1_1.plot(x_date, y1, color=(75/255, 115/255, 165/255))
# ax1_1.set_ylabel(ylabel="持多仓", color=(75/255, 115/255, 165/255), fontdict=fontdict) # 设置y轴标签及其颜色
# ax1_1.tick_params(axis='y', colors=(75/255, 115/255, 165/255)) # 设置坐标轴的刻度线及刻度值的颜色
# # ax1_1.set_ylim([0, 8000]) # 设置y轴的刻度范围
# # ax1_1.set_yticklabels(labels=[0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000], fontdict=fontdict) # 设置y轴刻度值的标签和刻度值的字体
# ax1_1.spines['top'].set_color("none") # 调整边框线的颜色以及是否设置边框线，第一个可选参数：top、bottom、left、right；第二个可选参数：none或其它颜色参数
# # ax1、ax2、ax3和ax4的边框线会有重叠，轴都为黑色的时候不会影响，但如果各轴的颜色不同，就需要把影响其它轴的边框线设为无颜色
# ax1_1.spines['left'].set_color(c=(75/255, 115/255, 165/255))
# ax1_1.spines['right'].set_color("none")
# ax1_1.legend(['持多仓'], fontsize=6, labelcolor=(75/255, 115/255, 165/255), frameon=False, bbox_to_anchor=(0.25,1.05)) # 设置图例的一些参数，其中bbox_to_anchor(x,y)用来控制图例的位置，x表示图例在x轴方向上的位置，y表示图例在y轴方向上的位置，范围是0到1，小于0或大于1可以让图例位于坐标轴之外。

# # 创建左侧的第二个y轴
# ax1_2 = ax1_1.twinx()
# # 调整ax1_2的位置，为了不与ax1_1重叠
# ax1_2.spines['left'].set_position(('outward', 30)) # 将y轴挪到x轴的50刻度处
# ax1_2.yaxis.set_ticks_position('left') # 将y轴的刻度值写y轴的左面
# ax1_2.yaxis.set_label_position('left') # 将y轴的标签值写y轴的左面
# y2 = df1["short_volume"]
# ax1_2.plot(x_date, y2, color=(165/255, 142/255, 90/255))
# ax1_2.set_ylabel(ylabel='持空仓', color=(165/255, 142/255, 90/255), fontdict=fontdict)
# ax1_2.tick_params(axis='y', colors=(165/255, 142/255, 90/255))
# ax1_2.spines['top'].set_color("none")
# ax1_2.spines['left'].set_color(c=(165/255, 142/255, 90/255))
# ax1_2.spines['right'].set_color("none")
# ax1_2.legend(['持空仓'], fontsize=6, labelcolor=(165/255, 142/255, 90/255), frameon=False, bbox_to_anchor=(0.25,0.98))

# # 创建右侧的第一个y轴
# ax1_3 = ax1_1.twinx()
# y3 = df1["open_interest"]
# ax1_3.plot(x_date, y3, color=(90/255, 130/255, 140/255))
# ax1_3.set_ylabel(ylabel="持仓量",  color=(90/255, 130/255, 140/255), fontdict=fontdict)
# ax1_3.tick_params(axis='y', colors=(90/255, 130/255, 140/255))
# ax1_3.spines['top'].set_color("none")
# ax1_3.spines['right'].set_color(c=(90/255, 130/255, 140/255))
# ax1_3.spines['left'].set_color("none")
# ax1_3.legend(['持仓量'], fontsize=6, labelcolor=(90/255, 130/255, 140/255), frameon=False, bbox_to_anchor=(0.25,0.91))

# # 创建右侧的第二个y轴
# ax1_4 = ax1_1.twinx()
# # 调整ax4的位置，为了不与ax3重叠
# ax1_4.spines['right'].set_position(('outward', 30))
# ax1_4.yaxis.set_ticks_position('right') # 将y轴的刻度值写y轴的右面
# ax1_4.yaxis.set_label_position('right') # 将y轴的标签值写y轴的右面
# y4 = df1["long/short"]
# ax1_4.plot(x_date, y4, color=(166/255, 166/255, 166/255))
# ax1_4.set_ylabel(ylabel='多/空', color=(166/255, 166/255, 166/255), fontdict=fontdict)
# ax1_4.tick_params(axis='y', colors=(166/255, 166/255, 166/255))
# ax1_4.spines['top'].set_color("none")
# ax1_4.spines['right'].set_color(c=(166/255, 166/255, 166/255))
# ax1_4.spines['left'].set_color("none")
# ax1_4.legend(['多/空'], fontsize=6, labelcolor=(166/255, 166/255, 166/255), frameon=False, bbox_to_anchor=(0.25,0.84))

# # 调整图的边界，为了有更多的空白来展示所有的y轴
# # fig.subplots_adjust(left=0.2, right=0.8)

# plt.show()


