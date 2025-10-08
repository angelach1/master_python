'''
Ejercicio 6
Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el título de la tabla y luego los resultados de la tabla.

'''
for tabla in range(1, 11):
    print(f'Tabla del {tabla}')
    for numero in range(1, 11):
        print(f'{tabla} x {numero} = {tabla * numero}')
    print()  # Línea en blanco entre tablas

# Otra forma de hacerlo
print("Otra forma de hacerlo")
for tabla in range(1, 11):
    print(f'Tabla del {tabla}')
    for numero in range(1, 11):
        resultado = tabla * numero
        print(f'{tabla} x {numero} = {resultado}')
    print()  # Línea en blanco entre tablas
    # Otra forma de hacerlo
print("Otra forma de hacerlo")
for tabla in range(1, 11):
    print(f'Tabla del {tabla}')
    for numero in range(1, 11):
        print(f'{tabla} x {numero} = {tabla * numero}')
    print()  # Línea en blanco entre tablas
    # Otra forma de hacerlo
