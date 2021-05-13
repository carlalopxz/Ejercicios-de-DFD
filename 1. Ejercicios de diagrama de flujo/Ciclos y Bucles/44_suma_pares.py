a = int(input('Ingrese un número A \n'))
b = int(input('Ingrese un número B \n'))
suma = 0 
for i in range(a,b+1):
    if i % 2 == 0:
        suma = suma + i 
print(f'La suma total de los números pares es de {suma}')