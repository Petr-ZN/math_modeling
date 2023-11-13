a = int(input())
b = int(input())
c = int(input())

d = b**2 - 4*a*c

if d < 0:
    print('Корней нет')
elif d == 0:
    print(f'корень уравнения:  {-b / (2*a)}')
else:
    print(f'первый корень = {(-b + d**0.5) / (2*a)}')
    print(f'второй корень = {(-b - d**0.5) / (2*a)}')
