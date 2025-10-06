nada = None
cadena = "Hola, soy Víctor Robles WEB"
entero = 10
decimal = 3.14
booleano = True
complejo = 1 + 2j
lista = [10, 20, 30, 100, 200]
listaString = [44, "treinta", 30, "cuarenta"]
tupla = ("master", "en", "python") # inmutable
diccionario = {
    "nombre": "Víctor",
     "apellido": "Robles",
     "curso": "Python"
}
rango = range(9) # 0 a 8
dato_byte = b"Probando" # datos en bytes
set_datos = {1, 2, 3, 4, 5} 
frozenset_datos = frozenset({1, 2, 3, 4, 5}) # inmutable


# Imprimir variable  y mostrar su tipo
print(nada)
print(type(nada))
"""
print(cadena)
print(type(cadena))
print(entero)
print(type(entero))
print(decimal)
print(type(decimal))
print(booleano)
print(type(booleano))
print(complejo)
print(type(complejo))
print(lista)
print(type(lista))
print(listaString)
print(type(listaString))
print(tupla)
print(type(tupla))
print(diccionario)
print(type(diccionario))
print(rango)
print(type(rango))
print(dato_byte)
print(type(dato_byte))
print(set_datos)
print(type(set_datos))
print(frozenset_datos)
print(type(frozenset_datos))
"""
 # Conversión de tipos
print("Conversión de tipos")
texto = "Hola soy un texto"
numerito = str(776)
print(type(texto))
print(type(numerito))
print(texto + " " + numerito) # Concatenación
numerito = float(776)
print(numerito)
print(type(numerito))   
print(texto + " " + str(numerito)) # Concatenación
