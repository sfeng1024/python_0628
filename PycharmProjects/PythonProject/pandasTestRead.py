import pandas as pd

people = pd.read_excel("/Users/fengshuai/PycharmProjects/PythonProject/6789.xlsx")
print(people)
print(people.columns)
scry_column = people.iloc[:,2]
scry_hang = people.iloc[1,:]
scry_list = scry_column.tolist()
scry_listhang = scry_hang.tolist()
print(scry_list)
averg = sum(scry_list) / len(scry_list)
max = max(scry_list)
min = min(scry_list)
count = people.count()
print(averg)
print(max)
print(min)
print(count)
print(scry_hang)
print(scry_listhang)