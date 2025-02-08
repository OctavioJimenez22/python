mensaje = input("Proporciona un mensaje a repetir: ")
repeticiones = int(input("Total de veces a repetir: "))

for i in range(repeticiones):
    print(i+1,"-",mensaje)
