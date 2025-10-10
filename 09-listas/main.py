'''
LISTAS (ARRAYS)
Son colecciones o conjuntos de datos/valores, bajo un mismo nombre.
Se accede a esos valores mediante un índice númerico.
Los valores se pueden modificar, agregar y eliminar.
Se pueden mezclar diferentes tipos de datos.

Sintaxis:
nombre_lista = [dato1, dato2, dato3, ...]

'''
# Definición de una lista
peliculas = ['Batman', 'Spiderman', 'El señor de los anillos']
cantantes = list(('2pac', 'Drake', 'Jennifer Lopez'))
years = list(range(2001, 2023))
variada = ['Miguel', 45, 1.75, True, 'Colombia']
print(peliculas)
print(cantantes)
print(years)
print(variada)

# Acceder a los elementos de una lista
print(peliculas[0])
print(peliculas[-2]) # Indice negativo (empieza desde el final de la lista)
print(cantantes[1])
print(years[5])
print(variada[3])
print(variada[1:3]) # Rango de índices (no incluye el último índice)
print(variada[:2]) # Desde el inicio hasta el índice 2 (no incluye el índice 2)
print(variada[2:]) # Desde el índice 2 hasta el final
print(variada[-3:]) # Últimos 3 elementos
print(variada[:-2]) # Todos menos los últimos 2 elementos

# Modificar elementos de una lista
print(peliculas)
peliculas[1] = 'Ironman'
print(peliculas)
peliculas[-1] = 'El hobbit'
print(peliculas)

# Agregar elementos a una lista
print(cantantes)
cantantes.append('Bad Bunny')
print(cantantes)
cantantes.insert(1, 'J Balvin')
print(cantantes)
cantantes.extend(['Shakira', 'Luis Fonsi'])
print(cantantes)
cantantes += ['Karol G', 'Maluma']
print(cantantes)
cantantes += 'Nicky Jam' # Agrega cada letra como un elemento
print(cantantes)

#Recprrer una lista
for cantante in cantantes:
    print(cantante)
for i in range(len(cantantes)):
    print(cantantes[i])
for i, cantante in enumerate(cantantes):
    print(i, cantante)

print('\n****************LISTADO DE PELICULAS****************\n')

nueva_pelicula = ''
while nueva_pelicula.lower() != 'salir':
    nueva_pelicula = input('Introduce una película (o "salir" para terminar): ')
    if nueva_pelicula.lower() != 'salir':
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f'{peliculas.index(pelicula) + 1} - {pelicula}')

# Eliminar elementos de una lista
print(peliculas)
peliculas.pop() # Elimina el último elemento
print(peliculas)
peliculas.pop(0) # Elimina el elemento en el índice 0
print(peliculas)
peliculas.remove('Ironman') # Elimina el elemento con el valor 'Ironman'
print(peliculas)
peliculas.clear() # Elimina todos los elementos de la lista
print(peliculas)
del peliculas # Elimina la lista completa
#print(peliculas) # Error, la lista ya no existe

# listas multidimensionales (matrices)
print('\n****************LISTAS MULTIDIMENSIONALES****************\n')
contactos = [
    ['Antonio', 'antonio@example.com', '123-456-7890'],
    ['Beatriz', 'beatriz@example.com', '987-654-3210'],
    ['Carlos', 'carlos@example.com', '555-555-5555']
]
print(contactos)

# Acceder a elementos de listas multidimensionales
print(contactos[0]) # Primer contacto
print(contactos[1][1]) # Email de Beatriz
print(contactos[2][2]) # Teléfono de Carlos

# Modificar elementos de listas multidimensionales
contactos[0][0] = 'Antonio Pérez'
print(contactos)

# Agregar elementos a listas multidimensionales
contactos.append(['David', 'david@example.com', '444-444-4444'])
print(contactos)

# Eliminar elementos de listas multidimensionales
del contactos[1]
print(contactos)