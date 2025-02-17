print("Triángulo simetrico")

filas = int(input("Proporciona un total de filas: "))

for i in range(1, filas+1):
    espacios_blanco = " " * (filas - i)
    asteriscos = "*" * (2*i-1)
    print(f"{espacios_blanco}{asteriscos}")
    