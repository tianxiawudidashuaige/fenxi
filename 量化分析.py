import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#第一题
"""pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000) #设置最大的行宽度（小于1000行均可以输出）
pd.set_option('display.max_colwidth',10) #设置最大的列宽1000行（小于1000行均可以输出）
df = pd.read_excel('/Users/linqing/Desktop/量化分析/跨境电商商品数据.xlsx')
df.insert(loc=8, column='销售额',value='')
df.index.name=None#去掉行索引的名字
df.columns=['商品ID','商品名称','商品图片','商品详情页','店铺编号','店铺名称','商品价格','订单量','销售额']
df['销售额']=df['商品价格']*df['订单量']
df.sort_values(by ='销售额',inplace=True,ascending=False)
plt.bar(df.店铺名称,df.销售额,color='orange')
plt.xticks(df.店铺名称,rotation='90')

plt.show()
"""


df = pd.read_excel('/Users/linqing/Desktop/量化分析/跨境电商客户评论数据.xlsx')
df.columns=['商品ID','SKU','客户评价','补充反馈','图片评论','图片数量','收货国家','国家缩写','收货国家英','客户名称','时间','评论星级','女鞋颜色','女鞋尺码','物流方式','发货地']
df = df.dropna(subset=['客户评价'])#空值处理
# 根据用户ProductID与CustomerReviews两列作为参照，如存在用户id与comment同时相同，那么只保留最开始出现的。
df.drop_duplicates(subset=['商品ID','客户评价'], keep='first', inplace=True)
# 重置索引
df.reset_index(drop=True, inplace=True)
df['客户评价'] = df['客户评价'].str.replace(r'^(.)\1*$<>', '',regex=True)
# 用空字符串('')替换('111','aaa','....')等

df['客户评价'] = df['客户评价'].str.replace(r'\d+/\d+/\d+ \d+:\d+:\d+', '',regex=True)
# 用空字符串('')替换('2020/11/20 20:00:00')等

# 将空字符串转为'np.nan',即NAN,用于下一步删除这些评论
df['客户评价'].replace(to_replace=r'^\s*$', value=np.nan, regex=True, inplace=True)
# 删除comment中的空值，并重置索引
df = df.dropna(subset=['客户评价'])
df.reset_index(drop=True, inplace=True)
#第二题
"""df = df['国家缩写'].value_counts()
x=df.index[:20]
y=df.values[:20]
plt.tight_layout()
plt.bar(x,y)
plt.show()
"""

#第三题
data=pd.read_excel('5\TB201812.xls',usecols=['时间','总金额'])
print(data)
data['订单创建时间']=pd.to_datetime(data['订单创建时间'])
data=data.set_index('订单创建时间')
print(data)





