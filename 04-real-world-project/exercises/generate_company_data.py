import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# ===== 1. 财务数据 =====
print("正在生成财务数据...")
months = list(range(1, 13))
income_items = ['主营业务收入', '其他业务收入', '投资收益', '营业外收入']
cost_items = ['主营业务成本', '销售费用', '管理费用', '财务费用', '研发费用']

finance_data = []
for month in months:
    # 收入（主营业务有季节性波动）
    base_income = 500000 + 100000 * np.sin(month * np.pi / 6)  # 季节性波动
    for item in income_items:
        if item == '主营业务收入':
            amount = int(base_income * random.uniform(0.9, 1.1))
        elif item == '其他业务收入':
            amount = int(base_income * random.uniform(0.05, 0.1))
        elif item == '投资收益':
            amount = int(base_income * random.uniform(0.02, 0.05))
        else:
            amount = int(base_income * random.uniform(0.01, 0.03))
        finance_data.append({
            '月份': f'{month}月',
            '科目类型': '收入',
            '科目名称': item,
            '金额': amount
        })
    
    # 成本
    for item in cost_items:
        if item == '主营业务成本':
            amount = int(base_income * random.uniform(0.5, 0.6))
        elif item == '销售费用':
            amount = int(base_income * random.uniform(0.08, 0.12))
        elif item == '管理费用':
            amount = int(base_income * random.uniform(0.06, 0.1))
        elif item == '财务费用':
            amount = int(base_income * random.uniform(0.02, 0.04))
        else:
            amount = int(base_income * random.uniform(0.1, 0.15))
        finance_data.append({
            '月份': f'{month}月',
            '科目类型': '成本',
            '科目名称': item,
            '金额': amount
        })

finance_df = pd.DataFrame(finance_data)

# ===== 2. 销售数据 =====
print("正在生成销售数据...")
n_sales = 120
product_ids = [f'P{i:03d}' for i in range(1, 21)]
customer_ids = [f'C{i:03d}' for i in range(1, 31)]
regions = ['华北', '华东', '华南', '华中', '西南', '西北', '东北']

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

sales_data = []
for i in range(n_sales):
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    pid = random.choice(product_ids)
    qty = random.randint(1, 50)
    price = random.randint(100, 5000)
    sales_data.append({
        '订单ID': f'O{10001+i}',
        '日期': date.strftime('%Y-%m-%d'),
        '产品ID': pid,
        '客户ID': random.choice(customer_ids),
        '区域': random.choice(regions),
        '数量': qty,
        '单价': price
    })

sales_df = pd.DataFrame(sales_data)

# ===== 3. 人力资源数据 =====
print("正在生成人力资源数据...")
n_employees = 80
names = ['张伟', '李娜', '王强', '刘洋', '陈静', '杨帆', '赵敏', '黄磊', '周婷', '吴磊',
         '徐丽', '孙杰', '马云', '朱琳', '胡军', '郭芳', '何平', '高峰', '林雪', '郑宇',
         '谢婷', '宋波', '唐丽', '许强', '韩梅', '冯刚', '曹颖', '彭亮', '曾静', '董伟',
         '袁芳', '蒋军', '蔡丽', '贾平', '魏强', '薛芳', '叶婷', '阎军', '余丽', '潘伟',
         '杜芳', '戴强', '夏丽', '钟伟', '汪芳', '田强', '任丽', '姜伟', '范芳', '方强',
         '邓婷', '沈军', '韩丽', '杨伟', '秦芳', '许强', '何丽', '吕伟', '施芳', '张军',
         '孔丽', '白伟', '崔芳', '康军', '范丽', '孟伟', '钱芳', '邱军', '秦丽', '江伟',
         '尹芳', '黎军', '易丽', '常伟', '武芳', '乔军', '贺丽', '赖伟', '龚芳', '文军']
departments = ['销售部', '技术部', '财务部', '人事部', '市场部', '运营部', '客服部']
positions = ['专员', '主管', '经理', '总监', '副总裁']

hire_start = datetime(2019, 1, 1)
hire_end = datetime(2024, 6, 30)

hr_data = []
for i in range(n_employees):
    hire_date = hire_start + timedelta(days=random.randint(0, (hire_end - hire_start).days))
    dept = random.choice(departments)
    pos = random.choices(positions, weights=[50, 25, 15, 8, 2])[0]
    base_salary = {'专员': 6000, '主管': 10000, '经理': 18000, '总监': 30000, '副总裁': 50000}[pos]
    salary = int(base_salary * random.uniform(0.9, 1.3))
    score = random.choices([1, 2, 3, 4, 5], weights=[5, 15, 40, 30, 10])[0]
    status = random.choices(['在职', '离职'], weights=[85, 15])[0]
    
    hr_data.append({
        '员工ID': f'E{i+1:03d}',
        '姓名': names[i],
        '部门': dept,
        '职位': pos,
        '入职日期': hire_date.strftime('%Y-%m-%d'),
        '基本工资': salary,
        '绩效评分': score,
        '离职状态': status
    })

hr_df = pd.DataFrame(hr_data)

# ===== 4. 库存数据 =====
print("正在生成库存数据...")
categories = ['电子产品', '办公用品', '家居用品', '服装鞋帽', '食品饮料']
product_names = {
    '电子产品': ['笔记本电脑', '手机', '平板电脑', '耳机', '显示器'],
    '办公用品': ['打印机', '扫描仪', '投影仪', '碎纸机', '电话机'],
    '家居用品': ['台灯', '收纳盒', '抱枕', '地毯', '窗帘'],
    '服装鞋帽': ['T恤', '衬衫', '运动鞋', '帽子', '围巾'],
    '食品饮料': ['咖啡豆', '茶叶', '坚果', '果汁', '饼干']
}

inventory_data = []
for cat in categories:
    for pname in product_names[cat]:
        pid = f'P{len(inventory_data)+1:03d}'
        initial = random.randint(50, 500)
        inbound = random.randint(100, 1000)
        outbound = random.randint(50, initial + inbound)
        ending = initial + inbound - outbound
        unit_cost = random.randint(20, 2000)
        inventory_amount = ending * unit_cost
        
        inventory_data.append({
            '产品ID': pid,
            '产品名称': pname,
            '类别': cat,
            '期初库存': initial,
            '入库数量': inbound,
            '出库数量': outbound,
            '期末库存': ending,
            '库存金额': inventory_amount
        })

inventory_df = pd.DataFrame(inventory_data)

# ===== 保存到Excel =====
with pd.ExcelWriter('finance_data.xlsx', engine='openpyxl') as writer:
    finance_df.to_excel(writer, sheet_name='财务数据', index=False)

sales_df.to_excel('sales_data.xlsx', index=False)
hr_df.to_excel('hr_data.xlsx', index=False)
inventory_df.to_excel('inventory_data.xlsx', index=False)

print("\n所有数据文件已生成！")
print(f"- finance_data.xlsx: {len(finance_df)} 行")
print(f"- sales_data.xlsx: {len(sales_df)} 行")
print(f"- hr_data.xlsx: {len(hr_df)} 行")
print(f"- inventory_data.xlsx: {len(inventory_df)} 行")
