import pandas as pd
import numpy as np

list1= [1,2,3,4]

list1 = pd.Series()

list1 = np.array([1,2,3,4])
list1 = pd.Series([1,2,3,4])
print(list1)
print("===DataFrame without data===")
data = pd.DataFrame()
print(data)
print("===DataFrame with data===")
data = pd.DataFrame([1,2,3,4])
print(data)

print("===DataFrame with data===")
data1 = pd.DataFrame(["John", "Ade","Kunle"])
print(data1)


lst = ['Geeks', 'For', 'Geeks', 'is',  
            'portal', 'for', 'Geeks'] 
data3 = pd.DataFrame(lst)

print(data3)


print("====DataFrame from Dictionary===")
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18], "Height":[20,31,26,15]}
data2 = pd.DataFrame(data)
data2 = np.set_index(age)
print(data2)
  
