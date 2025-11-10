# *args - argumentos - tupla
# **kawargs - keyword arguments (keys, value) como dict
print('Argumentos variables en forma de dict')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')
    
superheroe_superpoderes('Spiderman', 'Instinto arácnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Ironman', 'Armadura', 'playboy', edad=45)

#Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino',  persona='Buena onda')
