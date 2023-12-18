def my_func(a, b):
    x = 3 * a - b
    return x

#tmp = my_func()

def my_func(a=1, b=0):
    x = 3 * a - b
    return x

def my_func(*args):
    x = 3 * args[0] - args[1]
    return x