def main():
    capital=int(input('ingrese la cantidad de de dinero(pesos): '))
    tasa=int(input('ingrese la tasa anual %t: '))
    tiempo=int(input('ingrese la cantidad de año que desea invertir su dinero: '))
    print('Por',tiempo,'años inviertiendo $',capital,'usted recibira de intereses $',capital*(1*tasa/100)*tiempo)
main()
                     
