import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""ar =  [1,2,3,4,5]
ar2 =  ("a", "c", "d" ,2,3,4,5)
data = pd.Series(ar, index = ("a", "b", "c", "d", "e"))
data2 = pd.Series(ar2)

print(ar)
print(data)


data3 =  {'name' : 'IBM', 'date' : '2010-09-08', 'shares' : 100, 'price' : 10.2}
ds = pd.Series(data3)
print(ds)


data4 = {"Name":["John", "wale", "Biodun", "Ben"], "age": [20, 30, 35, 37],
         "Score":[60, 70, 71, 20], "grade":[ "B", "B", "A", "F"]}
data5 = pd.DataFrame(data4)
data5.set_index("")



print(data5)


data ={"age":[10, 20,40],
       "name":["Ade","John", "Ayo"]

    }
df = pd.DataFrame(data)
print(df)
print("========Specific data======")
print(df.loc[[0, 1]])"""

df1 = pd.read_csv("data.txt", index_col=None)
print(df1)
print(df1["Duration"][0])
print(len(df1))



