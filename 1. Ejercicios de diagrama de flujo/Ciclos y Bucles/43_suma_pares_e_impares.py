num = int(input('Digite un número \n'))
sumaA = 0
sumaB = 0
for i in range(1,num+1):
    if i % 2 == 0:
        n = i * (-1)
        sumaA = sumaA + n
    else:
        sumaB = sumaB + i 
sumaTotal = sumaA + sumaB
print(f'La suma total es de {sumaTotal}')