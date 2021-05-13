num = int(input('Digite un número \n'))
mult = 1
suma = 0
if num > 10:
    for i in range(1,num+1):
        mult = mult * i
    print(f'La multiplicación es de {mult}')
else:
    for i in range(num+1):
        suma = suma + i
    print(f'La suma es de {suma}')
