password = input("Ingrese un password (debe tener al menos 6 caracteres): ")

while len(password) < 6:
    print("El password no cumple con los requisitos. Debe tener al menos 6 caracteres")
    password = input("Ingrese un nuevo valor de password: ")
else: 
    print("El valor del apssword es válido")