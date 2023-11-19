import numpy as np

number_of_row = int(input('введите количество строк '))
number_of_column = int(input('введите количество столбцов '))

spisoc = []

array = np.zeros((number_of_row, number_of_column))

for string in range (number_of_row):
    for column in range (number_of_column):
        array[string, column] = int(input('введите новый элемент массива '))

print (array)

for column in range (number_of_column):
    for row in range (number_of_row):
        spisoc.append(array[row, column])
    print (max(spisoc))
    spisoc = []