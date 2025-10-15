'''
Ejercicio 4: Escribir un programa que tenga 4 variables, una lista, un string, un 
entero y un booleano y que imprima un mensaje según el tipo de dato de cada variable
usando funciones.
'''

def imprimir_tipo(variable):
    print(f"El tipo de dato de la variable {variable} es: {type(variable)}")

lista = [1, 2, 3]
cadena = "Hola"
entero = 42
booleano = True

imprimir_tipo(lista)
imprimir_tipo(cadena)
imprimir_tipo(entero)
imprimir_tipo(booleano)