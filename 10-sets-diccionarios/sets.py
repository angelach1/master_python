'''
SET es un tipo de dato que almacena una colección de elementos únicos y desordenados.

'''
personas = {'Juan', 'Ana', 'Pedro', 'Luis'}

print(personas)
print(type(personas))

personas.add('Maria')
print(personas)

personas.add('Juan') # No se agrega porque ya existe

personas.remove('Ana')

