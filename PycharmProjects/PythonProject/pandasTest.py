import pandas as pd

df = pd.DataFrame({"ID":[1,2,3],"NAME":['tomy','Jim','pole'],"scry":[400000,500000,600000]})
df.to_excel("/Users/fengshuai/PycharmProjects/PythonProject/6789.xlsx", index=False)
print("保存成功！")