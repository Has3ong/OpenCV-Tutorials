import numpy as np

print(np.arange(0, 10, 2))

print('===================================================')

print(np.zeros(shape=(10, 5)))

print('===================================================')

print(np.ones((2, 4)))

print('===================================================')

np.random.seed(101)
print(np.random.randint(0, 100, 10))


print('===================================================')

matrix = np.arange(0, 100).reshape(10, 10)
print(matrix)

print('===================================================')

matrix2 = matrix[:,1]. reshape(1, 10)
print(matrix2)

print('===================================================')

matrix3 = matrix[0:3, 0:3]
print(matrix3)

print('===================================================')

matrix[0:5, :] = 333
print(matrix)