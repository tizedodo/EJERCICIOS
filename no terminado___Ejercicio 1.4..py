dinero=10000
paraguas=10
print('Dinero disponible $',dinero,'y',paraguas,'paraguas a la venta')
cant_vendida=5
precio_vendida=400
print('A consecuencias de la ultima venta')
print('Dinero disponible $',(cant_vendida*precio_vendida)+dinero,'y',paraguas-cant_vendida,'paraguas restante a la venta')
paraguas=paraguas-cant_vendida

print('vendiendo la mita de los restantes')
precio_vendida=400
cant_vendida=(5/2)
dinero=(cant_vendida*precio_vendida)+dinero
print('Dinero disponible $',dinero,'y',paraguas//2,'paraguas restante a la venta')
