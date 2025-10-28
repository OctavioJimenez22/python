print("Tarifas del hotel")
print("Cuarto con vista al mar $190.50 por día\nCuarto sin vista al mar $150.50 por día")

vista_si = 190.50
vista_no = 150.50

nombre =  input("Ingrese su nombre: ")
dias_estadia = int(input("Cuantos días desea quedarse: "))
cuarto_vista = input("Cuarto con vista al mar (si/no): ")
cuarto_vista = cuarto_vista.strip().lower()

if cuarto_vista == "si":
    costo = dias_estadia * vista_si
else:
    costo = dias_estadia * vista_no

print(f"Hola {nombre}\nTú total de {dias_estadia} días. {cuarto_vista} Tiene vista al mar.")
print(f"El costo total del cuarto es de: {costo:.2f}")