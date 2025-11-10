print('Imprimir del 1 al 5 de fomra recursiva')

#definir la funcion recursiva
def funcion_recursiva(numero):
    #caso base
    if numero ==1:
        print(numero, end= ' ')
    else: #caso recursivo
        funcion_recursiva(numero -1)
        print(numero, end= ' ')

#programa principal
funcion_recursiva(8)     