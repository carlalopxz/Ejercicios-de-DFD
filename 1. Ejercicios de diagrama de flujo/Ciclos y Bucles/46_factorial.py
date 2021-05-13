num = int(input('Digite un número para sacar su factorial \n'))
i = 1
factorial = 1
while i <= num:
    factorial = factorial * i
    i = i + 1
print(f'El factorial del número {num} es {factorial}')
