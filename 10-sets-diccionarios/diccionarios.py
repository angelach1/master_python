'''
Diccionario:
Un diccionario es una colección desordenada de elementos que se almacenan en pares clave-valor.
Cada clave es única y se utiliza para acceder a su valor correspondiente.
Los diccionarios son mutables, lo que significa que sus elementos pueden ser modificados después de su creación.

'''

persona = {
    'nombre': 'Victor',
    'apellido': 'Robles',
    'edad': 35,
    'pais': 'España',
    'web': 'victorrobles.es'
}

print(persona)
print(persona['apellido'])

# Lista con diccionarios

personas = [
    {
        'nombre': 'Victor',
        'apellido': 'Robles',
        'edad': 35
    },
    {
        'nombre': 'Ana',
        'apellido': 'García',
        'edad': 28
    },
    {
        'nombre': 'Pedro',
        'apellido': 'Martínez',
        'edad': 42
    }
]

print(personas)
print(personas[1]['nombre'])
print(personas[2]['edad'])
personas[0]['nombre'] = 'Ángel'

print('\nListado de contactos:')
for persona in personas:
    print(f"{persona['nombre']} {persona['apellido']} - {persona['edad']} años")
