num = int(input('Ingrese un número \n'))
factorial = 1
acum = 0 
for i in range(1,num+1):
    for j in range(1,num - i + 1):
        factorial = factorial * j 
    acum = acum + factorial 
print(f'El resultado final es {acum}')