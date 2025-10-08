"""
# Bucle While
El bucle while ejecuta un bloque de código mientras una condición sea verdadera.
Sintaxis:
while condición:
     bloque de código
     ...
     ...
     actualización de la condición (opcional)
else:
    bloque de código (opcional)
    ...
   
"""

contador = 1

while contador <= 100:
    print(f"Voy por el número {contador}" )
    contador += 1  # actualización de la condición  

print("-----------------------------")
# Ejercicio: Mostrar números del 1 al 100 en una sola línea separados por comas

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1  # actualización de la condición
print(muestrame)

print("-----------------------------")
# Ejercicio: Pedir un número al usuario y mostrar su tabla de multiplicar
numero_usuario = int(input("¿De qué número quieres la tabla? "))
if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla de multiplicar del {numero_usuario}")
contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1  # actualización de la condición
else:
    print("Tabla finalizada")

print("-----------------------------")
