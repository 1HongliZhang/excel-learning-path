import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# 生成销售数据
n = 100
products = ['产品A', '产品B', '产品C', '产品D', '产品E']
regions = ['华北', '华东', '华南', '华中', '西南', '西北', '东北']
salespeople = ['张三', '李四', '王五', '赵六', '钱七', '孙八', '周九', '吴十']

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

data = []
for i in range(n):
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    data.append({
        '产品': random.choice(products),
        '区域': random.choice(regions),
        '销售额': random.randint(5000, 50000),
        '日期': date.strftime('%Y-%m-%d'),
        '销售员': random.choice(salespeople)
    })

df = pd.DataFrame(data)

# 添加月份列
df['月份'] = pd.to_datetime(df['日期']).dt.strftime('%Y年%m月')

# 计算汇总数据
summary = pd.DataFrame({
    '指标': ['总销售额', '平均销售额', '最高销售额', '最低销售额', '销售笔数'],
    '数值': [
        df['销售额'].sum(),
        round(df['销售额'].mean(), 2),
        df['销售额'].max(),
        df['销售额'].min(),
        len(df)
    ]
})

# 按区域汇总
region_summary = df.groupby('区域')['销售额'].sum().reset_index()
region_summary.columns = ['区域', '销售额']

# 保存到Excel
with pd.ExcelWriter('sales_analysis_solution.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='销售数据', index=False)
    summary.to_excel(writer, sheet_name='汇总数据', index=False)
    region_summary.to_excel(writer, sheet_name='区域汇总', index=False)

print('sales_analysis_solution.xlsx 已生成')
