'''
Ejercicio 2: escribir un programa que añada valores a una lista mientras que
su longitud sea menor a 120 y luego mostrar la lista completa.
plus: hacerlo con un bucle for y con un bucle while.
'''
coleccion = []
for i in range(120):
    coleccion.append(i)
print("Lista completa (bucle for):", coleccion)

coleccion = []
i = 0
while len(coleccion) < 120:
    coleccion.append(i)
    i += 1
print("Lista completa (bucle while):", coleccion)