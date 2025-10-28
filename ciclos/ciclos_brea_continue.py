print("Break y continue\n")


#Ejemplo con break
print("Palabra break:")
for numero in range(1,10):
    if numero %2 ==0:    #número par
        print(numero)
        break# salir del ciclo inmediatamente (luego de encontrar la primer acción)
    
   
#Ejemplo con conitnue
print("\nPalabra continue:")
for numero in range(1,20):
    if numero %2 ==1:  #número impar
        continue    #continua con las repeticiones
    print(numero) # numeros pares