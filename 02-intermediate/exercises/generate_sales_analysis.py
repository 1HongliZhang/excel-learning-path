import random
import pandas as pd
from datetime import datetime, timedelta

products = ["笔记本电脑", "智能手机", "平板电脑", "无线耳机", "智能手表", 
            "机械键盘", "无线鼠标", "显示器", "路由器", "移动硬盘"]
regions = ["华北", "华东", "华南", "华中", "西南", "西北", "东北"]
salespeople = ["张三", "李四", "王五", "赵六", "孙七", "周八"]

def generate_data():
    data = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(100):
        date = start_date + timedelta(days=random.randint(0, 364))
        product = random.choice(products)
        region = random.choice(regions)
        salesperson = random.choice(salespeople)
        amount = random.randint(1000, 50000)
        
        data.append({
            "产品": product,
            "区域": region,
            "销售额": amount,
            "日期": date.strftime("%Y/%m/%d"),
            "销售员": salesperson
        })
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = generate_data()
    df.to_excel("sales_analysis_raw.xlsx", index=False)
    print("sales_analysis_raw.xlsx 已生成")
