def prost (a):
    s = 0
    b = a
    while b != 0:
        if a % b == 0:
            s += 1
        b -= 1
    if s == 2:
        return True
    else:
        return False
    
a = int(input())
b = a
while  b!=0:
    if prost(b) and a % b == 0:
        print(b)
    b-=1