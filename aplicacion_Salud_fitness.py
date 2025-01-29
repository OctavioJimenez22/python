print("Aplicación de Salud y Fitness")

METAS_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.4 # valor aproximado

nobre = input("Cual es tu nombre? ")
pasos_diarios = int(input("Cuántos pasos has caminado hoy? "))

meta_alcanzada = pasos_diarios >= METAS_PASOS_DIARIOS
meta_alcanzada_txt = "si" if meta_alcanzada else "no"

calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

print(F"Usuario: {nobre}\nPasos dados hoy: {pasos_diarios}\nCalorias quemadas: {calorias_quemadas}")
print(f"Meta de pasos diario alcanzada: {meta_alcanzada_txt}")
print(F"La meta de pasos diarios es de: {METAS_PASOS_DIARIOS} pasos") 