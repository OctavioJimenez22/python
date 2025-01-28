edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print(f"Eres mayor de edad. Tienes {edad} años")
elif 13 <= edad < 18:
    print(f"Eres un adolencente. Tienes {edad} años")
else:
    print(f"Eres un niño. Tienes {edad} años")
    