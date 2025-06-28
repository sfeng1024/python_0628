import datetime
formats = [
    "%Y-%m-%d",     # 2024-06-01
    "%Y/%m/%d",     # 2024/06/01
    "%Y.%m.%d",     # 2024.06.01
    "%Y%m%d",       # 20240601
    "%d-%m-%Y",     # 01-06-2024
    "%d/%m/%Y",     # 01/06/2024
    "%m/%d/%Y",     # 06/01/2024
    "%d %b %Y",     # 01 Jan 2024
]
birth_date = None
birth_input = input("输入出生年月日" + ":" +"（格式：YYYY-MM-DD）")
today = datetime.date.today()

for ftm in formats:
    try:
        birth_date = datetime.datetime.strptime(birth_input, ftm).date()
        break
    except ValueError:
        continue
age: int = today.year - birth_date.year
if age < 20:print("您的年龄为" + str(age) + "  小年轻")
elif 20 < age < 30:print("您的年龄为" + str(age) +"  成人")
elif age < 40 and age > 30:print("您的年龄为" + str(age) +"  成家立业")
elif 40 < age < 50:print("您的年龄为" + str(age) +"  事业有成")
elif 50 < age < 60:print("您的年龄为" + str(age) +"  修身养性")
elif 60 < age < 70:print("您的年龄为" + str(age) +"  修身养性不问红尘")
elif 70 < age < 80:print("您的年龄为" + str(age) +"  儿孙满堂")
elif 80 < age < 90:print("您的年龄为" + str(age) +"  老头")
else:
    print("您的年龄为" + str(age) + "  要么太小要么太老")
# birth_date = datetime(1987,10,24)
# print('Hello' + "  AI" + "  I'm coming")

