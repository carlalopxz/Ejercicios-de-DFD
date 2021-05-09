a = int(input('Ingrese el primer numero \n'))
b = int(input('Ingrese el segundo numero \n'))
c = int(input('Ingrese el tercer numero \n'))

if c > b and c > a:
    if b > a:    
        print('No se introdujeron en orden decreciente')
elif a == b and a == c:
    print('Los 3 números son iguales')
else:
    print('Se introdujeron en orden decreciente')

