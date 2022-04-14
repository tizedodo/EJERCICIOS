def main():
    tanque=int(input('Porfavor ingre la cantidad de agua inicial del tanque: '))
    pileta=int(input('Porfavor ingre la cantidad de agua inicial de la pileta: '))
    cant_balde=10
    for balde in range(0,5):
        print('el tanque contiene:',tanque-(balde*cant_balde),'litros de agua y la pileta',pileta+(balde*10),'litros')
        tanque=tanque-(balde*cant_balde)
        pileta=pileta+(balde*10)
        print('transvasa',balde+1,'baldes de agua de:10 litros')













