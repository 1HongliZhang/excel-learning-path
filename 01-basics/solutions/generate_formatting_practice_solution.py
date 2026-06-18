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
        name = random.choice(names) + str(random.randint(1, 100))
        hire_date = start_date + timedelta(days=random.randint(0, 2555))
        department = random.choice(departments)
        salary = random.randint(4000, 25000)
        
        if salary >= 15000:
            salary_level = "高薪"
        elif salary >= 8000:
            salary_level = "中薪"
        else:
            salary_level = "底薪"
        
        data.append({
            "姓名": name,
            "入职日期": hire_date.strftime("%Y/%m/%d"),
            "部门": department,
            "薪资": salary,
            "薪资等级": salary_level
        })
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = generate_data()
    df.to_excel("formatting_practice_solution.xlsx", index=False)
    print("formatting_practice_solution.xlsx 已生成")
