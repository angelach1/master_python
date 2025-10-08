'''
Ejercicio 3. Escribir un programa que muestre los cuadrados
de los 60 primeros números naturales.

Resolverlo con un bucle for y con un bucle while.
'''

# Con el bucle while
print("Con el bucle while")
contador = 1
while contador <= 60:
    print(f'El cuadrado de {contador} es {contador**2}')
    contador += 1

# Con el bucle for
print("Con el bucle for")
for numero in range(1, 61):
    print(f'El cuadrado de {numero} es {numero**2}')

