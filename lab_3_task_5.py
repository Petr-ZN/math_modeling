import numpy as np
import lab_3_task_4 as l3t4

first_column = int(input())
if first_column >= l3t4.m: 
    first_column = -1
second_column = int(input())
if second_column >= l3t4.m:
    second_column = -1

first_column_in_array = l3t4.array[::, first_column]
second_column_in_array = l3t4.array[::, second_column]

l3t4.array[::,first_column] , l3t4.array[::,second_column] = second_column_in_array, first_column_in_array

print (l3t4.array)