print('Impremir detalles de una persona usando kwargs')

#Definimos una funcion que acepta argumentos variables en forma de llave-valor dict

def imprimir_Detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave} : {valor}')
        
#Llamamos la funcion
imprimir_Detalle_persona(nombre = 'Tavo', edad =30, ciudad = 'Medellin')
imprimir_Detalle_persona(nombre = 'Camila', edad = 25, ciudad= 'Medellin')

