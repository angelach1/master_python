cantantes = ['2pac', 'Drake', 'Jennifer Lopez']
numeros = [1, 2, 3, 4, 5, 9, 7, -1, 12]

# Ordenar listas

print(numeros)
numeros.sort()  # Ordena la lista de menor a mayor  
print(numeros)

# Agregar elementos a una lista
cantantes.append('Nicky Jam')  # Agrega un elemento al final de la lista
print(cantantes)
cantantes.insert(1, 'Ricky Martin')  # Agrega un elemento en la posición indicada
print(cantantes)

'''
# Eliminar elementos de una lista
cantantes.remove('Drake')  # Elimina el elemento indicado
print(cantantes)
cantantes.pop(2)  # Elimina el elemento en la posición indicada
print(cantantes)
cantantes.pop()  # Elimina el último elemento de la lista
print(cantantes)
cantantes.clear()  # Elimina todos los elementos de la lista
print(cantantes) 
del numeros[0]  # Elimina el elemento en la posición indicada
print(numeros)
del numeros  # Elimina la lista completa
# print(numeros)  # Esto generará un error porque la lista ya no existe
'''

# Dar la vuelta a una lista
numeros = [1, 2, 3, 4, 5, 9, 7, -1, 12]
numeros.reverse()  # Da la vuelta a la lista
print(numeros)

# Buscar dentro de una lista
print('Drake' in cantantes)  # Devuelve True si el elemento está en la lista
print('Nicky Jam' in cantantes)  # Devuelve False si el elemento no está en la lista
print(cantantes.index('Nicky Jam'))  # Devuelve la posición del elemento indicado
print(numeros.index(3))  # Devuelve la posición del elemento indicado   
print(3 in numeros)  # Devuelve True si el elemento está en la lista
print(15 in numeros)  # Devuelve False si el elemento no está en la lista

#Contar elementos en una lista
print(len(numeros))  # Devuelve el número de elementos en la lista
print(len(cantantes))  # Devuelve el número de elementos en la lista

# Cuántas veces se repite un elemento en una lista
numeros.append(3)
print(numeros.count(3))  # Devuelve cuántas veces se repite el elemento indicado
print(numeros)
print(cantantes.count('Nicky Jam'))  # Devuelve cuántas veces se repite el elemento indicado
cantantes.append('Nicky Jam')
print(cantantes)

# Unir listas
cantantes2 = ['Karol G', 'Maluma']
cantantes_completo = cantantes + cantantes2  # Une dos listas
print(cantantes_completo)
print(cantantes)
cantantes.extend(cantantes2)  # Agrega los elementos de una lista a otra
print(cantantes)
print(cantantes2)

# Convertir una cadena en una lista
cadena = "Hola que tal"
print(cadena)
print(cadena.split())  # Convierte una cadena en una lista, separando por espacios
cadena2 = "Hola,que,tal"
print(cadena2.split(','))  # Convierte una cadena en una lista, separando por comas
cadena3 = "Hola-que-tal"
print(cadena3.split('-'))  # Convierte una cadena en una lista, separando por guiones











