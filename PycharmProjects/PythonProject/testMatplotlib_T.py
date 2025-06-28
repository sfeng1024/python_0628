import matplotlib.pyplot as plt
import pandas as pd

people = pd.read_excel("/Users/fengshuai/PycharmProjects/PythonProject/6789.xlsx")
scry_column = people.iloc[:,2]
scry_list = scry_column.tolist()

plt.bar(['A','B'],[30,40])
plt.show()

