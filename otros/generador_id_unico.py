from random import randint 

nombre = input("Ingrese su nombre: ")
apellido = input(f"{nombre}, Ingrese su apellido: ")
anio_nacimiento = input("Año de nacimiento (YYY): ")

nombre_2 = nombre.upper().strip()[0:2]  # [0:""] para recuperar los dos primeros valores
apellido_2 = apellido.upper().strip()[0:2]
anio_nacimiento_2 = anio_nacimiento.strip()[2:]  #como solo es año indicamos los dos ultimos dos num

#vamos a generar el valor aleatorio de 4 ddigitos
aleatorio = randint(1000,9999)

#generamos el Id unico
id_unico = f"{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}"

print(f"\nHola {nombre}")
print(f"Tu nuevo numero de Id generado por el sistema es: {id_unico}\nFelicidades!!")

