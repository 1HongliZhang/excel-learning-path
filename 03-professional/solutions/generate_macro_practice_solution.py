import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# 生成销售数据
n = 50
products = ['产品A', '产品B', '产品C', '产品D', '产品E']
regions = ['华北', '华东', '华南', '华中', '西南']

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

data = []
for i in range(n):
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    qty = random.randint(10, 200)
    price = random.randint(50, 500)
    data.append({
        '日期': date.strftime('%Y-%m-%d'),
        '产品': random.choice(products),
        '区域': random.choice(regions),
        '销售量': qty,
        '单价': price,
        '销售额': qty * price
    })

df = pd.DataFrame(data)

# 保存为xlsx（VBA宏需在Excel中手动添加，答案文件提供完成计算后的数据）
df.to_excel('macro_practice_solution.xlsx', index=False)

print('macro_practice_solution.xlsx 已生成')
print('注意：VBA宏需在Excel中手动添加，请参考solution_process.md中的步骤')
