import numpy as np

array_first = np.zeros((3,4))
array_second = np.zeros((3,4))

for string in range(3):
    for column in range(4):
        array_first[string, column] = int(input())

for string in range(3):
    for column in range(4):
        array_second[string, column] = int(input())

array_third = np.zeros((3,4))
for string in range(3):
    for column in range(4):
        array_third[string, column] = max(array_first[string, column], array_second[string, column] )

print(array_first)
print(array_second)
print (array_third)