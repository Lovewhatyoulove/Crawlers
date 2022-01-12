import pandas as pd

# cols = ['寻亲类别', '寻亲编号', '姓名', '性别', '出生日期', '失踪时身高', '失踪时间', '失踪人所在地', '失踪地点', '寻亲者特征描述', '其他资料', '注册时间', '跟进志愿者']
# df = pd.DataFrame(columns=cols)
# df = pd.DataFrame([[3, 'yy', 'dsb']])
# df.to_csv('test.csv', mode='a', header=False)
df = pd.read_csv('宝贝寻家.csv', index_col=0)
print(df.head())
print(df.tail())
df1 = df.reset_index(drop=True)
df1['序号'] = list(range(1, df1.shape[0]+1))
df1.to_csv('宝贝寻家1.csv', index=False)
