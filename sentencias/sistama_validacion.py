usuario = "octavio"
contraseña = "jimenez123"
usuario_pedido = input("Usuario: ")
contraseña_pedida = input("Contraseña: ")

if usuario_pedido == usuario and  contraseña == contraseña_pedida:
    print(f"{usuario}. Bienvenido al sistema")
elif usuario != usuario_pedido and contraseña == contraseña_pedida:
    print("Usuario invalido")
elif usuario == usuario_pedido and contraseña != contraseña_pedida:
    print("Contraseña invalida")
else:
    print("Contraseña y usuario invalidos")
