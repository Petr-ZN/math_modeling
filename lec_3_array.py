import numpy as np

a = [1, 2, 4]

b = np.array(a)

print (type(a))
print (type(b))

print (b * b) # в отличии от списков, над массивами можно совершать математические операции
print (b / b)
print (b - b)

print (b[-1]) # вызов последнего элемента