num = int(input('Ingrese un número \n'))
suma = 0 
cont = 0
i = 0
while i <= num:
    i = i + 1
    if i % 2 == 0:
        suma = suma + i 
        cont = cont + 1 
print(f'La suma de los números pares es de {suma} y son {cont} números pares')