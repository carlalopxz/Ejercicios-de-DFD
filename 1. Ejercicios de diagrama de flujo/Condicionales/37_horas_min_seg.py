hours = int(input('Ingrese la hora \n'))
minutes = int(input('Ingrese los minutos \n'))
second = int(input('Ingrese los segundos \n')) 

second = second + 1

if minutes > 59:
    minutes = 0
if hours > 23:
    hours = 0
if second > 59:
    second = 0
    minutes = 0
    if minutes > 59:
        minutos = 0
        hours = hours + 1
        if hours > 23:
            hours = 0

print(f'La hora con un segundo de mas es de {hours}:{minutes}:{second}')