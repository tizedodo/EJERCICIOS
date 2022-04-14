def main():
    dinero = 1000
    sombreros = 0
    precio = 0
    cant_venta = 0
    sombreros = int(input('ingrese la cantidad inicial de sombreros: '))
    precio = float(input('ingrese el precio de venta de cada unidad: '))
    print('Total dinero disponible en caja:$',dinero,'pesos')
    print('La cantidad de sombreros disponibles para la venta:', sombreros,'sombreros')
    input("Ingrese enter para seguir")

    print('Las variaciones que resultan de la venta de la tercera parte (1/3) de los sombreros disponibles para la venta.')
    cant_venta = sombreros //3
    print('Vendieron en total:',cant_venta,'sombreros','a un precio de cada unidad $',precio,'pesos')
    print('La cantidad de sombrero restante para la venta:', sombreros - cant_venta,'sombreros')
    sombreros = sombreros - cant_venta
    print('La cantidad de dinero disponible en caja:', (cant_venta * precio)+dinero,'pesos')
    dinero = (cant_venta * precio)+dinero 
    input("Ingrese enter para seguir")

    print('la venta de la mitad (1/2) de sombreros restantes')
    cant_venta = sombreros //2 
    print('Vendieron en total:',cant_venta,'sombreros','a un precio de cada unidad $',precio,'pesos')
    print('La cantidad de sombrero restante para la venta:',sombreros - cant_venta,'sombreros' )
    print('La cantidad de dinero disponible en caja:', (cant_venta * precio)+dinero,'pesos')
    
main()
    
