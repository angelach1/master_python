"""
Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto
"""

# Crear variables y asignarles un valor
texto = "Máster en Python "
texto2 = "con Victor Robles"
numero = 45
decimal = 6.7

# Mostrar el valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("------------------------------")

# Sustituir el valor de las variables
numero = 77
decimal = 8.9

print(numero)
print(decimal)

print("------------------------------")

# Concatenar variables
nombre = "Víctor"
apellidos = "Robles"
web = "victorroblesweb.es"
print(nombre + " " + apellidos + " - " + web)
print(f"{nombre} {apellidos} - {web}")  
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))

print(nombre, apellidos, web)  # Con comas añade espacios automáticos
print("Hola me llamo", nombre, apellidos, "y mi web es:", web)


