MAXIMO = 5
numero = 1
acumulador = 0

while numero <= MAXIMO:
    print(f"Acumulador de suma: {acumulador} + {numero}")
    acumulador += numero
    numero +=1
print(f"\nEl resultado de la suma acumalada es: {acumulador}")