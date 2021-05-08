compra = int(input('Ingrese el valor de la compra \n'))

if compra > 1000:
    descuento = compra * 0.20
    precioFinal = compra - descuento
    print(f'el precio final con el descuento es de {precioFinal} pesos')
else: 
    print(f'No se hace ningun descuento')