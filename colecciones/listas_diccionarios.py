print('Listas y diccionarios\n')

personas = [
    {
        'nombre': 'Tavo',
        'apellido': 'jimenez',
        'edad': 26
    },
    {
        'nombre': 'Maria',
        'apellido': 'Gomez',
        'edad': 22
    },
    {
        'nombre': 'Carlos',
        'apellido': 'Perez',
        'edad': 30
    }
]
print(personas)

#acceder a un diccionario desde una lista
print(f'nombre: {personas[0].get('nombre')}\n')
for persona in personas:
    print(f'nombre: {persona.get('nombre')}, apellido: {persona.get('apellido')}, edad: {persona.get('edad')}')

print()

for contador, persona in enumerate(personas):
    print(f'Persona {contador + 1}: {persona.get('nombre')} {persona.get('apellido')} - {persona.get('edad')} años')

