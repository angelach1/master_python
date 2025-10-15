'''
Ejercicio 1: Crear un programa que tenga una lista de 8 números enteros y realice las siguientes operaciones:
- Mostrar la lista de números.
- Mostrar la lista ordenada de menor a mayor.
- Hacer una funcion que recorra la lista y devuelva una cadena con todos los números concatenados.  
- Mostrar su longitud.
- Buscar algun número dentro de la lista que el usuario introduzca por teclado.
'''
def concatenar_numeros(lista):
    resultado = ''
    for numero in lista:
        resultado += str(numero) + ' '
    return resultado

numeros = [34, 7, 23, 32, 5, 62, 32, 19]
print("Lista de números:", numeros)
print("Lista ordenada de menor a mayor:", sorted(numeros))
print("Concatenación de números:", concatenar_numeros(numeros))
print("Longitud de la lista:", len(numeros))
busqueda = int(input("Introduce un número a buscar: "))
comprobar =  isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    print("Error: Debes introducir un número entero positivo.")
    busqueda = int(input("Introduce un número a buscar: "))
    comprobar =  isinstance(busqueda, int)
else:
    print(f'El número {busqueda} {"está" if busqueda in numeros else "no está"} en la lista.')
    
    