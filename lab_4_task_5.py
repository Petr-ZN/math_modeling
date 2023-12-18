def square (key, *a):
    if key == 'circle':
        print (3.14*a[0]**2)
    elif key == 'rectangle':
        print (a[0]* a[1])
    elif key == 'triangle':
        print (a[0]*a[1]/2)
    
square ('circle', 5)
square ('rectangle', 3, 4)
square ('triangle', 4, 2)