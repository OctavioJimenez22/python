print('Argumentos variables')

#El *args solo se pone al final de los parametros
def superheroe_superpoderes(superheroe, nombre, *args):  #se pone el *args para indicar
    print(f'Superheroe: {superheroe} - {nombre} - {args}')   #no se pone *en el args porque es para mostrar
    
    #iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')
        
        
#llamamos la funcion
superheroe_superpoderes('Spiderman', 'peter parker', 'trepar muros', 'instinto arácnido')
superheroe_superpoderes('Hulk', 'Jose', 'fuerza sobrehumana', 'piel resistente', 'salto gigante')
