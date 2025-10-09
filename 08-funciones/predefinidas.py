'''
Funciones predefinidas (integradas) en Python

'''
nombre = "Ángel Alhambra"

#funciones generales
print(type(nombre))

#Detectar el tipo de dato
comprobar = isinstance(nombre, str)

if comprobar:
    print("Es una cadena")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("No es un número con decimales")

# Limpiar espacios
frase = "   mi contenido   "
print(frase)
print(frase.strip())

# Eliminar variables
year = 2024
print(year)
del year
# print(year) # NameError: name 'year' is not defined

# Comprobar variable vacía
texto = ""
if len(texto) == 0:
    print("La variable está vacía")
if texto == "":
    print("La variable está vacía") 
if not texto:
    print("La variable está vacía")

# Encotrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))
print(frase.find("vida123")) # -1 si no lo encuentra
print(frase.index("vida"))
# print(frase.index("vida123")) # ValueError si no lo encuentra

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)
print(frase) # No modifica la frase original

# Mayúsculas y minúsculas
print(nombre.lower())
print(nombre.upper())
print(nombre.capitalize()) # Primera letra en mayúscula
print(nombre.title()) # Primera letra de cada palabra en mayúscula
print(nombre.swapcase()) # Mayúsculas a minúsculas y viceversa

