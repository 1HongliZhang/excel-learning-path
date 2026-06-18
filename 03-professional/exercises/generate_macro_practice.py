import random
import pandas as pd
from datetime import datetime, timedelta

products = ["笔记本电脑", "智能手机", "平板电脑", "无线耳机", "智能手表"]
regions = ["华北", "华东", "华南", "华中", "西南"]

def generate_data():
    data = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(50):
        date = start_date + timedelta(days=random.randint(0, 364))
        product = random.choice(products)
        region = random.choice(regions)
        quantity = random.randint(1, 50)
        unit_price = random.randint(100, 5000)
        
        data.append({
            "日期": date.strftime("%Y/%m/%d"),
            "产品": product,
            "区域": region,
            "销售量": quantity,
            "单价": unit_price,
            "销售额": ""
        })
    
    df = pd.DataFrame(data)
    df.to_excel("macro_practice.xlsx", index=False)
    print("macro_practice.xlsx 已生成")

if __name__ == "__main__":
    generate_data()
