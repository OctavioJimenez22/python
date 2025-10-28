nombre = input("Nombre: ")
apellido = input("Apellido: ")
empresa = input("Nombre de la empresa: ")
extesion_dominio = ".com.co"


#normalizamos los datos pedidos
nombre = nombre.strip().lower().replace(" ", ".")
apellido = apellido.strip().lower().replace(" ", ".")
empresa = empresa.strip().lower().replace(" ","")
extesion_dominio = extesion_dominio.strip().lower().replace(" ", ".")

email = f"{nombre}.{apellido}@{empresa}{extesion_dominio}"
print(f"Tu nuevo email generado por el sistema es:\n\t{email}\n\tFelicitaciones!!")
