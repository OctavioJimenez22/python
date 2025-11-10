print('funcion par')

#Funcion para saber si un numero es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
#Llamamos a la funcion
if __name__ == '__main__':
    numero = int(input('Ingrese un numero: '))
    print(f'Número par? {es_par(numero)}')
