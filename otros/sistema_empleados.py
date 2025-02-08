nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
salario = float(input("Ingrese su salario: "))
es_jefe = input("Es jefe de departamento. si/no ")

es_jefe = es_jefe.lower() == "si"

print(f"\nSu nombre es {nombre}\nSu edad es: {edad}\nSu salario es: {salario:.2f}\nEs jefe de departamento? {es_jefe}")