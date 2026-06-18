import pandas as pd
import numpy as np
from datetime import datetime
import random

random.seed(42)
np.random.seed(42)

# 读取练习数据
finance_df = pd.read_excel('../exercises/finance_data.xlsx')
sales_df = pd.read_excel('../exercises/sales_data.xlsx')
hr_df = pd.read_excel('../exercises/hr_data.xlsx')
inventory_df = pd.read_excel('../exercises/inventory_data.xlsx')

print("正在生成答案文件...")

# ===== 1. 财务汇总 =====
finance_summary = finance_df.groupby(['月份', '科目类型'])['金额'].sum().unstack(fill_value=0).reset_index()
finance_summary['利润'] = finance_summary['收入'] - finance_summary['成本']
finance_summary['利润率'] = round(finance_summary['利润'] / finance_summary['收入'] * 100, 2)
finance_summary['成本率'] = round(finance_summary['成本'] / finance_summary['收入'] * 100, 2)

# 按月份排序
month_order = [f'{i}月' for i in range(1, 13)]
finance_summary['月份'] = pd.Categorical(finance_summary['月份'], categories=month_order, ordered=True)
finance_summary = finance_summary.sort_values('月份')

# 科目明细汇总
subject_summary = finance_df.groupby('科目名称')['金额'].sum().reset_index().sort_values('金额', ascending=False)

# ===== 2. 销售汇总 =====
sales_df['销售额'] = sales_df['数量'] * sales_df['单价']

# 区域汇总
region_summary = sales_df.groupby('区域').agg({
    '销售额': 'sum',
    '数量': 'sum',
    '订单ID': 'count'
}).reset_index()
region_summary.columns = ['区域', '销售额', '销量', '订单数']
region_summary = region_summary.sort_values('销售额', ascending=False)

# 产品汇总（关联库存产品信息）
product_summary = sales_df.groupby('产品ID').agg({
    '销售额': 'sum',
    '数量': 'sum',
    '订单ID': 'count'
}).reset_index()
product_summary.columns = ['产品ID', '销售额', '销量', '订单数']
product_summary = product_summary.sort_values('销售额', ascending=False)

# 月度销售趋势
sales_df['月份'] = pd.to_datetime(sales_df['日期']).dt.strftime('%m月')
month_sales = sales_df.groupby('月份')['销售额'].sum().reset_index()
month_sales['月份'] = pd.Categorical(month_sales['月份'], categories=month_order, ordered=True)
month_sales = month_sales.sort_values('月份')

# 客户ABC分析
customer_summary = sales_df.groupby('客户ID')['销售额'].sum().reset_index().sort_values('销售额', ascending=False)
customer_summary['累计销售额'] = customer_summary['销售额'].cumsum()
customer_summary['累计占比'] = round(customer_summary['累计销售额'] / customer_summary['销售额'].sum() * 100, 2)
customer_summary['ABC分类'] = customer_summary['累计占比'].apply(
    lambda x: 'A类' if x <= 80 else ('B类' if x <= 95 else 'C类')
)

# ===== 3. 人力资源汇总 =====
hr_summary = hr_df.groupby('部门').agg({
    '员工ID': 'count',
    '基本工资': 'mean',
    '绩效评分': 'mean'
}).reset_index()
hr_summary.columns = ['部门', '员工数', '平均薪资', '平均绩效']
hr_summary['平均薪资'] = hr_summary['平均薪资'].round(0)
hr_summary['平均绩效'] = hr_summary['平均绩效'].round(2)

# 在职/离职统计
status_summary = hr_df.groupby('离职状态').agg({
    '员工ID': 'count',
    '基本工资': 'mean'
}).reset_index()
status_summary.columns = ['离职状态', '人数', '平均薪资']
status_summary['占比'] = round(status_summary['人数'] / status_summary['人数'].sum() * 100, 2)

# 职位分布
position_summary = hr_df.groupby('职位').agg({
    '员工ID': 'count',
    '基本工资': 'mean'
}).reset_index()
position_summary.columns = ['职位', '人数', '平均薪资']

# ===== 4. 库存汇总 =====
inventory_df['周转率'] = round(inventory_df['出库数量'] / ((inventory_df['期初库存'] + inventory_df['期末库存']) / 2), 2)
inventory_df['库存预警'] = inventory_df['期末库存'].apply(lambda x: '库存不足' if x < 50 else ('库存积压' if x > 300 else '正常'))

# 类别汇总
category_summary = inventory_df.groupby('类别').agg({
    '期末库存': 'sum',
    '库存金额': 'sum',
    '出库数量': 'sum'
}).reset_index()
category_summary['库存占比'] = round(category_summary['库存金额'] / category_summary['库存金额'].sum() * 100, 2)

# ===== 5. 综合KPI =====
total_income = finance_df[finance_df['科目类型'] == '收入']['金额'].sum()
total_cost = finance_df[finance_df['科目类型'] == '成本']['金额'].sum()
total_profit = total_income - total_cost
total_sales = sales_df['销售额'].sum()
active_employees = len(hr_df[hr_df['离职状态'] == '在职'])

kpi = pd.DataFrame({
    'KPI指标': [
        '总收入', '总成本', '总利润', '利润率(%)', 
        '总销售额', '总订单数', '平均客单价',
        '员工总数', '在职员工数', '离职率(%)', '平均薪资',
        '总库存金额', '库存SKU数', '人均产值', '人均利润'
    ],
    '数值': [
        total_income,
        total_cost,
        total_profit,
        round(total_profit / total_income * 100, 2),
        total_sales,
        sales_df['订单ID'].nunique(),
        round(total_sales / sales_df['订单ID'].nunique(), 2),
        len(hr_df),
        active_employees,
        round(len(hr_df[hr_df['离职状态'] == '离职']) / len(hr_df) * 100, 2),
        round(hr_df['基本工资'].mean(), 2),
        inventory_df['库存金额'].sum(),
        len(inventory_df),
        round(total_sales / active_employees, 2),
        round(total_profit / active_employees, 2)
    ]
})

# ===== 保存到Excel =====
with pd.ExcelWriter('company_analysis_solution.xlsx', engine='openpyxl') as writer:
    kpi.to_excel(writer, sheet_name='综合KPI', index=False)
    finance_summary.to_excel(writer, sheet_name='财务汇总', index=False)
    subject_summary.to_excel(writer, sheet_name='科目明细', index=False)
    region_summary.to_excel(writer, sheet_name='区域销售', index=False)
    product_summary.to_excel(writer, sheet_name='产品销售', index=False)
    month_sales.to_excel(writer, sheet_name='月度销售', index=False)
    customer_summary.to_excel(writer, sheet_name='客户ABC', index=False)
    hr_summary.to_excel(writer, sheet_name='部门人力', index=False)
    status_summary.to_excel(writer, sheet_name='在职离职', index=False)
    position_summary.to_excel(writer, sheet_name='职位分布', index=False)
    inventory_df.to_excel(writer, sheet_name='库存明细', index=False)
    category_summary.to_excel(writer, sheet_name='库存类别', index=False)

print("company_analysis_solution.xlsx 已生成")
print(f"包含12个工作表，涵盖财务、销售、人力资源、库存全维度分析")
