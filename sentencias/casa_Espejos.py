edad = int(input("Cual es tu edad? "))
miedo_oscuridad = input("Tienes miedo a la oscuridad (si/no): ")
miedo_oscuridad = miedo_oscuridad.strip().lower() == "si"

if not miedo_oscuridad and edad >= 10:
    print("Puedes entrar")
else: 
    print("Lo siento, la casa de los espejos podria darte miedo")