print('Agenda de contactos')

agenda = {
    'Carlos': {
        'telefono': '2423432',
        'email' : 'carlos@.com',
        'dirrecion' : 'calle3232#2323'
    },
    'Maria': {
        'telefono': '5555',
        'email' : 'Maria@.com',      
        'dirrecion' : 'calle23#3434'    
    },
    'Tavo':{
        'telefono': '43434',
        'email' : 'tavo@.com',
        'dirrecion' : 'calle3333#222'
    }
}
print(f'Agenda: {agenda}')

#Aceder a un contacto especifico
print('\n')
print(f'Email de Tavo es: {agenda['Tavo']['email']}')
print(f'la direccion de Tavo es: {agenda['Tavo']['dirrecion']}')
print(f'Telefono de Tavo: {agenda.get('Tavo').get('telefono')}')

#Agregar un nuevo contacto
agenda['Pepito'] = {
    'telefono': '7777',
    'email' : 'pepito@.com',
    'dirrecion' : 'calle777#777'
}
print(f'\nAgenda actualizada: {agenda}')

#eliminar un contacto
agenda.pop('Maria')
print(f'\nAgenda actualizada: {agenda}')