import random
import pandas as pd
from datetime import datetime, timedelta

products = ["笔记本电脑", "智能手机", "平板电脑", "无线耳机", "智能手表",
            "机械键盘", "无线鼠标", "显示器", "路由器", "移动硬盘"]
regions = ["华北", "华东", "华南", "华中", "西南", "西北", "东北"]
categories = ["电子产品", "外设配件", "存储设备"]

def generate_product_table():
    data = []
    for i, product in enumerate(products):
        category = categories[i // 3] if i // 3 < len(categories) else categories[-1]
        cost = random.randint(200, 3000)
        price = cost * random.uniform(1.3, 2.0)
        
        data.append({
            "产品ID": f"P{i+1:03d}",
            "产品名称": product,
            "类别": category,
            "成本": cost,
            "售价": round(price, 2)
        })
    
    return pd.DataFrame(data)

def generate_sales_table():
    data = []
    start_date = datetime(2024, 1, 1)
    
    for i in range(100):
        date = start_date + timedelta(days=random.randint(0, 364))
        product_id = f"P{random.randint(1, 10):03d}"
        region = random.choice(regions)
        quantity = random.randint(1, 50)
        salesperson = random.choice(["张三", "李四", "王五", "赵六", "孙七"])
        
        data.append({
            "订单ID": f"ORD{i+1:04d}",
            "日期": date.strftime("%Y/%m/%d"),
            "产品ID": product_id,
            "区域": region,
            "数量": quantity,
            "销售员": salesperson
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    df_products = generate_product_table()
    df_sales = generate_sales_table()
    
    with pd.ExcelWriter("sales_model_for_power_pivot.xlsx") as writer:
        df_products.to_excel(writer, sheet_name="产品表", index=False)
        df_sales.to_excel(writer, sheet_name="销售表", index=False)
    
    print("sales_model_for_power_pivot.xlsx 已生成")
