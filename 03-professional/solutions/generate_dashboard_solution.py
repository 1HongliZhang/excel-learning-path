import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# 生成仪表板数据
months = list(range(1, 13))
categories = ['电子产品', '服装鞋帽', '食品饮料', '家居用品', '办公用品']
regions = ['北京', '上海', '广州', '深圳', '成都', '杭州']

data = []
for month in months:
    for category in categories:
        for region in regions:
            sales = random.randint(50000, 200000)
            cost = int(sales * random.uniform(0.6, 0.8))
            profit = sales - cost
            data.append({
                '月份': f'{month}月',
                '产品类别': category,
                '地区': region,
                '销售额': sales,
                '成本': cost,
                '利润': profit
            })

df = pd.DataFrame(data)

# KPI汇总
kpi = pd.DataFrame({
    'KPI指标': ['总销售额', '总成本', '总利润', '利润率'],
    '数值': [
        df['销售额'].sum(),
        df['成本'].sum(),
        df['利润'].sum(),
        round(df['利润'].sum() / df['销售额'].sum() * 100, 2)
    ]
})

# 月度销售趋势
month_trend = df.groupby('月份')['销售额'].sum().reset_index()
month_trend['月份'] = pd.Categorical(month_trend['月份'], 
                                      categories=[f'{i}月' for i in range(1,13)], 
                                      ordered=True)
month_trend = month_trend.sort_values('月份')

# 区域销售对比
region_sales = df.groupby('地区')['销售额'].sum().reset_index().sort_values('销售额', ascending=False)

# 产品类别占比
category_sales = df.groupby('产品类别')['销售额'].sum().reset_index().sort_values('销售额', ascending=False)

# 保存到Excel
with pd.ExcelWriter('dashboard_solution.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='原始数据', index=False)
    kpi.to_excel(writer, sheet_name='KPI汇总', index=False)
    month_trend.to_excel(writer, sheet_name='月度趋势', index=False)
    region_sales.to_excel(writer, sheet_name='区域对比', index=False)
    category_sales.to_excel(writer, sheet_name='类别占比', index=False)

print('dashboard_solution.xlsx 已生成')
