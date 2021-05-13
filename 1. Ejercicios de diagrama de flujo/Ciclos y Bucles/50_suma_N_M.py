n = int(input('Ingrese un número N \n'))
m = int(input('Ingrese un número M \n'))
suma = 0
if n < m:
    for i in range(n,m):
        suma = suma + i 
    print(f'La suma de N hasta M es de {suma}')
else: 
    for i in range(m,n):
        suma = suma + i 
    print(f'La suma de M hasta N es de {suma}')