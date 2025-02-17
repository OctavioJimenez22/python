print("Promedio de calificaciones")

numero_calificaciones = int(input("Cuantas calificaciones quieres evaluar: "))
calificaciones = []

for i in range(numero_calificaciones):
    calificacion = float(input(f"Calificacion[{i}]= "))
    calificaciones.append(calificacion)

print(F"\nLas calificaciones proporcionadas son: {calificaciones}")

suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones/numero_calificaciones

print(f"\nPromedio de las calificaciones: {promedio:.2f}")