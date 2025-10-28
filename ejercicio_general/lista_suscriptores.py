print("Lista de Suscriptores\n")

suscriptores = set()  #Aqui definimos un diccionario vacio
num_suscriptores = int(input("Ingrese el numero de suscriptores iniciales: "))
for _ in range(num_suscriptores):
    suscriptores.add(input("Nuevo suscriptor (email): "))
    
print(f'Lista inicial de suscriptores: {suscriptores}')

#verificar si un suscriptor ya esta
nuevo_suscriptor = input("Ingrese un nuevo suscriptor (email): ")
print(f'Verificando si el suscriptor {nuevo_suscriptor} ya esta en la lista')

if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya esta en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'Se ha agregado el nuevo suscriptor: {nuevo_suscriptor}')
    print(f'Lista actualizada de suscriptores: {suscriptores}')

#eliminar suscriptor
suscriptor_eliminar = input("Ingrese el suscriptor que vas a eliminar: ")
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado')
print(f'Lista actualizada de suscriptores: {suscriptores}')
