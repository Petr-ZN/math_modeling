def fib (n):
    if n == 1:
        print (0)
        return
    a = 0
    b = 1
    for i in range (2,n):
        if a < b:
            a += b
        else:
            b +=a
    if a > b:
        print (f'{n} = {a}')
    else:
        print (f'{n} = {b}')

fib (1)
fib (2)
fib (3)
fib (4)
fib (5)
fib (6)