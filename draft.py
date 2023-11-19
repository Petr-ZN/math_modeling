import numpy as np

array_first = np.zeros((2,2))

for string in range(2):
    for column in range(2):
        if string == 1 and column == 1:
            break
        array_first[string, column] = int(input())

print (array_first)
entered_value = int(input('введите число '))

a1 = int(input('введите позицию '))
a2 = int(input('введите позицию '))

for string in range (a1, 2):
    for column in range (a2, 2):
        a = array_first[string, column]
        array_first[string, column] = entered_value
        entered_value = a

print (array_first)