a = int(input())
while a!=0:
    s = 0
    for i in range (1, a):
         if a % i == 0:
             s += i
    if s==a:
        print (f'число {a} совершенное')

    a -= 1
    