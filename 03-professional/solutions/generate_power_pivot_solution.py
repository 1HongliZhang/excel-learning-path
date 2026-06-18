import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# 产品表
products_data = {
    '产品ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
    '产品名称': ['笔记本电脑', '手机', '平板电脑', '耳机', '显示器'],
    '类别': ['电子产品', '电子产品', '电子产品', '配件', '配件'],
    '成本': [4000, 2500, 3000, 200, 1500],
    '售价': [6000, 3500, 4500, 350, 2200]
}
products_df = pd.DataFrame(products_data)

# 销售表
n = 80
regions = ['华北', '华东', '华南', '华中']
salespeople = ['张三', '李四', '王五', '赵六', '钱七']
product_ids = ['P001', 'P002', 'P003', 'P004', 'P005']

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

sales_data = []
for i in range(n):
    pid = random.choice(product_ids)
    qty = random.randint(1, 20)
    cost = products_df[products_df['产品ID'] == pid]['成本'].values[0]
    price = products_df[products_df['产品ID'] == pid]['售价'].values[0]
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    sales_data.append({
        '订单ID': f'O{1001+i}',
        '日期': date.strftime('%Y-%m-%d'),
        '产品ID': pid,
        '区域': random.choice(regions),
        '数量': qty,
        '销售员': random.choice(salespeople),
        '销售额': qty * price,
        '成本': qty * cost,
        '利润': qty * (price - cost)
    })

sales_df = pd.DataFrame(sales_data)

# 计算度量值汇总
metrics = pd.DataFrame({
    '度量值': ['总销售额', '总成本', '总利润', '利润率', '销售数量', '订单数量'],
    '数值': [
        sales_df['销售额'].sum(),
        sales_df['成本'].sum(),
        sales_df['利润'].sum(),
        round(sales_df['利润'].sum() / sales_df['销售额'].sum() * 100, 2),
        sales_df['数量'].sum(),
        sales_df['订单ID'].nunique()
    ]
})

# 按区域汇总
region_summary = sales_df.groupby('区域').agg({
    '销售额': 'sum',
    '成本': 'sum',
    '利润': 'sum',
    '数量': 'sum'
}).reset_index()
region_summary['利润率'] = round(region_summary['利润'] / region_summary['销售额'] * 100, 2)

# 按产品汇总
product_summary = sales_df.groupby('产品ID').agg({
    '销售额': 'sum',
    '成本': 'sum',
    '利润': 'sum',
    '数量': 'sum'
}).reset_index()
product_summary = product_summary.merge(products_df[['产品ID', '产品名称']], on='产品ID')
product_summary['利润率'] = round(product_summary['利润'] / product_summary['销售额'] * 100, 2)

# 保存到Excel
with pd.ExcelWriter('power_pivot_solution.xlsx', engine='openpyxl') as writer:
    products_df.to_excel(writer, sheet_name='产品表', index=False)
    sales_df.to_excel(writer, sheet_name='销售表', index=False)
    metrics.to_excel(writer, sheet_name='度量值', index=False)
    region_summary.to_excel(writer, sheet_name='区域汇总', index=False)
    product_summary.to_excel(writer, sheet_name='产品汇总', index=False)

print('power_pivot_solution.xlsx 已生成')
