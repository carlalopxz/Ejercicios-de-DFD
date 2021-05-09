import math

a = int(input('Ingrese el número A \n'))
b = int(input('Ingrese el número B \n'))
c = int(input('Ingrese el número C \n'))

y = (b * b - 4 * a * c)
rta1 = 0
rta2 = 0

if y > 0:
    rta1 = (-b + math.sqrt(y)) / (2 * a)
    rta2 = (-b - math.sqrt(y)) / (2 * a)
    print(f'La solución 1 de la ecuación es {rta1}')
    print(f'La solución 2 de la ecuación es {rta2}')
else:
    print('La ecuación no tiene solucion real')


