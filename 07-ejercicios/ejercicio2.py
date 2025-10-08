"""
Ejercicio 2.
Escribir un script que nos muestre por pantalla los números pares del 1 al 120

"""
for numero in range(1, 121):
    if numero % 2 == 0:
        print(f'{numero} es par')
    else:
        print(f"{numero} es impar")


'''
# Otra forma de hacerlo
print("Otra forma de hacerlo")
for numero in range(2, 121, 2):
    print(numero)

# Otra forma de hacerlo
print("Otra forma de hacerlo")
for numero in range(1, 121):
    if not numero % 2:
        print(numero)

# Otra forma de hacerlo
print("Otra forma de hacerlo")
for numero in range(1, 121):
    if numero & 1 == 0: # Operación bit a bit
        print(numero)

'''