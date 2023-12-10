import numpy as np
#data = np.loadtxt("data1.txt", delimiter = " ")
data = [[1,2,3,4],[4, 6, 78, 100]]
data1 = np.array(data)
print(data1)

data2 = np.copy(data1)
print(data2)

#print(data2.tolist())
print(data2.T)

#Appending to np array

print(np.append(data2, 31))
print(np.insert(data2, 4, 11))


data3 =[1,2,3,4]
data4 =[1,3,3,4]
data3= np.array(data3)
data4 = np.array(data4)
data7 = np.concatenate((data3, data4), axis = 0)
print(data7)

print(data3 + data4)
print(np.power(data3, 2))

print("Abraham "*6)
a = np.array_equal(data3, data4)
if a:
    print("The arrays are eqaul")
else:
    print("Not tally.")

