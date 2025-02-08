print("*** GENERADOR EMAIL ***")

nombre_completo = " Tavo Jimenez "
print(f"Nombre del usuario: {nombre_completo}")

#procesar o normalizar el nombre del usuario
#Limpiamos los espacio al inicio y al final

nombre_normalizado = nombre_completo.strip()
#Reemplazamos los espacio en blanco por puntos
nombre_normalizado = nombre_normalizado.replace(" ", ".")
print(f"Espacios reemplazados por puntos: {nombre_normalizado}")

#Datos de la empreza
nombre_empresa = "Global Mentoring"
print(f"Nombre de la empresa: {nombre_empresa}")

extesion_dominio = ".com.co"
print(f"Extension del dominio: {extesion_dominio}")

#Quitamos los espacios en blanco
nombre_empresa_normalizado = nombre_empresa.replace(" ", "") #aqui se quitaron los espacios en blanco

dominio_email_normalizado = f"@{nombre_empresa_normalizado}{extesion_dominio}"
email = f"{nombre_normalizado}{dominio_email_normalizado}"
print(f"Dominio del email normalizado: {dominio_email_normalizado}\n")
print(f"Email asignado: {email}")
