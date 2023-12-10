import numpy as np
A = [[2,1,3], [4,1,5]]
A = np.array(A)
print("Dimension is: ", A.ndim)
print("Dimension is: ", A.shape)
print("Type is: ", type(A))


a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'complex')
print ("Array created using passed list:\n", a)

d = np.full((3, 3), 6, dtype = 'complex')
print(d)

#create an array of 4X4 matrix with all elements 0

zer = np.zeros((4,4), dtype ="int")
print(zer)

a = np.arange(2, 9, 1)
print(a)
