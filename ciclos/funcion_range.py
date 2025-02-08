# Sintaxis funcion range
# inicio- valor inicial (opcional)
# fin- valor final, sin incluirlo
# incremento - diferencia entre cada número (opcional)
#range(inicio, fin, incremento)

print("Secuencia del 0 al 5")

#valor inicio 0, valor fin 5
for i in range(5): #fin 5-1
    print(i, end=" ")
    
print("\n\n")

for i in range(10, 20+1):
    print(i, end=" ")
    
print("\n\n")
#imprimir los números del 20 al 30 de 2 en 2
for i in range(20, 31, 2):
    print(i, end=" ")
