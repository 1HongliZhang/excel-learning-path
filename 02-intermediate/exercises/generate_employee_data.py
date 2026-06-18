import random
import pandas as pd
from datetime import datetime, timedelta

names = ["张三", "李四", "王五", "赵六", "孙七", "周八", "吴九", "郑十",
         "钱十一", "陈十二", "杨十三", "黄十四", "周十五", "吴十六", "郑十七",
         "王十八", "冯十九", "陈二十", "褚二十一", "卫二十二"]
departments = ["销售部", "技术部", "人事部", "财务部", "市场部", "运营部"]

def generate_data():
    data = []
    start_date = datetime(2018, 1, 1)
    
    for i in range(50):
        emp_id = f"{i+1:03d}"
        name = random.choice(names) + str(random.randint(1, 100))
        department = random.choice(departments)
        salary = random.randint(4000, 25000)
        hire_date = start_date + timedelta(days=random.randint(0, 2555))
        
        data.append({
            "ID": emp_id,
            "姓名": name,
            "部门": department,
            "薪资": salary,
            "入职日期": hire_date.strftime("%Y/%m/%d")
        })
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = generate_data()
    df.to_excel("employee_data.xlsx", index=False)
    print("employee_data.xlsx 已生成")
