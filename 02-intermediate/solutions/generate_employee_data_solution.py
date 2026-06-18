import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# 生成员工数据
n = 50
names = ['张伟', '李娜', '王强', '刘洋', '陈静', '杨帆', '赵敏', '黄磊', '周婷', '吴磊',
         '徐丽', '孙杰', '马云', '朱琳', '胡军', '郭芳', '何平', '高峰', '林雪', '郑宇',
         '谢婷', '宋波', '唐丽', '许强', '韩梅', '冯刚', '曹颖', '彭亮', '曾静', '董伟',
         '袁芳', '蒋军', '蔡丽', '贾平', '魏强', '薛芳', '叶婷', '阎军', '余丽', '潘伟',
         '杜芳', '戴强', '夏丽', '钟伟', '汪芳', '田强', '任丽', '姜伟', '范芳', '方强']
departments = ['销售部', '技术部', '财务部', '人事部', '市场部']

# 生成入职日期（2018-2023年）
start_date = datetime(2018, 1, 1)
end_date = datetime(2023, 12, 31)
hire_dates = [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(n)]

# 生成薪资
salaries = [random.randint(4000, 25000) for _ in range(n)]

df = pd.DataFrame({
    'ID': [f'{i+1:03d}' for i in range(n)],
    '姓名': names[:n],
    '部门': [random.choice(departments) for _ in range(n)],
    '薪资': salaries,
    '入职日期': [d.strftime('%Y-%m-%d') for d in hire_dates]
})

# 计算工龄（年数和月数）
today = datetime(2024, 12, 1)
work_years = []
work_months = []
for d in hire_dates:
    diff = today - d
    years = diff.days // 365
    months = (diff.days % 365) // 30
    work_years.append(years)
    work_months.append(months)

df['工龄'] = [f'{y}年{m}个月' for y, m in zip(work_years, work_months)]

# 薪资等级
df['薪资等级'] = df['薪资'].apply(lambda x: '高薪' if x >= 15000 else ('中薪' if x >= 8000 else '底薪'))

# 保存到Excel
with pd.ExcelWriter('employee_data_solution.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='员工信息', index=False)
    
    # 添加查询区域工作表
    query_df = pd.DataFrame({
        '查询ID': ['005'],
        '姓名(VLOOKUP)': ['=VLOOKUP($A$2,员工信息!$A$2:$E$51,2,FALSE)'],
        '部门(VLOOKUP)': ['=VLOOKUP($A$2,员工信息!$A$2:$E$51,3,FALSE)'],
        '薪资(VLOOKUP)': ['=VLOOKUP($A$2,员工信息!$A$2:$E$51,4,FALSE)'],
        '姓名(INDEX+MATCH)': ['=INDEX(员工信息!B:B,MATCH($A$2,员工信息!A:A,0))'],
        '部门(INDEX+MATCH)': ['=INDEX(员工信息!C:C,MATCH($A$2,员工信息!A:A,0))'],
        '薪资(INDEX+MATCH)': ['=INDEX(员工信息!D:D,MATCH($A$2,员工信息!A:A,0))']
    })
    query_df.to_excel(writer, sheet_name='查询示例', index=False)
    
    # 添加筛选示例
    filter_df = pd.DataFrame({
        '筛选部门': ['销售部'],
        '说明': ['在下方使用FILTER函数筛选该部门所有员工']
    })
    filter_df.to_excel(writer, sheet_name='筛选示例', index=False)

print('employee_data_solution.xlsx 已生成')
