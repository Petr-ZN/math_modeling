a = [1, 3, 6] # создание списка
print (a[0]) # вызов нулевого элемента

b = [8, 9, 10]

c = a+b
print (c)

#c = a-b

print(c*2)

c.append('Good') # Добавление элемента в конец списка
print (c)

a.append(b) # a = [1, 3, 6, [8, 9, 10]] //a содержит 3 злемента
print (a) 

print (len(a))