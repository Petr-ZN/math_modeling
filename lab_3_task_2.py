import numpy as np

array = np.zeros((2, 2, 2, 2, 2))
for dimension_1 in range (2):
    for dimension_2 in range (2):
        for dimension_3 in range (2):
            for dimension_4 in range (2):
                for dimension_5 in range (2):
                    if dimension_1 == 1 and dimension_2 == 1 and dimension_3 == 1 and dimension_4 == 1 and dimension_5 == 1:
                        break                    
                    array [dimension_1 , dimension_2, dimension_3, dimension_4, dimension_5] = int(input())
print (array)

entered_value = int(input('введите число '))


coordinate_1 = int(input('введите координату 1 '))
coordinate_2 = int(input('введите координату 2 '))
coordinate_3 = int(input('введите координату 3 '))
coordinate_4 = int(input('введите координату 4 '))
coordinate_5 = int(input('введите координату 5 '))

for dimension_1 in range (coordinate_1, 2):
    for dimension_2 in range (coordinate_2, 2):
        for dimension_3 in range (coordinate_3, 2):
            for dimension_4 in range (coordinate_2, 2):
                for dimension_5 in range (coordinate_5, 2):
                    next_value = array[dimension_1, dimension_2, dimension_3, dimension_4, dimension_5]
                    array[dimension_1, dimension_2, dimension_3, dimension_4, dimension_5] = entered_value
                    entered_value = next_value

print (array)