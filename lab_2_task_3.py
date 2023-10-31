a = int(input())
b = ''

while a!=0:
    b += str(a%10)
    a//=10
print(b)