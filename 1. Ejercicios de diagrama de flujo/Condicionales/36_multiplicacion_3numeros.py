x = int(input('Ingrese un número X \n')) 
y = int(input('Ingrese un número Y \n')) 
z = int(input('Ingrese un número Z \n'))

if x * y == z:
    print(f'La suma de {x} * {y} es = {z}')
else:
    print(f'{z} no es el resultado de la multiplicación entre {x} y {y}')
