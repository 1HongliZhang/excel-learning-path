import random
import pandas as pd
from datetime import datetime, timedelta

products = ["电子产品", "服装鞋帽", "食品饮料", "家居用品", "办公用品"]
regions = ["北京", "上海", "广州", "深圳", "成都", "杭州"]
months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

def generate_data():
    data = []
    
    for month in months:
        for product in products:
            for region in regions:
                sales = random.randint(5000, 50000)
                profit = sales * random.uniform(0.1, 0.3)
                cost = sales - profit
                
                data.append({
                    "月份": month,
                    "产品类别": product,
                    "地区": region,
                    "销售额": sales,
                    "成本": round(cost, 2),
                    "利润": round(profit, 2)
                })
    
    df = pd.DataFrame(data)
    df.to_excel("dashboard_data.xlsx", index=False)
    print("dashboard_data.xlsx 已生成")

if __name__ == "__main__":
    generate_data()
