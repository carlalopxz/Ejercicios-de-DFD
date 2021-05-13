num = int(input('Ingrese un número \n'))
x = 0
y = 1
z = 1
for i in range(num):
    z = x + y
    x = y 
    y = z
    print(f'El resultado de la serie Fibonacci es {z}')