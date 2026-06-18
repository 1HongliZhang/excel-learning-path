import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

products = ["笔记本电脑", "智能手机", "平板电脑", "无线耳机", "智能手表", 
            "机械键盘", "无线鼠标", "显示器", "路由器", "移动硬盘"]
regions = ["华北", "华东", "华南", "华中", "西南", "西北", "东北"]

def generate_data():
    data = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(50):
        date = start_date + timedelta(days=random.randint(0, 364))
        product = random.choice(products)
        quantity = random.randint(1, 50)
        unit_price = random.randint(100, 5000)
        
        region = random.choice(regions)
        
        data.append({
            "日期": date.strftime("%Y/%m/%d"),
            "产品": product,
            "销售量": quantity,
            "单价": unit_price,
            "销售额": "",
            "区域": region
        })
    
    df = pd.DataFrame(data)
    
    for i in [5, 12, 18, 25, 33, 40, 47]:
        if i < len(df):
            df.loc[i, "销售量"] = np.nan
            df.loc[i, "单价"] = np.nan
    
    return df

if __name__ == "__main__":
    df = generate_data()
    df.to_excel("sales_basic.xlsx", index=False)
    print("sales_basic.xlsx 已生成")
