import random

total_compra = int(input('Ingrese el valor de su compra total \n'))

bolita = random.randint(1,5)

if bolita == 1:
    print('Salió la bolita blanca, no se le hace ningun descuento')
    total_a_pagar = total_compra
    print('Precio total $',total_a_pagar)
elif bolita == 2:
    print('Salió la bolita verde - descuento del 10%')
    total_a_pagar = total_compra * 0.10
    print('Precio total $',total_a_pagar)
elif bolita == 3:
    print('Salió la bolita amarilla - descuento del 25%')
    total_a_pagar = total_compra * 0.25
    print('Precio total $',total_a_pagar)
elif bolita == 4:
    print('Salio la bolita azul - descuento del 50%')
    total_a_pagar = total_compra * 0.50
    print('Precio total $',total_a_pagar)
else:
    print('Salio la bolita roja - SU COMPRA ES GRATIS! :D')


