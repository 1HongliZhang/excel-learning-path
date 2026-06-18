import random
import pandas as pd
from datetime import datetime, timedelta

products = ["笔记本电脑", "智能手机", "平板电脑", "无线耳机", "智能手表"]
regions = ["华北", "华东", "华南", "华中", "西南"]

def generate_data():
    data_sheet1 = []
    data_sheet2 = []
    
    start_date = datetime(2024, 1, 1)
    
    for i in range(30):
        date = start_date + timedelta(days=random.randint(0, 180))
        product = random.choice(products)
        region = random.choice(regions)
        sales = random.randint(1000, 50000)
        
        data_sheet1.append({
            "日期": date.strftime("%Y-%m-%d"),
            "产品名称": product,
            "销售区域": region,
            "销售额(元)": sales
        })
    
    for i in range(30):
        date = start_date + timedelta(days=random.randint(180, 364))
        product = random.choice(products)
        region = random.choice(regions)
        sales = random.randint(1000, 50000)
        profit = sales * random.uniform(0.1, 0.3)
        
        data_sheet2.append({
            "销售日期": date.strftime("%Y年%m月%d日"),
            "产品": product,
            "区域": region,
            "金额": sales,
            "利润": round(profit, 2)
        })
    
    df1 = pd.DataFrame(data_sheet1)
    df2 = pd.DataFrame(data_sheet2)
    
    with pd.ExcelWriter("messy_data_for_power_query.xlsx") as writer:
        df1.to_excel(writer, sheet_name="上半年数据", index=False)
        df2.to_excel(writer, sheet_name="下半年数据", index=False)
    
    print("messy_data_for_power_query.xlsx 已生成")

if __name__ == "__main__":
    generate_data()
