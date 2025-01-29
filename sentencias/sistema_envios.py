COSTO_NACIONAL = 10
COSTO_INTERNACIONAL = 20

print(f"El costo nacional por kilo nacional es de {COSTO_NACIONAL}")
print(f"El costo internacional por kilo es de {COSTO_INTERNACIONAL}")

destino = input("Tu destino es nacional o internacional: ").strip().lower()
peso = float(input("Ingrese el peso del paquete (en kg): "))
total = None

if destino == "nacional":
    total = peso * COSTO_NACIONAL
elif destino == "internacional":
    total = peso * COSTO_INTERNACIONAL
else:
    total = "Error"

print(f"El costo total del envio del paquete es de: {total:.2f}")