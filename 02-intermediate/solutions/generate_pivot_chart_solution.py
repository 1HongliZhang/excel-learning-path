import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# 生成数据
months = list(range(1, 13))
categories = ['电子产品', '服装鞋帽', '食品饮料', '家居用品', '办公用品']
regions = ['北京', '上海', '广州', '深圳', '成都', '杭州']

data = []
for month in months:
    for category in categories:
        for region in regions:
            sales = random.randint(10000, 100000)
            profit = int(sales * random.uniform(0.1, 0.3))
            data.append({
                '月份': f'{month}月',
                '产品类别': category,
                '地区': region,
                '销售额': sales,
                '利润': profit
            })

df = pd.DataFrame(data)

# 计算利润率
df['利润率'] = round(df['利润'] / df['销售额'] * 100, 2)

# 按地区汇总
region_summary = df.groupby('地区')['销售额'].sum().reset_index()

# 按产品类别汇总
category_summary = df.groupby('产品类别')['销售额'].sum().reset_index()

# 按月份汇总
month_summary = df.groupby('月份')['利润'].sum().reset_index()
month_summary['月份'] = pd.Categorical(month_summary['月份'], 
                                       categories=[f'{i}月' for i in range(1,13)], 
                                       ordered=True)
month_summary = month_summary.sort_values('月份')

# 保存到Excel
with pd.ExcelWriter('pivot_chart_solution.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='原始数据', index=False)
    region_summary.to_excel(writer, sheet_name='地区汇总', index=False)
    category_summary.to_excel(writer, sheet_name='产品类别汇总', index=False)
    month_summary.to_excel(writer, sheet_name='月度利润汇总', index=False)

print('pivot_chart_solution.xlsx 已生成')
