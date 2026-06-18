import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# 生成上半年数据
products = ['产品A', '产品B', '产品C', '产品D', '产品E']
regions = ['华北', '华东', '华南', '华中']

# 上半年数据（2024年1-6月）
data1 = []
for i in range(30):
    date = datetime(2024, random.randint(1, 6), random.randint(1, 28))
    sales = random.randint(10000, 50000)
    data1.append({
        '日期': date.strftime('%Y-%m-%d'),
        '产品名称': random.choice(products),
        '区域': random.choice(regions),
        '销售额': sales,
        '利润': int(sales * 0.2)
    })

df1 = pd.DataFrame(data1)
df1 = df1.sort_values('日期').reset_index(drop=True)

# 下半年数据（2024年7-12月）
data2 = []
for i in range(30):
    date = datetime(2024, random.randint(7, 12), random.randint(1, 28))
    sales = random.randint(10000, 50000)
    data2.append({
        '日期': date.strftime('%Y-%m-%d'),
        '产品名称': random.choice(products),
        '区域': random.choice(regions),
        '销售额': sales,
        '利润': int(sales * random.uniform(0.15, 0.25))
    })

df2 = pd.DataFrame(data2)
df2 = df2.sort_values('日期').reset_index(drop=True)

# 合并数据
df_merged = pd.concat([df1, df2], ignore_index=True)
df_merged = df_merged.sort_values('日期').reset_index(drop=True)

# 保存到Excel（答案文件：清洗后数据）
with pd.ExcelWriter('power_query_solution.xlsx', engine='openpyxl') as writer:
    df_merged.to_excel(writer, sheet_name='清洗后数据', index=False)
    
    # 添加数据质量检查表
    quality_check = pd.DataFrame({
        '检查项': ['总行数', '空值数', '日期范围', '销售额范围'],
        '结果': [
            len(df_merged),
            df_merged.isnull().sum().sum(),
            f"{df_merged['日期'].min()} ~ {df_merged['日期'].max()}",
            f"{df_merged['销售额'].min()} ~ {df_merged['销售额'].max()}"
        ]
    })
    quality_check.to_excel(writer, sheet_name='数据质量检查', index=False)

print('power_query_solution.xlsx 已生成')
