a = int(input())
b = int(input())
c = int(input())

if a > b+c or b > a+c or c > a+b:
    print ('такой треугольник не существует')
else:
    if a==b and b==c:
        print('треугольник равносторонний')
    elif a==b or b==c:
        print('треугольник равнобеlренный')
    else:
        print('треугольник разносторонний')