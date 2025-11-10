print('Alcance de variables')

contador_global = 0  # Variable global

def incrementar_contador():
    contador_local = 0  # Variable local
    contador_local += 1

    #usar la variable global
    global contador_global  #para esto colocamos global para poder llamarla
    contador_global += 1
    print(f'Contador local: {contador_local}\nContador global: {contador_global}')

# Llamamos varias veces la función
incrementar_contador()
incrementar_contador()
incrementar_contador()

print(f'Contador global: {contador_global}')