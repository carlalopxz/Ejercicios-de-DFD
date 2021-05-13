num = int(input('Ingrese un número para saber si es primo \n'))
cont = 0
for i in range(1,num+1):
    if num % i == 0:
        cont = cont + 1
if cont > 2:
    print(f'El número {num} no es primo')
else:
    print(f'El número {num} es primo')
