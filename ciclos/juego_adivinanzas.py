from random import randint

print("***Juego de adivinanzas!!***\n")

numero_secreto = randint(1, 50)
intentos = 1
adivinanza = None
INTENTOS_MAXIMOS = 5

while adivinanza != numero_secreto and intentos <= INTENTOS_MAXIMOS:
    print("Adivina el número secreto (1-50)")
    adivinanza = int(input(f"intento #{intentos}. Ingresa el número: "))
    if adivinanza < numero_secreto:
        print("El número secreto es mayor")
    elif adivinanza > numero_secreto:
        print("El número secreto es menor")
    intentos += 1
    
if adivinanza == numero_secreto:
    print(F"\nfELICIDADES!! Advinaste el número secreto: {numero_secreto} en {intentos} intentos.")
elif adivinanza != numero_secreto:
    print(f"No encontraste el número secreto, has agotado tus intentos. El número secreto era: {numero_secreto}")