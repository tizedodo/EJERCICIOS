def main():
    tanque=1000
    pileta=3000
    balde=10
    print('el tanque contiene:',tanque,'litros de agua y la pileta',pileta,'litros')
    cant_baldes=1
    print('transvasa', cant_baldes,'baldes de agua de:',balde,'litros')
    tanque=tanque-cant_baldes*balde
    pileta = pileta + cant_baldes * balde
    print ( 'El tanque contiene:', tanque, 'litros de agua y la pileta:', pileta, 'litros')
    cant_baldes = cant_baldes + 1
    print('Transvasa',cant_baldes,'baldes de agua de:',balde,'litros')
    tanque=tanque-cant_baldes*balde
    pileta=pileta+cant_baldes*balde
    print('El tanque contiene:',tanque,'litros de agua y la pileta:',pileta,'litros')
    cant_baldes = cant_baldes + 1
    print ('Transvasa',cant_baldes, 'baldes de agua de:',balde, 'litros')
    tanque=tanque-cant_baldes*balde
    pileta=pileta+cant_baldes*balde
    print('El tanque contiene:',tanque,'litros de agua y la pileta:', pileta, 'litros')
main()
